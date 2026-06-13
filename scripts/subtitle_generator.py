#!/usr/bin/env python3
"""字幕生成器：根据语音时长数据生成SRT字幕"""

import json

def generate_srt(durations_path: str, output_path: str,
                 max_chars_per_line: int = 24, min_gap: float = 0.3):
    """
    生成SRT字幕文件。

    参数：
        durations_path: segment_durations.json 路径
        output_path: 输出的 .srt 文件路径
        max_chars_per_line: 每行最大字符数（中文约24字/行较舒适）
        min_gap: 字幕段间最小间隔（秒），避免连续切换
    """
    with open(durations_path, 'r', encoding='utf-8') as f:
        segments = json.load(f)

    srt_entries = []
    index = 1

    for seg in segments:
        text = seg["narration"]
        start = seg["start_time"]
        end = seg["end_time"]

        # 如果一段太长（>8秒），考虑拆分
        duration = end - start
        if duration > 8.0:
            # 按标点拆分
            sub_texts = split_by_punctuation(text, max_chars_per_line)
            sub_duration = duration / len(sub_texts)
            for i, sub in enumerate(sub_texts):
                sub_start = start + i * sub_duration
                sub_end = start + (i + 1) * sub_duration - min_gap
                if sub_end <= sub_start:
                    sub_end = sub_start + sub_duration
                srt_entries.append(format_srt_entry(index, sub_start, sub_end, sub))
                index += 1
        else:
            # 单段直接输出，超长文本换行
            lines = split_by_punctuation(text, max_chars_per_line)
            display_text = "\n".join(lines)
            # 字幕提前0.1秒出现，晚0.2秒消失，增强可读性
            srt_entries.append(format_srt_entry(
                index, start - 0.1, end + 0.2, display_text
            ))
            index += 1

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(srt_entries))

    print(f"字幕文件已生成: {output_path} ({index-1} 条)")

def split_by_punctuation(text: str, max_chars: int) -> list:
    """按标点拆分长句，每行不超过max_chars个字符"""
    import re
    # 在中文标点处断开
    sentences = re.split(r'([，。；：！？、])', text)
    result = []
    current = ""
    for i, part in enumerate(sentences):
        current += part
        # 标点后断行，或超过最大长度时断行
        if part in '，。；：！？、' or len(current) >= max_chars:
            if current.strip():
                result.append(current.strip())
            current = ""
    if current.strip():
        result.append(current.strip())

    # 合并过短的行
    merged = []
    for line in result:
        if merged and len(merged[-1]) + len(line) <= max_chars:
            merged[-1] = merged[-1] + line
        else:
            merged.append(line)

    return merged if merged else [text]

def format_srt_entry(index: int, start: float, end: float, text: str) -> str:
    """格式化单条SRT条目"""
    return f"{index}\n{format_srt_time(start)} --> {format_srt_time(end)}\n{text}\n"

def format_srt_time(seconds: float) -> str:
    """将秒数转换为SRT时间格式 HH:MM:SS,mmm"""
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("用法: subtitle_generator.py <durations.json> <output.srt>")
        sys.exit(1)
    generate_srt(sys.argv[1], sys.argv[2])