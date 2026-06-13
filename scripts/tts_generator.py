#!/usr/bin/env python3
"""TTS生成器：逐段生成语音并记录每段时长"""

import asyncio
import json
import edge_tts
import os

async def generate_segment(text: str, voice: str, output_path: str) -> float:
    """生成单段语音，返回时长（秒）"""
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)

    # 用ffprobe获取精确时长
    import subprocess
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
         "-of", "default=noprint_wrappers=1:nokey=1", output_path],
        capture_output=True, text=True
    )
    return float(result.stdout.strip())

async def generate_all(script_path: str, output_dir: str):
    """根据教学脚本生成全部语音段"""
    with open(script_path, 'r', encoding='utf-8') as f:
        script = json.load(f)

    voice = script.get("voice", "zh-CN-YunxiNeural")
    segments = script["segments"]

    os.makedirs(output_dir, exist_ok=True)
    durations = {}
    segment_files = []

    for seg in segments:
        seg_id = seg["id"]
        seg_file = os.path.join(output_dir, f"{seg_id}.mp3")
        duration = await generate_segment(seg["narration"], voice, seg_file)
        durations[seg_id] = duration
        segment_files.append(seg_file)
        print(f"  ✓ {seg_id}: {duration:.2f}s")

    # 合并所有段为一个完整音频
    concat_list = os.path.join(output_dir, "concat_list.txt")
    with open(concat_list, 'w') as f:
        for sf in segment_files:
            f.write(f"file '{os.path.abspath(sf)}'\n")

    full_audio = os.path.join(output_dir, "narration.mp3")
    os.system(f"ffmpeg -y -f concat -safe 0 -i {concat_list} -c:a libmp3lame -q:a 2 {full_audio}")

    # 保存时长数据（含累积时间，供字幕和时间轴使用）
    cumulative = 0.0
    timeline_data = []
    for seg in segments:
        seg_id = seg["id"]
        dur = durations[seg_id]
        timeline_data.append({
            "id": seg_id,
            "section": seg["section"],
            "animation_hint": seg["animation_hint"],
            "duration": round(dur, 3),
            "start_time": round(cumulative, 3),
            "end_time": round(cumulative + dur, 3),
            "narration": seg["narration"]
        })
        cumulative += dur

    durations_path = os.path.join(output_dir, "segment_durations.json")
    with open(durations_path, 'w', encoding='utf-8') as f:
        json.dump(timeline_data, f, ensure_ascii=False, indent=2)

    total_duration = sum(durations.values())
    print(f"\n总计 {len(segments)} 段语音，总时长 {total_duration:.2f}s")
    print(f"完整音频: {full_audio}")
    print(f"时长数据: {durations_path}")

    return durations_path, full_audio

def run(script_path: str, output_dir: str = "./output/audio"):
    asyncio.run(generate_all(script_path, output_dir))

if __name__ == "__main__":
    import sys
    run(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "./output/audio")