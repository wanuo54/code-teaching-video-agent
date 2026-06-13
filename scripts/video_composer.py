#!/usr/bin/env python3
"""视频合成器：合并动画+语音+字幕为最终教学视频"""

import subprocess
import os

def compose(video_path: str, audio_path: str, subtitle_path: str,
            output_path: str, burn_subtitle: bool = True):
    """
    合成最终视频。

    参数：
        video_path: Manim渲染的无声动画 mp4
        audio_path: TTS生成的完整语音 mp3
        subtitle_path: SRT字幕文件
        output_path: 最终输出 mp4
        burn_subtitle: 是否将字幕烧录到视频中（硬字幕）
    """
    if burn_subtitle and os.path.exists(subtitle_path):
        # 硬字幕：字幕烧录进视频画面
        # subtitles filter 会自动处理中文编码
        cmd = [
            "ffmpeg", "-y",
            "-i", video_path,
            "-i", audio_path,
            "-vf", f"subtitles={subtitle_path}:force_style='FontName=WenQuanYi Zen Hei,FontSize=18,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,Outline=2,MarginV=30'",
            "-c:v", "libx264", "-preset", "medium", "-crf", "23",
            "-c:a", "aac", "-b:a", "128k",
            "-shortest",
            output_path
        ]
    else:
        # 无字幕或软字幕
        cmd = [
            "ffmpeg", "-y",
            "-i", video_path,
            "-i", audio_path,
            "-c:v", "libx264", "-preset", "medium", "-crf", "23",
            "-c:a", "aac", "-b:a", "128k",
            "-shortest",
            output_path
        ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"合成失败: {result.stderr}")
        return False

    file_size = os.path.getsize(output_path) / (1024 * 1024)
    print(f"✓ 合成完成: {output_path} ({file_size:.1f} MB)")
    return True

def compose_with_soft_subtitle(video_path: str, audio_path: str,
                                subtitle_path: str, output_path: str):
    """软字幕：字幕作为独立轨道嵌入，播放器可开关"""
    cmd = [
        "ffmpeg", "-y",
        "-i", video_path,
        "-i", audio_path,
        "-i", subtitle_path,
        "-c:v", "libx264", "-preset", "medium", "-crf", "23",
        "-c:a", "aac", "-b:a", "128k",
        "-c:s", "mov_text",           # MP4兼容的字幕编码
        "-metadata:s:s:0", "language=chi",
        "-shortest",
        output_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"软字幕合成失败: {result.stderr}")
        return False

    file_size = os.path.getsize(output_path) / (1024 * 1024)
    print(f"✓ 软字幕合成完成: {output_path} ({file_size:.1f} MB)")
    return True

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("用法: video_composer.py <video.mp4> <audio.mp3> <subtitle.srt> [output.mp4]")
        sys.exit(1)
    video = sys.argv[1]
    audio = sys.argv[2]
    subtitle = sys.argv[3]
    output = sys.argv[4] if len(sys.argv) > 4 else "output/final.mp4"
    compose(video, audio, subtitle, output)