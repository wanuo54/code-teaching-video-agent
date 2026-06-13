# Code Teaching Video Agent

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

将用户输入的代码自动转换为AI教学视频的Trae Skill，同时支持coze扣子平台。

## 简介

Code Teaching Video Agent 是一个强大的代码教学视频生成工具，能够将任意代码转换为专业的教学视频，包含：

- 可视化动画演示
- 中文语音讲解
- 中文字幕
- 代码执行演示
- 算法与数据结构可视化
- 调用栈与变量跟踪动画

**目标：** 帮助用户真正理解代码逻辑，而不仅仅是观看代码执行过程。

**最终效果接近：**
- B站算法讲解视频
- 编程教学课程视频
- AI 编程老师讲课

而不是简单的代码执行录像。

## 功能特性

### 核心能力

- **代码结构分析**：AST分析、控制流分析（CFG）、依赖分析、函数调用关系分析
- **算法类型自动识别**：支持10大类、70+算法的自动分类
  - 数据结构类（数组、链表、栈、队列、树、图等）
  - 排序算法类（冒泡、选择、插入、快速、归并、堆排序等）
  - 查找算法类（顺序查找、二分查找、哈希查找等）
  - 递归与分治类（汉诺塔、归并排序、快速排序等）
  - 动态规划类（背包问题、LCS、编辑距离等）
  - 贪心算法类（活动选择、哈夫曼编码等）
  - 图论算法类（DFS、BFS、Dijkstra、Prim、Kruskal等）
  - 回溯算法类（全排列、N皇后、数独等）
  - 字符串算法类（KMP、AC自动机等）
  - 高级专题类（A*搜索、快速幂、凸包等）
- **教学策略规划**：根据用户水平（初学者/中级/高级）自动调整教学策略
- **语音讲解生成**：使用edge-tts生成高质量中文语音
- **可视化动画渲染**：使用Manim生成专业教学动画
- **视频合成与字幕**：自动合成视频、音频、字幕

### 技术架构

采用7个核心Stage的流水线架构：

```
User Code
│
▼
Stage 1: Code Analyzer（代码结构分析）
│
▼
Stage 2: Code Type Classifier（代码类型分类）
│
▼
Stage 3: Pedagogical Planner（教学规划）
│
▼
Stage 4: Teaching Script Generator（教学脚本生成）
│
▼
Stage 5: Storyboard Generator（分镜生成）
│
▼
Stage 6: Timeline Planner（时间轴规划）
│   ├── TTS Generator（语音生成）
│   └── Manim Renderer（动画渲染）
│
▼
Stage 7: Video Composer（视频合成）
│
▼
Final Teaching Video
```

## 系统要求

### Python版本
- **最低版本：** Python 3.8+
- **推荐版本：** Python 3.10+

### 系统依赖
- **ffmpeg**：视频处理必需（需单独安装）
- **LaTeX**：Manim渲染必需（可选，用于高级数学公式渲染）

### 操作系统
- Windows 10/11
- macOS 10.15+
- Linux（Ubuntu 18.04+）

## 安装

### 1. 安装系统依赖

#### Windows
```bash
# 安装ffmpeg
# 从 https://ffmpeg.org/download.html 下载并安装

# 安装LaTeX（可选）
# 从 https://miktex.org/ 下载并安装
```

#### macOS
```bash
# 使用Homebrew安装
brew install ffmpeg
brew install mactex  # 可选
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg
sudo apt-get install texlive-full  # 可选
```

### 2. 克隆仓库
```bash
git clone https://github.com/[username]/code-teaching-video-agent.git
cd code-teaching-video-agent
```

### 3. 安装Python依赖
```bash
pip install -r requirements.txt
```

或使用现代安装方式：
```bash
pip install .
```

## 使用方法

### 作为Trae Skill使用

将本项目作为Trae Skill加载：

1. 将 `SKILL.md` 文件放置到Trae的skills目录
2. 在Trae中触发关键词：
   - "把这段代码做成视频"
   - "生成代码讲解视频"
   - "可视化代码执行过程"
   - "用动画解释这段代码"
   - "帮我理解这段代码"
   - "制作算法动画"

### 作为独立工具使用

```python
from scripts.pipeline import CodeTeachingPipeline

# 创建pipeline实例
pipeline = CodeTeachingPipeline()

# 输入代码
code = """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
"""

# 生成教学视频
result = pipeline.run(
    code=code,
    user_level="BEGINNER",  # BEGINNER, INTERMEDIATE, ADVANCED
    output_path="output/bubble_sort_tutorial.mp4"
)

print(f"视频已生成: {result['video_path']}")
```

### 命令行使用

```bash
python scripts/pipeline.py --code examples/input/bubble_sort.py --level BEGINNER --output output/tutorial.mp4
```

## 项目结构

```
code-teaching-video-agent/
├── SKILL.md                    # 核心skill定义文件
├── README.md                   # 项目说明文档
├── LICENSE                     # MIT许可证
├── requirements.txt            # Python依赖列表
├── setup.py                    # 项目安装配置
├── pyproject.toml              # 现代Python项目配置
├── .gitignore                  # Git忽略文件
│
├── scripts/                    # 核心脚本目录
│   ├── pipeline.py             # 主控脚本
│   ├── code_analyzer.py        # Stage 1: 代码分析
│   ├── classifier.py           # Stage 2: 类型分类
│   ├── pedagogical_planner.py  # Stage 3: 教学规划
│   ├── script_generator.py     # Stage 4: 脚本生成
│   ├── storyboard_generator.py # Stage 5: 分镜生成
│   ├── timeline_planner.py     # Stage 6: 时间轴规划
│   ├── tts_generator.py        # 语音生成
│   ├── subtitle_generator.py   # 字幕生成
│   ├── manim_renderer.py       # 动画渲染
│   ├── video_composer.py       # Stage 7: 视频合成
│   └── audio_driven_scene.py   # Manim基类
│
├── templates/                  # 算法模板目录
│   ├── sorting/                # 排序算法模板
│   │   ├── bubble.py
│   │   ├── quick.py
│   │   ├── merge.py
│   │   └── heap.py
│   ├── searching/              # 查找算法模板
│   ├── recursion/              # 递归算法模板
│   ├── dp/                     # 动态规划模板
│   │   ├── knapsack_01.py
│   │   └── lcs.py
│   ├── greedy/                 # 贪心算法模板
│   ├── graph/                  # 图论算法模板
│   │   ├── dijkstra.py
│   │   ├── dfs.py
│   │   └── bfs.py
│   ├── backtracking/           # 回溯算法模板
│   ├── string_algo/            # 字符串算法模板
│   ├── data_structure/         # 数据结构模板
│   └── advanced/               # 高级专题模板
│
├── examples/                   # 示例目录
│   ├── input/                  # 输入示例
│   │   └── bubble_sort.py
│   ├── output/                 # 输出示例（Coze平台生成的样例）
│   │   ├── AOE网关键路径_逆拓扑求vl_教学视频.mp4  # AOE网关键路径教学视频样例
│   │   └── mmexport1781288327497.jpg            # 视频截图样例
│   ├── scripts/                # 教学脚本示例
│   │   └ prim_script.json
│   └ scenes/                   # Manim场景示例
│       └ prim_scene.py
│
├── assets/                     # 资源文件目录
├── output/                     # 输出目录
│
└── docs/                       # 文档目录（适用于Coze扣子平台）
    ├── ARCHITECTURE.md         # 架构文档
    ├── USAGE.md                # 使用指南
    ├── CONTRIBUTING.md         # 贡献指南
    └── CodeVizTeach-Original.md  # 原始Skill定义文档（适用于Coze平台导入）
```

## 示例

### 示例1：冒泡排序教学视频

输入代码：
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

生成视频包含：
- 数组可视化动画
- 每次比较和交换的动画演示
- 中文语音讲解："现在我们比较第j个和第j+1个元素..."
- 中文字幕同步显示
- 时间复杂度分析动画

### 示例2：快速排序教学视频

输入代码：
```python
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
```

生成视频包含：
- 分治策略可视化
- 递归调用栈动画
- pivot选择和分区过程演示
- 时间复杂度分析

### 示例3：Dijkstra最短路径算法

输入代码：
```python
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    visited = set()

    while len(visited) < len(graph):
        current = min(
            (node for node in graph if node not in visited),
            key=lambda node: distances[node]
        )
        visited.add(current)

        for neighbor, weight in graph[current].items():
            if neighbor not in visited:
                new_dist = distances[current] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist

    return distances
```

生成视频包含：
- 图结构可视化
- 节点访问顺序动画
- 最短路径更新过程
- 距离表格动态更新

## 核心依赖

本项目依赖以下核心库：

- **edge-tts** (>=6.1.0)：微软Edge TTS服务，用于生成高质量中文语音
- **manim** (>=0.18.0)：3Blue1Brown开发的数学动画引擎，用于生成教学动画
- **ffmpeg-python** (>=0.2.0)：视频处理工具的Python接口
- **tree-sitter** (>=0.20.0)：代码解析工具，用于AST分析
- **pygments** (>=2.15.0)：代码语法高亮
- **numpy** (>=1.24.0)：数值计算
- **pandas** (>=2.0.0)：数据处理
- **moviepy** (>=1.0.3)：视频编辑库
- **imageio** (>=2.31.0)：图像和视频IO

## 教学策略

根据用户水平自动调整教学策略：

| 用户水平 | 教学侧重 | 特点 |
|---------|---------|------|
| **BEGINNER**（初学者） | 多类比、多动画、慢节奏 | 详细讲解每个步骤，使用生活化类比 |
| **INTERMEDIATE**（中级） | 适度讲解、重点突破 | 聚焦核心逻辑，略过基础概念 |
| **ADVANCED**（高级） | 聚焦核心逻辑、略过基础 | 强调算法思想和优化技巧 |

## 音频驱动管线

采用独特的音频驱动架构，确保音画同步：

```
Teaching Script
│
▼
TTS Generator → Audio Files + Duration Info
│
▼
Timeline Planner → Scene Timing Plan
│
▼
Manim Renderer → Animation Scenes (synced to audio)
│
▼
Video Composer → Final Video + Audio + Subtitles
```

**核心优势：**
- 先生成语音，再驱动动画
- 确保动画时长与语音时长精确匹配
- 避免传统方案的音画不同步问题

## 贡献指南

欢迎贡献代码、算法模板、教学脚本等！

### 贡献方式

1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建Pull Request

### 贡献内容

- **算法模板**：添加新的算法可视化模板
- **教学脚本**：优化教学讲解内容
- **场景库**：扩展Manim场景库
- **文档**：改进文档和示例
- **Bug修复**：修复已知问题

详见 [CONTRIBUTING.md](docs/CONTRIBUTING.md)

## 许可证

本项目采用MIT许可证 - 详见 [LICENSE](LICENSE) 文件

## 致谢

- **Manim**：感谢3Blue1Brown开发的优秀数学动画引擎
- **edge-tts**：感谢微软提供的免费TTS服务
- **Trae**：感谢Trae平台提供的skill框架
- **Coze（扣子）**：感谢Coze扣子平台提供的技能开发支持

## 联系方式

- 项目主页：https://github.com/wanuo54/code-teaching-video-agent
- 问题反馈：https://github.com/wanuo54/code-teaching-video-agent/issues

---

**让代码教学更生动、更易懂！**