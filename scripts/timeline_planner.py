#!/usr/bin/env python3
"""时间轴规划器：将语音时长数据转换为Manim动画控制参数"""

import json

# 动画时间预算比例
# 每段语音的时长不会100%用于主动画，留出过渡空间
ANIMATION_RATIO = 0.85   # 85%时间给主动画
LEAD_IN = 0.15           # 语音开始前0.15秒启动动画（视觉先行）
MIN_WAIT = 0.3           # 段间最小等待

def build_timeline(durations_path: str, output_path: str):
    """
    生成Manim可用的时间轴文件。

    输出格式（timeline.json）：
    {
      "total_duration": 25.5,
      "segments": [
        {
          "id": "seg_01",
          "animation_hint": "show_graph_highlight_u",
          "manim_wait": 5.2,        // 主动画时长（秒）
          "run_time_multiplier": 1.0, // 动画速度倍率
          "lead_in": 0.15,          // 动画提前量
          "start_time": 0.0,        // 在最终视频中的开始时间
          "end_time": 5.35          // 在最终视频中的结束时间
        },
        ...
      ]
    }
    """
    with open(durations_path, 'r', encoding='utf-8') as f:
        segments = json.load(f)

    timeline = {
        "total_duration": 0.0,
        "segments": []
    }

    for seg in segments:
        duration = seg["duration"]
        anim_duration = duration * ANIMATION_RATIO

        entry = {
            "id": seg["id"],
            "section": seg["section"],
            "animation_hint": seg["animation_hint"],
            "narration": seg["narration"],
            "audio_start": seg["start_time"],
            "audio_end": seg["end_time"],
            "audio_duration": round(duration, 3),
            "manim_wait": round(anim_duration, 3),
            "lead_in": LEAD_IN,
            "start_time": round(seg["start_time"] - LEAD_IN, 3),
            "end_time": round(seg["end_time"], 3),
        }
        timeline["segments"].append(entry)

    timeline["total_duration"] = round(segments[-1]["end_time"] + 0.5, 3)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(timeline, f, ensure_ascii=False, indent=2)

    print(f"时间轴已生成: {output_path}")
    print(f"总时长: {timeline['total_duration']:.1f}s, 共 {len(segments)} 段")
    return timeline

if __name__ == "__main__":
    import sys
    build_timeline(sys.argv[1], sys.argv[2])