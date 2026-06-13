#!/usr/bin/env python3
"""音频驱动的Manim场景基类"""

from manim import *
import json

class AudioDrivenScene(Scene):
    """音频驱动的Manim场景基类"""

    def setup(self):
        # 加载时间轴
        with open("output/audio/timeline.json", 'r') as f:
            self.timeline = json.load(f)
        self.seg_index = 0

    def wait_for_narration(self, segment_id: str = None):
        """等待当前段的语音播完，自动同步"""
        if segment_id:
            # 查找指定段
            seg = next(s for s in self.timeline["segments"] if s["id"] == segment_id)
        else:
            # 按顺序取下一段
            seg = self.timeline["segments"][self.seg_index]
            self.seg_index += 1

        wait_time = seg["manim_wait"]
        self.wait(wait_time)

    def get_segment_duration(self, segment_id: str) -> float:
        """获取指定段的语音时长"""
        seg = next(s for s in self.timeline["segments"] if s["id"] == segment_id)
        return seg["audio_duration"]