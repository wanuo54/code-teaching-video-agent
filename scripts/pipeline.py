#!/usr/bin/env python3
"""
Code Teaching Video Agent — 完整渲染管线
一键执行：教学脚本 → TTS → 字幕 → 时间轴 → 动画 → 合成
"""

import os
import sys
import json
import subprocess

# ============================================================
# 配置
# ============================================================
OUTPUT_DIR = "./output"
AUDIO_DIR = os.path.join(OUTPUT_DIR, "audio")
MANIM_QUALITY = "l"  # l=480p15, m=720p30, h=1080p60

def ensure_dirs():
    for d in [OUTPUT_DIR, AUDIO_DIR, os.path.join(OUTPUT_DIR, "video")]:
        os.makedirs(d, exist_ok=True)

# ============================================================
# Stage A: TTS 生成
# ============================================================
def stage_tts(script_path: str):
    print("\n" + "="*60)
    print("Stage A: TTS 语音生成")
    print("="*60)
    from tts_generator import run as tts_run
    tts_run(script_path, AUDIO_DIR)
    return os.path.join(AUDIO_DIR, "segment_durations.json"), \
           os.path.join(AUDIO_DIR, "narration.mp3")

# ============================================================
# Stage B: 字幕生成
# ============================================================
def stage_subtitle(durations_path: str):
    print("\n" + "="*60)
    print("Stage B: 字幕生成")
    print("="*60)
    from subtitle_generator import generate_srt
    srt_path = os.path.join(OUTPUT_DIR, "subtitle.srt")
    generate_srt(durations_path, srt_path)
    return srt_path

# ============================================================
# Stage C: 时间轴规划
# ============================================================
def stage_timeline(durations_path: str):
    print("\n" + "="*60)
    print("Stage C: 时间轴规划")
    print("="*60)
    from timeline_planner import build_timeline
    timeline_path = os.path.join(AUDIO_DIR, "timeline.json")
    build_timeline(durations_path, timeline_path)
    return timeline_path

# ============================================================
# Stage D: Manim 动画渲染
# ============================================================
def stage_manim(scene_file: str, scene_name: str):
    print("\n" + "="*60)
    print("Stage D: Manim 动画渲染")
    print("="*60)
    output_dir = os.path.join(OUTPUT_DIR, "video")
    cmd = [
        "manim", f"-q{MANIM_QUALITY}",
        "--output_file", output_dir,
        scene_file, scene_name
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"渲染失败: {result.stderr}")
        sys.exit(1)

    # 查找生成的视频文件
    for root, dirs, files in os.walk(output_dir):
        for f in files:
            if f.endswith(".mp4") and "media" in f:
                return os.path.join(root, f)

    # 兜底：查找manim默认输出
    media_dir = os.path.join(os.path.dirname(scene_file), "media")
    for root, dirs, files in os.walk(media_dir):
        for f in files:
            if f == "media.mp4":
                return os.path.join(root, f)

    print("未找到渲染输出的视频文件")
    sys.exit(1)

# ============================================================
# Stage E: 合成输出
# ============================================================
def stage_compose(video_path: str, audio_path: str, srt_path: str):
    print("\n" + "="*60)
    print("Stage E: 视频合成")
    print("="*60)
    from video_composer import compose
    final_path = os.path.join(OUTPUT_DIR, "final.mp4")
    compose(video_path, audio_path, srt_path, final_path, burn_subtitle=True)
    return final_path

# ============================================================
# 主流程
# ============================================================
def run(script_path: str, scene_file: str, scene_name: str):
    ensure_dirs()

    # Stage A: 生成语音
    durations_path, audio_path = stage_tts(script_path)

    # Stage B: 生成字幕
    srt_path = stage_subtitle(durations_path)

    # Stage C: 规划时间轴
    timeline_path = stage_timeline(durations_path)

    # Stage D: 渲染动画（此时Manim场景代码应已读取timeline.json）
    video_path = stage_manim(scene_file, scene_name)

    # Stage E: 合成最终视频
    final_path = stage_compose(video_path, audio_path, srt_path)

    print("\n" + "="*60)
    print(f"✅ 全部完成！最终视频: {final_path}")
    print("="*60)
    print(f"  语音: {audio_path}")
    print(f"  字幕: {srt_path}")
    print(f"  时间轴: {timeline_path}")
    print(f"  无声动画: {video_path}")
    print(f"  最终视频: {final_path}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("用法: pipeline.py <教学脚本.json> <场景文件.py> <场景名>")
        print("示例: pipeline.py prim_script.json prim_scene.py PrimWithNarration")
        sys.exit(1)
    run(sys.argv[1], sys.argv[2], sys.argv[3])