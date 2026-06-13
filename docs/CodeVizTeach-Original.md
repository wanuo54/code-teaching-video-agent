---
AIGC:
    Label: "1"
    ContentProducer: 001191110102MACQD9K64018705
    ProduceID: 7634061414809927936-data_volume/files/所有对话/主对话/code-teaching-video-agent-enhanced/SKILL.md
    ReservedCode1: ""
    ContentPropagator: 001191110102MACQD9K64028705
    PropagateID: 933899713385244#1781311007417
    ReservedCode2: ""
---
# Code Teaching Video Agent

## Overview

将用户输入的代码自动转换为：

- AI 教学视频
- 可视化动画
- 中文语音讲解
- 中文字幕
- 代码执行演示
- 算法与数据结构可视化
- 调用栈与变量跟踪动画

目标：

帮助用户真正理解代码逻辑，而不仅仅是观看代码执行过程。

最终效果应接近：

- B站算法讲解视频
- 编程教学课程视频
- AI 编程老师讲课

而不是简单的代码执行录像。

---

## Trigger Conditions

当用户提出以下需求时自动触发：

- 把这段代码做成视频
- 生成代码讲解视频
- 可视化代码执行过程
- 用动画解释这段代码
- 帮我理解这段代码
- 制作算法动画
- Explain this code visually
- Create a code walkthrough video

---

## Core Philosophy

传统方案：

```
Code → Execution → Animation
```

本 Skill：

```
Code → Understanding → Teaching Strategy → Storyboard → Animation → Teaching Video
```

核心目标：

不是回答"代码执行了什么？"，而是回答"用户应该如何理解这段代码？"

---

## Architecture

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
│
├── TTS Generator（语音生成）
└── Manim Renderer（动画渲染）
│
▼
Stage 7: Video Composer（视频合成）
│
▼
Final Teaching Video
```

---

# Stage 1: Code Analyzer

负责解析代码结构。

**支持语言：** Python、JavaScript、Java、C、C++、Go

**分析内容：**

```json
{
  "functions": [],
  "classes": [],
  "loops": [],
  "conditions": [],
  "variables": [],
  "returns": [],
  "calls": [],
  "imports": [],
  "data_structures": [],
  "recursion_depth": 0,
  "complexity_hint": ""
}
```

**能力：** AST 分析、控制流分析（CFG）、依赖分析、函数调用关系分析、递归深度检测

---

# Stage 2: Code Type Classifier

自动识别代码类型，覆盖本科算法全谱系。

## 完整分类体系

### 一、数据结构类（ds）

| type_id | 分类 | 关键词/函数签名 |
|---------|------|----------------|
| `ds_array` | 数组操作 | 索引访问、切片、双指针 |
| `ds_linked_list` | 链表操作 | ListNode、next、prev、头插/尾插 |
| `ds_stack` | 栈操作 | push、pop、peek、括号匹配 |
| `ds_queue` | 队列操作 | enqueue、dequeue、循环队列 |
| `ds_string` | 字符串操作 | 子串匹配、回文、模式匹配 |
| `ds_binary_tree` | 二叉树 | TreeNode、left/right、遍历 |
| `ds_bst` | 二叉搜索树 | 插入/删除/查找、中序有序 |
| `ds_avl` | 平衡二叉树 | 旋转、平衡因子、LL/RR/LR/RL |
| `ds_b_tree` | B树/B+树 | 分裂、合并、多路搜索 |
| `ds_huffman` | 哈夫曼树 | 频率、编码、合并最小 |
| `ds_heap` | 堆 | heapify、sift_up/down、优先队列 |
| `ds_graph` | 图 | 邻接矩阵/邻接表、顶点、边 |
| `ds_hash` | 哈希表 | hash函数、冲突解决、装载因子 |

### 二、排序算法类（sorting）

| type_id | 算法 | 复杂度 | 稳定性 |
|---------|------|--------|--------|
| `sort_bubble` | 冒泡排序 | O(n²) | 稳定 |
| `sort_selection` | 选择排序 | O(n²) | 不稳定 |
| `sort_insertion` | 插入排序 | O(n²) | 稳定 |
| `sort_shell` | 希尔排序 | O(n^1.3) | 不稳定 |
| `sort_quick` | 快速排序 | O(nlogn) | 不稳定 |
| `sort_merge` | 归并排序 | O(nlogn) | 稳定 |
| `sort_heap` | 堆排序 | O(nlogn) | 不稳定 |
| `sort_radix` | 基数排序 | O(d·n) | 稳定 |
| `sort_bucket` | 桶排序 | O(n+k) | 稳定 |
| `sort_counting` | 计数排序 | O(n+k) | 稳定 |

### 三、查找算法类（searching）

| type_id | 算法 |
|---------|------|
| `search_sequential` | 顺序查找 |
| `search_binary` | 二分查找 |
| `search_block` | 分块查找 |
| `search_hash` | 哈希查找 |
| `search_bst` | 二叉搜索树查找 |
| `search_avl` | 平衡树查找 |

### 四、递归与分治类（recursion_divide）

| type_id | 算法 |
|---------|------|
| `rec_basic` | 基础递归（阶乘、斐波那契） |
| `rec_hanoi` | 汉诺塔 |
| `rec_merge_sort` | 归并排序（分治视角） |
| `rec_quick_sort` | 快速排序（分治视角） |
| `rec_big_multiply` | 大数相乘 |
| `rec_chessboard` | 棋盘覆盖 |

### 五、动态规划类（dp）

| type_id | 算法/题型 |
|---------|----------|
| `dp_fibonacci` | 斐波那契数列、爬楼梯 |
| `dp_max_subarray` | 最大子数组和（Kadane） |
| `dp_knapsack_01` | 01背包 |
| `dp_knapsack_complete` | 完全背包 |
| `dp_knapsack_multiple` | 多重背包 |
| `dp_lis` | 最长上升子序列 |
| `dp_lcs` | 最长公共子序列 |
| `dp_edit_distance` | 最短编辑距离 |
| `dp_matrix_chain` | 矩阵连乘 |
| `dp_stone_merge` | 石子合并 |
| `dp_path` | 路径问题（不同路径、最小路径和） |

### 六、贪心算法类（greedy）

| type_id | 算法 |
|---------|------|
| `greedy_activity` | 活动选择问题 |
| `greedy_coin` | 零钱兑换（贪心版） |
| `greedy_huffman` | 哈夫曼编码 |
| `greedy_interval` | 区间覆盖/区间选点 |
| `greedy_fractional_knapsack` | 分数背包 |

### 七、图论算法类（graph）

| type_id | 算法 |
|---------|------|
| `graph_dfs` | 深度优先搜索 |
| `graph_bfs` | 广度优先搜索 |
| `graph_dijkstra` | Dijkstra 最短路径 |
| `graph_bellman_ford` | Bellman-Ford |
| `graph_spfa` | SPFA |
| `graph_floyd` | Floyd-Warshall |
| `graph_prim` | Prim 最小生成树 |
| `graph_kruskal` | Kruskal 最小生成树 |
| `graph_topological` | 拓扑排序 |
| `graph_critical_path` | 关键路径（AOE网） |
| `graph_hungarian` | 匈牙利算法（二分图匹配） |
| `graph_tarjan` | Tarjan 强连通分量 |

### 八、回溯算法类（backtracking）

| type_id | 算法 |
|---------|------|
| `bt_permutation` | 全排列 |
| `bt_subset` | 子集/组合 |
| `bt_n_queen` | N皇后 |
| `bt_sudoku` | 数独 |
| `bt_maze` | 迷宫求解 |
| `bt_eight_puzzle` | 八数码 |

### 九、字符串算法类（string_algo）

| type_id | 算法 |
|---------|------|
| `str_naive_match` | 朴素模式匹配 |
| `str_kmp` | KMP 算法 |
| `str_hash` | 字符串哈希 |
| `str_ac_automaton` | AC自动机 |
| `str_manacher` | Manacher 回文串 |

### 十、高级专题类（advanced）

| type_id | 算法 |
|---------|------|
| `adv_bidirectional_bfs` | 双向BFS |
| `adv_ids` | 迭代加深搜索 |
| `adv_astar` | A* 启发式搜索 |
| `adv_gcd` | 欧几里得/扩展欧几里得 |
| `adv_prime_sieve` | 素数筛（埃氏筛、线性筛） |
| `adv_fast_pow` | 快速幂 |
| `adv_convex_hull` | 凸包算法 |
| `adv_monte_carlo` | 蒙特卡洛 |
| `adv_matrix` | 矩阵运算/分解 |

### 多标签支持

一个代码可同时命中多个类型，如：

- `quick_sort` → `sorting` + `recursion_divide`
- `dfs` → `graph` + `recursion_divide`
- `huffman_encoding` → `greedy` + `ds_huffman`
- `dp_knapsack_01` → `dp` + 可关联 `greedy_fractional_knapsack` 对比

---

# Stage 3: Pedagogical Planner

## Purpose

自动决定：先讲什么、后讲什么、哪些重点讲、哪些略过。

## User Levels

| Level | 描述 | 教学侧重 |
|-------|------|---------|
| BEGINNER | 初学者 | 多类比、多动画、慢节奏 |
| INTERMEDIATE | 有基础用户 | 适度讲解、重点突破 |
| ADVANCED | 进阶开发者 | 聚焦核心逻辑、略过基础 |
| AUTO | 自动判断 | 根据代码复杂度和用户历史推断 |

## Teaching Strategies

### Concept First（概念先行）
适用于：递归、动态规划、图论、树
```
概念 → 直觉理解 → 执行过程 → 代码实现 → 总结
```

### Execution First（执行先行）
适用于：简单函数、基础代码
```
执行过程 → 代码分析 → 总结
```

### Visualization First（可视化先行）
适用于：排序算法、数据结构
```
动画展示 → 观察规律 → 代码解释 → 总结
```

### Problem First（问题先行）
适用于：算法题
```
问题 → 暴力方案 → 优化思路 → 最终代码 → 复杂度分析
```

### Comparison First（对比先行）
适用于：多算法对比
```
方案A → 方案B → 差异分析 → 总结
```

### State Transition First（状态转移先行）
适用于：动态规划
```
问题定义 → 状态定义 → 状态转移方程 → 填表过程 → 代码实现
```

### Prune First（剪枝先行）
适用于：回溯算法
```
全搜索空间 → 剪枝条件 → 搜索树缩小 → 代码实现
```

### Graph Modeling First（建图先行）
适用于：图论算法
```
问题描述 → 图的建模 → 算法选择 → 执行过程 → 结果
```

## Learning Objective Generator

自动生成学习目标。示例：

> 本视频结束后你将能够：
> ✓ 理解递归概念
> ✓ 理解终止条件
> ✓ 分析简单递归函数
> ✓ 画出调用栈

## Analogy Generator

| 概念 | 类比 |
|------|------|
| 递归 | 镜子中的镜子、俄罗斯套娃 |
| 栈 | 叠盘子、浏览器后退 |
| 队列 | 排队买票、打印队列 |
| 树 | 家谱结构、公司组织架构 |
| 图 | 地铁路线图、社交网络 |
| 哈希表 | 字典目录、快递柜 |
| 动态规划 | 记忆化、填表格 |
| 贪心 | 每次拿最大的、近视眼策略 |
| 回溯 | 走迷宫回头、试错法 |
| 分治 | 把大问题拆成小问题 |
| KMP前缀函数 | 看后视镜找回头路 |
| 最短路径 | 导航找最快捷路线 |
| 最小生成树 | 用最少线缆连通所有城市 |
| 拓扑排序 | 先修课程排序 |
| A*搜索 | 带指南针的探险家 |

## Misconception Detector

| 算法 | 常见误区 | 解决方案 |
|------|---------|---------|
| 递归 | 无限调用 | 增加终止条件讲解动画 |
| 引用传参 | 变量被复制 | 增加内存可视化动画 |
| 快速排序 | 总是O(nlogn) | 展示最坏情况退化动画 |
| 动态规划 | 和贪心混淆 | 对比贪心的反例动画 |
| 哈希冲突 | 认为查找一定是O(1) | 展示冲突链/探测过程 |
| DFS | 栈溢出 | 展示递归深度动画 |
| KMP | next数组难理解 | 逐步构建前缀表动画 |
| Dijkstra | 有负权边时出错 | 展示负权场景的错误结果 |
| 回溯 | 和DP混淆 | 对比同一问题的两种解法 |
| 堆 | 堆≠排序数组 | 展示堆的树形结构和数组的映射 |

---

# Stage 4: Teaching Script Generator

将分析结果转换为教学脚本。

**输出格式：**

```json
[
  {"section": "intro", "narration": "这是一个递归函数"},
  {"section": "concept", "narration": "递归的核心思想是函数调用自身"},
  {"section": "execution", "narration": "让我们看看它是怎么执行的"},
  {"section": "summary", "narration": "总结一下关键点"}
]
```

**要求：** 教学化、自然语言、避免逐行念代码

## Narration Optimizer

优化讲解文案。

| 原始 | 优化 |
|------|------|
| 比较第一个和第二个元素 | 现在我们观察数组中的前两个数字。第一个数字是5，第二个数字是3。因为5大于3，所以它们需要交换位置。 |
| dp[i] = max(dp[i-1], dp[i-2]+nums[i]) | 当前位置的最优解，要么来自不选当前元素的前一个状态，要么来自选当前元素的前两个状态加上当前值，我们取两者中更大的那个。 |
| if s[i] == s[j] and dp[i+1][j-1] | 当两端字符相同，且去掉两端后中间部分也是回文时，整个子串就是回文。注意中间部分的判断在前面已经算好了。 |
| next[i] = next[j] | 前缀函数中，当失配时我们回退到next[j]位置继续匹配，而不是从头开始，这就是KMP的核心优化。 |

---

# Stage 5: Storyboard Generator

生成镜头脚本。

```json
[
  {"scene": "intro", "duration": 5},
  {"scene": "show_array", "duration": 8},
  {"scene": "swap_animation", "duration": 10}
]
```

---

# Scene Library（完整场景库）

## 一、数据结构场景

### Array Scene
- 一维数组：索引高亮、元素交换、双指针移动
- 二维数组/矩阵：行列遍历、对角线、螺旋遍历
- 前缀和：累加过程、区间求值

### LinkedList Scene
- 节点创建：data + next 指针箭头
- 头插法/尾插法：指针变化动画
- 删除节点：指针跳过动画
- 反转链表：三指针翻转过程
- 快慢指针：环检测
- 双链表：prev/next 双向箭头

### Stack Scene
- 入栈/出栈：元素压入弹出
- 括号匹配：栈内状态实时展示
- 表达式求值：操作数栈和运算符栈
- 函数调用栈：递归展开/回溯

### Queue Scene
- 入队/出队：FIFO 动画
- 循环队列：首尾指针移动、取模运算
- 双端队列：两端操作
- 优先队列/堆：按优先级出队

### String Scene
- 字符索引：逐字符扫描
- 子串截取：区间高亮
- 回文检测：两端向中间收缩

### BinaryTree Scene
- 节点创建：左子/右子指针
- 三种遍历：前序/中序/后序递归动画 + 调用栈
- 层序遍历：BFS 队列展示
- 节点插入/删除：指针重连动画

### BST Scene
- 查找路径：比较+左右子树选择
- 插入：沿查找路径到空位
- 删除：叶子/单子/双子三种情况
- 中序遍历有序性验证

### AVLTree Scene
- 平衡因子：节点标注高度差
- 四种旋转：LL/RR/LR/RL 动画
- 旋转前后对比：树高变化

### BTree Scene
- 多路搜索：节点内关键字比较
- 插入+分裂：节点满时向上分裂
- 删除+合并：节点下溢时借用/合并

### HuffmanTree Scene
- 频率统计：字符出现次数
- 优先队列合并：每次取两个最小
- 编码生成：左0右1路径标注
- 编码/解码过程

### Heap Scene
- 堆的数组表示：树 ↔ 数组映射
- sift_up：新元素上浮
- sift_down：堆顶下沉
- 建堆过程：从最后一个非叶节点开始
- 堆排序：取堆顶+调整

### Graph Scene
- 邻接矩阵/邻接表：两种存储可视化
- 加边/删边：矩阵/链表变化
- 有向/无向：箭头方向
- 有权/无权：边标注权重
- 度数：入度出度统计

### HashTable Scene
- 哈希函数计算：key → hash → index
- 链地址法：冲突链表增长
- 开放定址法：线性探测/二次探测
- 装载因子：扩容 rehash

## 二、排序算法场景

### BubbleSort Scene
- 相邻比较+交换动画
- 每轮最大值冒泡到末尾
- 优化：无交换则提前终止
- 颜色标记：已排序区/未排序区/当前比较

### SelectionSort Scene
- 扫描找最小值
- 交换到前面
- 已排序区逐渐增长

### InsertionSort Scene
- 取元素插入已排序区
- 元素后移腾位
- 适合近乎有序的数据

### ShellSort Scene
- 增量序列展示
- 分组插入排序
- 增量缩小直到1
- 对比直接插入排序

### QuickSort Scene
- 选取基准（pivot）
- 分区动画（Lomuto/Hoare）
- 递归左右子数组
- 最坏情况退化动画（已排序数组+首元素pivot）

### MergeSort Scene
- 递归拆分动画
- 合并动画（双指针比较）
- 辅助数组展示
- 分治过程树形图

### HeapSort Scene
- 建堆过程
- 取堆顶+下沉调整
- 已排序区从末尾增长

### RadixSort Scene
- 按位排序：个位→十位→百位
- 桶的分配和收集
- 稳定性展示

### BucketSort Scene
- 区间分桶
- 桶内排序
- 桶间合并

### CountingSort Scene
- 频率统计数组
- 前缀和计算
- 反向填充
- 非比较排序的本质

## 三、查找算法场景

### SequentialSearch Scene
- 逐个比较
- 找到/未找到标记

### BinarySearch Scene
- 有序前提强调
- 左右指针收缩
- 中间值比较
- 变体：左边界/右边界查找
- 搜索区间 [left, right] vs [left, right)

### BlockSearch Scene
- 分块索引表
- 块内查找
- 块间查找

### HashSearch Scene
- 哈希函数映射
- 冲突解决过程
- 查找成功/失败

### BSTSearch Scene
- 比较路径动画
- 查找效率与树高度关系
- 退化成链表的最坏情况

## 四、递归与分治场景

### RecursionBasic Scene
- 递归调用栈展开动画
- 参数传递（值变化）
- 返回值回传动画
- 终止条件触发

### HanoiTower Scene
- 三根柱子可视化
- 盘子移动动画
- 递归分解：n → n-1 + 1 + n-1
- 步骤计数

### BigMultiply Scene
- 大数拆分
- 分治乘法
- 合并结果

### ChessboardCover Scene
- 棋盘网格
- 特殊方格标注
- L型骨牌覆盖过程
- 四象限递归

## 五、动态规划场景

### DPTable Scene（通用）
- 状态定义展示
- DP 表格逐步填充
- 当前单元格的计算来源箭头
- 状态转移方程高亮
- 最优解回溯路径

### Fibonacci Scene
- 递归树 → 重叠子问题 → 记忆化 → DP
- 三种方式对比动画
- 空间优化：滚动变量

### MaxSubarray Scene
- Kadane 算法
- 当前和/最大和双变量追踪
- 负数归零策略

### Knapsack Scene
- 01背包：二维DP表、物品选取回溯
- 完全背包：一维优化、正序遍历
- 多重背包：二进制拆分
- 空间优化：逆序/正序遍历对比

### LIS Scene
- DP 解法：O(n²) 填表
- 贪心+二分：O(nlogn) 维护递增序列

### LCS Scene
- 二维DP表
- 匹配/不匹配三种来源
- 回溯构造LCS

### EditDistance Scene
- 三种操作：插入、删除、替换
- DP表逐步填充
- 操作路径回溯

### MatrixChain Scene
- 区间DP
- 对角线填充顺序
- 最优分割点标注

### StoneMerge Scene
- 区间DP
- 前缀和优化
- 合并代价计算

### PathProblem Scene
- 网格路径
- 障碍物处理
- 最小路径和：DP表 + 路径回溯

## 六、贪心算法场景

### ActivitySelection Scene
- 活动按结束时间排序
- 贪心选择：最早结束
- 兼容性判断
- 对比动态规划解法

### CoinChange Scene
- 贪心选择：最大面值
- 贪心失效的反例（如面值 [1,3,4]，目标6）
- 对比DP正确解法

### HuffmanEncoding Scene
- 频率统计
- 优先队列建树
- 编码表生成
- 编码/解码演示
- 与等长编码对比压缩率

### IntervalScene
- 区间排序策略
- 选点/覆盖过程动画
- 贪心正确性直观证明

### FractionalKnapsack Scene
- 单位价值排序
- 部分装入
- 对比01背包（不可分割）

## 七、图论算法场景

### DFS Scene
- 递归调用栈展示
- 访问标记变色
- 回溯过程
- 生成树/森林
- 应用：连通分量、环检测

### BFS Scene
- 队列状态实时展示
- 层次遍历动画
- 最短路径（无权图）
- 生成树

### Dijkstra Scene
- 距离表更新过程
- 已确定/未确定节点标记
- 松弛操作动画
- 贪心选择：当前最短
- 负权边失效演示

### BellmanFord Scene
- 每轮对所有边松弛
- 距离表逐步收敛
- 第n轮仍可松弛 → 负环检测
- 与Dijkstra对比

### SPFA Scene
- 队列优化
- 入队/出队过程
- 负环检测

### Floyd Scene
- 三重循环动画
- 中间节点k的枚举
- 距离矩阵逐步更新
- 任意两点最短路径

### Prim Scene
- 从起点扩展
- 切割边集
- 每次选最短横切边
- 生成树逐步生长

### Kruskal Scene
- 边排序
- 并查集：查找+合并
- 环检测：连通性判断
- 生成树逐步构建

### TopologicalSort Scene
- 入度表
- 入度为0入队
- 删除节点+更新入度
- 环检测：未处理节点存在

### CriticalPath Scene
- AOE网展示
- 事件最早/最晚时间
- 活动时间计算
- 关键路径标注
- 关键活动识别

### Hungarian Scene
- 二分图展示
- 增广路径搜索
- 匹配/未匹配边交替
- 匹配数增长

### Tarjan Scene
- DFS序号标注
- low值更新
- 栈的使用
- 强连通分量识别

## 八、回溯算法场景

### BacktrackFramework Scene（通用框架）
- 解空间树展示
- 选择→递归→撤销 选择过程
- 剪枝条件触发动画
- 有效解收集

### Permutation Scene
- 决策树逐层展开
- used数组追踪
- 叶节点即为一个排列

### SubsetScene
- 选/不选二叉决策树
- 递归路径展示

### NQueen Scene
- 棋盘可视化
- 逐行放置
- 列/对角线冲突检测
- 回溯撤销
- 解的数量

### Sudoku Scene
- 9×9网格
- 约束传播
- 试填+回溯
- 唯一解验证

### Maze Scene
- 网格迷宫
- 四方向探索
- 死胡同回溯
- 路径标记

### EightPuzzle Scene
- 3×3数字板
- 空格移动
- 状态空间搜索
- 曼哈顿距离启发

## 九、字符串算法场景

### NaiveMatch Scene
- 模式串逐位滑动
- 字符比较
- 失配后整体右移一位
- 重复比较展示（低效原因）

### KMP Scene
- 前缀函数/next数组逐步构建
- 匹配过程：失配后跳转
- 不回溯主串指针
- 对比朴素匹配的效率

### StringHash Scene
- 滚动哈希计算
- 哈希冲突概率
- 子串哈希O(1)查询
- Rabin-Karp 匹配

### ACAutomaton Scene
- Trie树构建
- 失配指针（fail指针）
- 多模式匹配过程
- 同时匹配多个模式串

### Manacher Scene
- 回文半径数组
- 中心扩展
- 利用已知回文加速
- 最长回文子串

## 十、高级专题场景

### BidirectionalBFS Scene
- 两端同时扩展
- 交汇点检测
- 搜索空间对比单向BFS

### IDSScene
- 深度限制递增
- 同一搜索树反复遍历
- 空间复杂度优势

### AStarScene
- 启发函数展示
- f = g + h 计算
- 优先队列选择
- 与BFS/DFS路径对比
- 启发函数可纳性

### GCDScene
- 辗转相除过程
- 余数变化
- 扩展欧几里得：逆元求解

### PrimeSieve Scene
- 埃氏筛：标记合数
- 线性筛：每个合数只被最小质因子筛
- 对比两种方法效率

### FastPow Scene
- 二进制拆分指数
- 逐步平方
- 取模运算
- O(logn) 次乘法

### ConvexHull Scene
- 点集展示
- Graham扫描/Andrew算法
- 叉积判断方向
- 凸包逐步构建

### MonteCarlo Scene
- 随机采样可视化（如圆周率估算）
- 收敛过程
- 误差分析

### MatrixScene
- 矩阵乘法：行列点积
- 矩阵快速幂
- 特征值/特征向量几何意义

---

# Variable Tracking System

实时追踪变量变化。

```json
{"i": 0, "j": 1, "temp": 5}
```

动画展示：
```
i: 0 → 1
j: 1 → 2
```

## 特殊追踪模式

### DP表追踪
- 当前填充单元格高亮
- 来源单元格箭头标注
- 值变化实时更新

### 图遍历追踪
- 当前节点高亮
- 已访问/未访问/正在访问三色标记
- 边的遍历顺序

### 递归调用栈追踪
- 栈帧入栈/出栈
- 每帧局部变量
- 返回值传播

### 指针追踪
- 指针所指位置箭头
- 指针移动动画
- 多指针同步追踪（快慢指针、双指针）

---

# Code Highlighting

类似 VSCode Debugger：

| 类型 | 颜色 | 含义 |
|------|------|------|
| CURRENT_LINE | 黄色 | 当前执行行 |
| EXECUTED_LINE | 绿色 | 已执行行 |
| INACTIVE_LINE | 灰色 | 未执行行 |
| MODIFIED_VAR | 橙色 | 值发生变化的变量 |
| CONDITION_TRUE | 蓝色 | 条件为真 |
| CONDITION_FALSE | 红色 | 条件为假 |

---

# Camera Planner

```python
camera_actions = ["zoom_in", "zoom_out", "focus", "pan", "follow"]
```

| 场景 | 摄像机动作 |
|------|-----------|
| 递归展开 | zoom_in（逐层深入） |
| 递归返回 | zoom_out（逐层回退） |
| 数组交换 | focus（聚焦交换区域） |
| 图遍历 | follow（跟随当前节点） |
| DP填表 | pan（从左到右/从上到下扫视） |
| 调用栈 | zoom_in（栈增长）→ zoom_out（栈收缩） |
| 排序整体 | zoom_out（看全局趋势） |
| 排序细节 | zoom_in（看当前比较） |

---

# Example Selection Engine

自动生成教学示例，原则：数据量小、变化明显、易于动画展示。

| 算法 | 自动选择示例 |
|------|------------|
| 冒泡排序 | [5, 3, 8, 2, 1] |
| 快速排序 | [7, 2, 5, 1, 8, 3, 6] |
| 归并排序 | [6, 3, 8, 2, 5, 1, 7, 4] |
| 二分查找 | arr=[1,3,5,7,9,11], target=7 |
| 汉诺塔 | n=3（刚好可视化） |
| 01背包 | weights=[2,3,4,5], values=[3,4,5,6], W=8 |
| LCS | "ABCDGH", "AEDFHR" |
| Dijkstra | 5节点6边的小图 |
| N皇后 | n=4（比n=8更适合教学） |
| KMP | text="ABABDABACDABABC", pattern="ABABC" |
| 斐波那契 | n=6（递归树可展开但不过大） |

---

# Audio-Driven Pipeline（音频驱动管线）

## 核心思想

**先生成语音，再驱动动画。** 传统做法是先做动画再配音，动画节奏和语音难以对齐。本管线反过来：先逐段生成 TTS 语音，获取每段实际时长，再用这些时长控制 Manim 动画的 `self.wait()` 和 `run_time`，确保音画帧级同步。

## 管线总览

```
教学脚本（narration_segments）
        │
        ▼
┌─────────────────────┐
│  Stage A: TTS 生成   │  edge-tts 逐段生成语音 → narration.mp3 + segment_durations.json
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│  Stage B: 字幕生成   │  根据 segment_durations.json → subtitle.srt
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│  Stage C: 时间轴规划 │  segment_durations.json → timeline.json（每段动画的精确时间窗口）
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│  Stage D: 动画渲染   │  Manim 读取 timeline.json 控制 wait/run_time → video_only.mp4
└─────────────────────┘
        │
        ▼
┌─────────────────────┐
│  Stage E: 合成输出   │  ffmpeg 合并 video_only.mp4 + narration.mp3 + subtitle.srt → final.mp4
└─────────────────────┘
```

## 输入格式：教学脚本

```json
{
  "title": "Prim算法 — 核心更新步骤",
  "voice": "zh-CN-YunxiNeural",
  "segments": [
    {
      "id": "seg_01",
      "section": "intro",
      "narration": "这是Prim最小生成树算法的核心更新步骤。当一个新的顶点u被加入已选集合后，我们需要更新剩余所有未访问顶点到已选集合的最短距离。",
      "animation_hint": "show_graph_highlight_u"
    },
    {
      "id": "seg_02",
      "section": "step1",
      "narration": "第一步，标记顶点u为已访问。将visited数组的对应位置设为1，表示这个顶点已经加入了最小生成树。",
      "animation_hint": "mark_visited_u"
    },
    {
      "id": "seg_03",
      "section": "step2_loop",
      "narration": "第二步，遍历所有未访问的顶点v。对每个顶点，检查从u到v的边权是否比当前记录的lowcost值更小。如果更小，就更新lowcost。",
      "animation_hint": "loop_over_vertices"
    },
    {
      "id": "seg_04",
      "section": "example_v2",
      "narration": "看顶点2，从u到2的边权是3，而当前lowcost[2]是无穷大，3小于无穷大，所以更新lowcost[2]为3。",
      "animation_hint": "update_v2"
    },
    {
      "id": "seg_05",
      "section": "example_v3",
      "narration": "再看顶点3，从u到3的边权是8，但当前lowcost[3]已经是6了，8不小于6，所以不更新。",
      "animation_hint": "skip_v3"
    },
    {
      "id": "seg_06",
      "section": "example_v4",
      "narration": "最后看顶点4，边权是5，而当前lowcost[4]是无穷大，5小于无穷大，更新lowcost[4]为5。",
      "animation_hint": "update_v4"
    },
    {
      "id": "seg_07",
      "section": "summary",
      "narration": "这就是Prim算法的核心：每次新加入一个顶点，就用它到未访问顶点的边来尝试更新最短距离，保证始终选择最短的横切边加入生成树。",
      "animation_hint": "show_summary"
    }
  ]
}
```

**关键字段说明：**
- `narration`：语音讲解文案，会直接送给TTS，必须自然流畅、教学化
- `animation_hint`：给Manim渲染器的提示，标识这段语音对应哪段动画
- `section`：教学阶段标记，用于教学策略匹配

---

## Stage A: TTS 生成（tts_generator.py）

使用 `edge-tts` 库生成语音，同时获取每段的精确时长。

```python
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
```

**依赖安装：** `pip install edge-tts`

### TTS Voices

| 场景 | voice参数 | 特点 |
|------|----------|------|
| 默认 | `zh-CN-YunxiNeural` | 男声，清晰自然，适合技术讲解 |
| 正式讲解 | `zh-CN-YunjianNeural` | 男声，沉稳有力 |
| 轻松教学 | `zh-CN-XiaoxiaoNeural` | 女声，亲切活泼 |
| 快速讲解 | `zh-CN-XiaoyiNeural` | 女声，语速偏快 |
| 温柔教学 | `zh-CN-XiaohanNeural` | 女声，温柔舒缓 |

### 语速控制

edge-tts 支持 rate 参数调节语速：

```python
communicate = edge_tts.Communicate(text, voice, rate="+20%")  # 加速20%
communicate = edge_tts.Communicate(text, voice, rate="-10%")  # 减速10%
```

推荐：
- 复杂推导过程：`rate="-5%"` 稍慢
- 概念总结/回顾：`rate="+10%"` 稍快
- 代码逐行讲解：默认语速

---

## Stage B: 字幕生成（subtitle_generator.py）

根据 `segment_durations.json` 生成 SRT 字幕文件。

```python
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
    generate_srt(sys.argv[1], sys.argv[2])
```

---

## Stage C: 时间轴规划（timeline_planner.py）

将语音时长转换为 Manim 动画控制参数。

```python
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
```

---

## Stage D: 动画渲染（Manim 集成模式）

### 方式一：音频驱动渲染（推荐）

Manim 场景读取 `timeline.json`，用每段的 `manim_wait` 控制 `self.wait()` 时长，确保动画节奏与语音完全同步。

```python
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
```

**使用示例（Prim算法）：**

```python
class PrimWithNarration(AudioDrivenScene):
    def construct(self):
        # 第1段：介绍
        self.play(Write(title), FadeIn(graph))
        self.wait_for_narration("seg_01")  # 自动等待语音播完

        # 第2段：标记已访问
        self.play(vertex_circles[u].animate.set_fill(GREEN, opacity=0.3))
        self.wait_for_narration("seg_02")

        # 第3段：遍历说明
        self.play(Write(loop_label))
        self.wait_for_narration("seg_03")

        # 第4段：更新v=2
        self.play(edge_lines[2].animate.set_color(YELLOW))
        self.play(FadeOut(old_val), FadeIn(new_val))
        self.wait_for_narration("seg_04")

        # ... 后续段
```

### 方式二：后处理对齐（备选）

如果不想修改Manim场景代码，也可以：
1. 先渲染纯动画视频（固定节奏）
2. 用 ffmpeg 的 `atempo` 调整语速来适配动画节奏

```bash
# 语速调整范围 0.5x ~ 2.0x
ffmpeg -i narration.mp3 -filter:a "atempo=1.1" adjusted_narration.mp3
```

> **推荐方式一**，音频驱动渲染才能真正实现帧级音画同步。

---

## Stage E: 合成输出（video_composer.py）

用 ffmpeg 合并无声动画、语音和字幕为最终教学视频。

```python
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
```

### 字幕样式说明

ffmpeg `subtitles` filter 的 `force_style` 参数：

| 参数 | 值 | 说明 |
|------|---|------|
| FontName | WenQuanYi Zen Hei | 中文字体 |
| FontSize | 18 | 字号（视频1080p时推荐18-22） |
| PrimaryColour | &H00FFFFFF | 白色（AABBGGRR格式） |
| OutlineColour | &H00000000 | 黑色描边 |
| Outline | 2 | 描边粗细 |
| MarginV | 30 | 底部边距 |
| Alignment | 2 | 底部居中（默认） |

---

## Pipeline 主控脚本（pipeline.py）

将五个 Stage 串联为一键执行的完整管线。

```python
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
```

---

## 快速使用流程

### 1. 准备教学脚本

按上面的输入格式编写 JSON 文件，包含每段 narration 和 animation_hint。

### 2. 编写 Manim 场景

继承 `AudioDrivenScene`，用 `self.wait_for_narration(segment_id)` 替代 `self.wait()`。

### 3. 一键运行

```bash
pip install edge-tts manim ffmpeg
python pipeline.py teaching_script.json scene.py SceneName
```

### 4. 输出文件

```
output/
├── final.mp4              ← 最终教学视频（带语音+字幕）
├── subtitle.srt           ← SRT字幕
├── audio/
│   ├── narration.mp3      ← 完整语音
│   ├── seg_01.mp3         ← 各段语音
│   ├── segment_durations.json  ← 语音时长数据
│   └── timeline.json      ← 动画时间轴
└── video/
    └── media.mp4          ← 无声动画
```

---

## 音画同步校验清单

生成视频后，按以下标准校验音画同步质量：

| 检查项 | 标准 | 修复方式 |
|--------|------|---------|
| 动画是否在语音前0.1-0.2秒启动 | 视觉先行，用户看到变化时语音才解释 | 调整 `lead_in` 参数 |
| 语音段间是否有自然停顿 | 0.3-0.5秒间隔，避免太赶 | 调整 `min_gap` 参数 |
| 字幕是否与语音同步 | 偏差<0.3秒 | 检查 `segment_durations.json` |
| 字幕行是否过长 | 每行不超过24个中文字 | 调整 `max_chars_per_line` |
| 动画是否等语音播完才切下一段 | 不能语音还在播动画已经跳走 | 检查 `manim_wait` 与 `audio_duration` 的比例 |
| 语音速率是否舒适 | 关键步骤稍慢，总结稍快 | 调整 TTS 的 `rate` 参数 |

---

# Algorithm Code Library（算法代码库）

以下是各算法的参考实现、教学重点与可视化要求，供代码分析器匹配和教学规划器使用。

## 一、数据结构

### 1.1 链表反转

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # 暂存下一个
        curr.next = prev       # 反转指针
        prev = curr            # prev前进
        curr = next_node       # curr前进
    return prev
```

**教学重点：** 三指针（prev/curr/next）协同移动，指针方向反转是核心
**可视化：** 三个指针箭头动画、节点next指针断开重连
**常见误区：** 忘记暂存next_node导致链表断裂

### 1.2 栈实现括号匹配

```python
def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack
```

**教学重点：** LIFO特性与括号嵌套的天然对应
**可视化：** 栈的入栈出栈动画、匹配/不匹配标记
**常见误区：** 忽略栈空时的右括号、最终栈非空

### 1.3 二叉树三种遍历

```python
def preorder(root):
    if not root:
        return
    print(root.val)       # 先访问根
    preorder(root.left)   # 再左子树
    preorder(root.right)  # 再右子树

def inorder(root):
    if not root:
        return
    inorder(root.left)    # 先左子树
    print(root.val)       # 再访问根
    inorder(root.right)   # 再右子树

def postorder(root):
    if not root:
        return
    postorder(root.left)  # 先左子树
    postorder(root.right) # 再右子树
    print(root.val)       # 最后访问根
```

**教学重点：** 递归序中访问根的时机决定遍历类型
**可视化：** 树上路径动画 + 调用栈展开 + 节点访问顺序编号
**常见误区：** 三种遍历的输出混淆

### 1.4 AVL树旋转

```python
def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def left_rotate(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))
    return y
```

**教学重点：** 平衡因子计算、四种失衡类型对应四种旋转
**可视化：** 树结构变化动画、高度标注更新、旋转前后对比
**常见误区：** LR/RL型需要两次旋转

### 1.5 哈希表（链地址法）

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None
```

**教学重点：** 哈希函数、冲突原因、链地址法解决冲突
**可视化：** key→hash→index映射动画、冲突链增长
**常见误区：** 认为查找一定是O(1)

## 二、排序算法

### 2.1 冒泡排序

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
```

**教学重点：** 相邻比较交换、每轮最大值冒泡、优化：无交换提前终止
**可视化：** 柱状图比较+交换、已排序区着色、swapped标志
**复杂度：** 最好O(n)，最坏O(n²)，稳定

### 2.2 快速排序

```python
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

**教学重点：** 分治思想、pivot选择、Lomuto分区法、最坏情况退化
**可视化：** pivot高亮、分区过程、递归树、已排序区标注
**常见误区：** 已排序数组+首元素pivot导致O(n²)

### 2.3 归并排序

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

**教学重点：** 分治拆分+有序合并、辅助数组、稳定排序
**可视化：** 递归拆分树、双指针合并动画
**复杂度：** O(nlogn)稳定，空间O(n)

### 2.4 堆排序

```python
def heap_sort(arr):
    n = len(arr)
    # 建堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # 逐个取堆顶
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

**教学重点：** 完全二叉树↔数组映射、sift_down、建堆从n/2开始
**可视化：** 树形结构与数组同步展示、sift_down路径
**常见误区：** 建堆从最后一个节点开始（应从最后一个非叶节点）

## 三、查找算法

### 3.1 二分查找

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**教学重点：** 有序前提、搜索区间 [left, right]、防溢出写法 mid=left+(right-left)//2
**可视化：** 数组上左右指针收缩、mid位置高亮、区间缩小
**常见误区：** 循环条件 <= vs <、边界更新 +1/-1

### 3.2 二分查找左边界

```python
def binary_search_left(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```

**教学重点：** 搜索左闭右开区间 [left, right)、找到不立即返回
**可视化：** 与标准二分对比动画

## 四、递归与分治

### 4.1 汉诺塔

```python
def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, source, target)
```

**教学重点：** 递归分解 n→n-1+1+n-1、三步递归关系
**可视化：** 三柱盘子动画、递归树展开、步骤计数器
**复杂度：** 时间O(2^n)、空间O(n)

### 4.2 棋盘覆盖

```python
def chessboard_cover(board, size, top_row, top_col, special_row, special_col, tile=[0]):
    if size == 1:
        return
    tile[0] += 1
    current_tile = tile[0]
    half = size // 2
    # 四个象限分别处理
    for i, (sr, sc) in enumerate([(top_row, top_col),
                                   (top_row, top_col + half),
                                   (top_row + half, top_col),
                                   (top_row + half, top_col + half)]):
        if not (sr <= special_row < sr + half and sc <= special_col < sc + half):
            # 该象限无特殊方格，在靠近中心的角放置L型骨牌的一格
            board[sr + (1 if i >= 2 else 0)][sc + (1 if i % 2 == 1 else 0)] = current_tile
    # 递归四个象限
    chessboard_cover(board, half, top_row, top_col, special_row if special_row < top_row + half else top_row + half - 1, special_col if special_col < top_col + half else top_col + half - 1, tile)
    # ... 类似处理其余三个象限
```

**教学重点：** 分治策略、L型骨牌放置、特殊方格传播
**可视化：** 棋盘网格、骨牌颜色填充、四象限递归

## 五、动态规划

### 5.1 01背包

```python
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]  # 不选第i个
            if w >= weights[i - 1]:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
    return dp[n][capacity]
```

**教学重点：** 状态定义 dp[i][w]：前i个物品容量w的最大价值、选/不选决策
**可视化：** 二维DP表逐行填充、来源箭头、物品选取回溯
**常见误区：** 一维优化时遍历顺序必须逆序

### 5.2 完全背包

```python
def knapsack_complete(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for w in range(capacity + 1):
        for i in range(len(weights)):
            if w >= weights[i]:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]
```

**教学重点：** 与01背包区别：每个物品可重复选、正序遍历
**可视化：** 一维DP表填充、正序vs逆序对比动画

### 5.3 最长公共子序列

```python
def lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
```

**教学重点：** 字符匹配+1/不匹配取max、回溯构造LCS
**可视化：** DP表 + 字符串对齐动画 + 回溯路径

### 5.4 最长上升子序列

```python
def lis_dp(nums):
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

def lis_binary(nums):
    tails = []
    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)
```

**教学重点：** O(n²) DP解法 vs O(nlogn) 贪心+二分解法
**可视化：** DP解法填表、二分解法维护tails数组

### 5.5 编辑距离

```python
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1): dp[i][0] = i
    for j in range(n + 1): dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]
```

**教学重点：** 三种操作（插入、删除、替换）对应三个来源
**可视化：** DP表 + 操作类型标注 + 回溯操作序列

### 5.6 矩阵连乘

```python
def matrix_chain(p):
    n = len(p) - 1
    dp = [[0] * n for _ in range(n)]
    split = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):  # 链长
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k
    return dp[0][n - 1]
```

**教学重点：** 区间DP、对角线填充顺序、最优分割点
**可视化：** 三角形DP表对角线填充、括号化方案

### 5.7 最大子数组和

```python
def max_subarray(nums):
    max_sum = curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum
```

**教学重点：** Kadane算法、当前和为负则重新开始
**可视化：** 数组上区间标记、curr_sum和max_sum双线追踪

### 5.8 路径问题

```python
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for j in range(1, n): dp[0][j] = dp[0][j-1] + grid[0][j]
    for i in range(1, m): dp[i][0] = dp[i-1][0] + grid[i][0]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    return dp[m-1][n-1]
```

**教学重点：** 网格DP、边界初始化、来源只有上/左
**可视化：** 网格 + DP值填充 + 最优路径回溯

## 六、贪心算法

### 6.1 活动选择

```python
def activity_selection(starts, ends):
    activities = sorted(zip(starts, ends), key=lambda x: x[1])
    selected = [activities[0]]
    last_end = activities[0][1]
    for start, end in activities[1:]:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected
```

**教学重点：** 按结束时间排序、贪心选择最早结束
**可视化：** 时间轴上活动条、选择/不选择标记

### 6.2 哈夫曼编码

```python
import heapq

def huffman_codes(freq):
    heap = [[f, [char, ""]] for char, f in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]: pair[1] = '0' + pair[1]
        for pair in hi[1:]: pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: p[0])
```

**教学重点：** 贪心+优先队列、每次取两个最小频率、左0右1编码
**可视化：** 频率表→优先队列→树构建→编码表

### 6.3 分数背包

```python
def fractional_knapsack(weights, values, capacity):
    items = sorted(zip(weights, values), key=lambda x: x[1]/x[0], reverse=True)
    total_value = 0
    for w, v in items:
        if capacity >= w:
            total_value += v
            capacity -= w
        else:
            total_value += v * (capacity / w)
            break
    return total_value
```

**教学重点：** 按单位价值排序、可部分装入（与01背包区别）
**可视化：** 单位价值排序→依次装入→部分装入动画

### 6.4 区间选点

```python
def interval_points(intervals):
    intervals.sort(key=lambda x: x[1])
    points = []
    last_point = float('-inf')
    for start, end in intervals:
        if start > last_point:
            points.append(end)
            last_point = end
    return points
```

**教学重点：** 按右端点排序、贪心选择最右端
**可视化：** 数轴上区间和选点

## 七、图论算法

### 7.1 DFS

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
```

**教学重点：** 递归+标记、回溯、连通分量
**可视化：** 图上节点变色、递归调用栈、生成树边标注

### 7.2 BFS

```python
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

**教学重点：** 队列+标记、层次遍历、最短路径（无权）
**可视化：** 队列状态展示、层次波浪扩散动画

### 7.3 Dijkstra

```python
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, node = heapq.heappop(heap)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist[node] + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return dist
```

**教学重点：** 贪心+优先队列、松弛操作、不能处理负权边
**可视化：** 距离表更新、已确定节点标记、松弛动画

### 7.4 Bellman-Ford

```python
def bellman_ford(edges, n, start):
    dist = [float('inf')] * n
    dist[start] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    # 检测负环
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            return None  # 存在负环
    return dist
```

**教学重点：** 对所有边松弛n-1轮、负环检测
**可视化：** 每轮松弛后距离表变化、第n轮仍可松弛→负环

### 7.5 Floyd-Warshall

```python
def floyd(n, edges):
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n): dist[i][i] = 0
    for u, v, w in edges: dist[u][v] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
```

**教学重点：** 中间节点枚举、多源最短路、动态规划思想
**可视化：** 距离矩阵逐步更新、当前k对应的中转路径高亮

### 7.6 Prim

```python
def prim(graph, start):
    visited = {start}
    edges = [(w, start, v) for v, w in graph[start]]
    heapq.heapify(edges)
    mst = []
    while edges:
        w, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, w))
            for next_v, next_w in graph[v]:
                if next_v not in visited:
                    heapq.heappush(edges, (next_w, v, next_v))
    return mst
```

**教学重点：** 从一个点扩展、每次选最短横切边
**可视化：** 生成树逐步生长、横切边集展示

### 7.7 Kruskal

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py: self.parent[px] = py; return True
        return False

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    for u, v, w in edges:
        if uf.union(u, v):
            mst.append((u, v, w))
            if len(mst) == n - 1: break
    return mst
```

**教学重点：** 边排序+并查集、环检测通过连通性判断
**可视化：** 边按权重排序、并查集合并动画、MST构建

### 7.8 拓扑排序

```python
def topological_sort(graph, n):
    in_degree = [0] * n
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for v in graph[node]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    return result if len(result) == n else None  # None表示有环
```

**教学重点：** 入度统计、BFS入度为0入队、环检测
**可视化：** 入度表实时更新、节点出队/入队动画

### 7.9 关键路径（AOE网）

```python
def critical_path(graph, n):
    # 正向求最早开始时间
    topo = topological_sort(graph, n)
    ve = [0] * n
    for u in topo:
        for v, w in graph[u]:
            ve[v] = max(ve[v], ve[u] + w)
    # 反向求最晚开始时间
    vl = [ve[-1]] * n
    for u in reversed(topo):
        for v, w in graph[u]:
            vl[u] = min(vl[u], vl[v] - w)
    # 关键活动：e == l
    critical = []
    for u in range(n):
        for v, w in graph[u]:
            if ve[u] == vl[v] - w:
                critical.append((u, v))
    return critical
```

**教学重点：** 正向推ve、反向推vl、关键活动判断
**可视化：** AOE网、ve/vl标注、关键路径高亮

### 7.10 匈牙利算法

```python
def hungarian(graph, n_left, n_right):
    match_right = [-1] * n_right

    def dfs(u, visited):
        for v in range(n_right):
            if graph[u][v] and v not in visited:
                visited.add(v)
                if match_right[v] == -1 or dfs(match_right[v], visited):
                    match_right[v] = u
                    return True
        return False

    result = 0
    for u in range(n_left):
        visited = set()
        if dfs(u, visited):
            result += 1
    return result
```

**教学重点：** 增广路径、交替路、匹配数递增
**可视化：** 二分图、匹配/未匹配边交替、增广路径搜索

## 八、回溯算法

### 8.1 回溯框架

```python
def backtrack(path, choices):
    if satisfy_end_condition(path):
        result.append(path[:])
        return
    for choice in choices:
        if is_valid(choice):
            make_choice(choice)      # 选择
            backtrack(path, choices) # 递归
            undo_choice(choice)      # 撤销选择
```

**教学重点：** 选择→递归→撤销、解空间树、剪枝
**可视化：** 决策树展开/回退动画、剪枝标记

### 8.2 N皇后

```python
def solve_n_queens(n):
    result = []
    def backtrack(row, cols, diag1, diag2, board):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if col in cols or row - col in diag1 or row + col in diag2:
                continue
            cols.add(col); diag1.add(row - col); diag2.add(row + col)
            board.append('.' * col + 'Q' + '.' * (n - col - 1))
            backtrack(row + 1, cols, diag1, diag2, board)
            board.pop(); cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)
    backtrack(0, set(), set(), set(), [])
    return result
```

**教学重点：** 逐行放置、列/对角线冲突检测集合
**可视化：** 棋盘+皇后放置/移除动画、冲突线高亮

### 8.3 全排列

```python
def permute(nums):
    result = []
    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path, used)
            path.pop()
            used[i] = False
    backtrack([], [False] * len(nums))
    return result
```

**教学重点：** used数组标记、决策树层级=排列位置
**可视化：** 决策树展开、used数组状态、路径追踪

### 8.4 子集

```python
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return result
```

**教学重点：** 选/不选二叉决策、start控制不重复
**可视化：** 二叉决策树、当前子集展示

## 九、字符串算法

### 9.1 KMP

```python
def compute_next(pattern):
    n = len(pattern)
    next_arr = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and pattern[i] != pattern[j]:
            j = next_arr[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        next_arr[i] = j
    return next_arr

def kmp_search(text, pattern):
    next_arr = compute_next(pattern)
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = next_arr[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            return i - j + 1
    return -1
```

**教学重点：** 前缀函数/next数组含义、失配不回退主串指针
**可视化：** next数组逐步构建动画、匹配+跳转过程、与朴素匹配对比

### 9.2 字符串哈希

```python
class StringHash:
    def __init__(self, s, base=131, mod=2**64):
        n = len(s)
        self.hash = [0] * (n + 1)
        self.power = [1] * (n + 1)
        for i in range(n):
            self.hash[i + 1] = (self.hash[i] * base + ord(s[i])) % mod
            self.power[i + 1] = (self.power[i] * base) % mod

    def get_hash(self, l, r):  # [l, r)
        return (self.hash[r] - self.hash[l] * self.power[r - l]) % mod
```

**教学重点：** 多项式哈希、滚动哈希O(1)子串查询
**可视化：** 哈希值计算过程、子串哈希提取

## 十、高级专题

### 10.1 A*搜索

```python
def astar(grid, start, end):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = [(heuristic(start, end), 0, start)]
    g_score = {start: 0}
    came_from = {}

    while open_set:
        f, g, current = heapq.heappop(open_set)
        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            neighbor = (current[0]+dx, current[1]+dy)
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                tentative_g = g + 1
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    came_from[neighbor] = current
                    heapq.heappush(open_set, (tentative_g + heuristic(neighbor, end), tentative_g, neighbor))
```

**教学重点：** f=g+h、启发函数设计、可纳性
**可视化：** f值标注、搜索过程、与BFS路径对比

### 10.2 欧几里得算法

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1
```

**教学重点：** 辗转相除、扩展欧几里得求逆元
**可视化：** 余数变化过程、贝祖等式验证

### 10.3 素数筛

```python
def eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

def linear_sieve(n):
    is_prime = [True] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
        for p in primes:
            if i * p > n: break
            is_prime[i * p] = False
            if i % p == 0: break
    return primes
```

**教学重点：** 埃氏筛标记合数、线性筛每个合数只被最小质因子筛
**可视化：** 数轴上标记过程、两种方法效率对比

### 10.4 快速幂

```python
def fast_pow(base, exp, mod=None):
    result = 1
    while exp > 0:
        if exp & 1:
            result = result * base
            if mod: result %= mod
        base = base * base
        if mod: base %= mod
        exp >>= 1
    return result
```

**教学重点：** 二进制拆分指数、逐步平方、O(logn)
**可视化：** 指数二进制拆分、每步平方值变化

### 10.5 凸包

```python
def convex_hull(points):
    points = sorted(points)
    if len(points) <= 1:
        return points
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
```

**教学重点：** 叉积判断方向、Andrew算法上下凸包
**可视化：** 点集→排序→上下凸包构建→合并

---

# Rendering Pipeline

## 完整流程（含音频驱动）

```
用户代码
   │
   ├─→ Stage 1: Code Analyzer（代码结构分析）
   ├─→ Stage 2: Code Type Classifier（代码类型分类）
   ├─→ Stage 3: Pedagogical Planner（教学规划）
   └─→ Stage 4: Teaching Script Generator（教学脚本生成）
         │
         ▼
   teaching_script.json（含 narration segments）
         │
         ├─→ Stage A: TTS Generator → narration.mp3 + segment_durations.json
         ├─→ Stage B: Subtitle Generator → subtitle.srt
         ├─→ Stage C: Timeline Planner → timeline.json
         ├─→ Stage D: Manim Renderer（读取 timeline.json 驱动动画节奏）→ video_only.mp4
         └─→ Stage E: Video Composer（ffmpeg 合并）→ final.mp4
```

## 纯动画模式（无需语音）

如果只需要无声动画，跳过 Stage A-C，直接写 Manim 场景渲染：

```bash
manim -ql scene.py SceneName
```

## 一键完整渲染

```bash
python pipeline.py teaching_script.json scene.py SceneName
```

---

# Output Files

| 文件 | 说明 |
|------|------|
| final.mp4 | 最终教学视频 |
| subtitle.srt | 字幕文件 |
| video_only.mp4 | 无声动画 |
| narration.mp3 | 讲解音频 |
| timeline.json | 时间轴 |
| storyboard.json | 镜头脚本 |
| analysis.json | 代码分析结果 |
| lesson_plan.json | 教学规划结果 |

---

# Directory Structure

```
code-teaching-video-agent/
├── SKILL.md
├── scripts/
│   ├── pipeline.py              # 主控脚本：一键执行完整管线
│   ├── code_analyzer.py         # Stage 1: 代码结构分析
│   ├── classifier.py            # Stage 2: 代码类型分类
│   ├── pedagogical_planner.py   # Stage 3: 教学规划
│   ├── script_generator.py      # Stage 4: 教学脚本生成
│   ├── storyboard_generator.py  # Stage 5: 分镜生成
│   ├── tts_generator.py         # Stage A: TTS语音生成（edge-tts）
│   ├── subtitle_generator.py    # Stage B: SRT字幕生成
│   ├── timeline_planner.py      # Stage C: 时间轴规划
│   ├── narration_optimizer.py   # 讲解文案优化
│   ├── manim_renderer.py        # Stage D: Manim动画渲染
│   ├── video_composer.py        # Stage E: ffmpeg音视频合成
│   └── audio_driven_scene.py    # AudioDrivenScene基类（Manim用）
├── templates/
│   ├── sorting/
│   │   ├── bubble.py
│   │   ├── selection.py
│   │   ├── insertion.py
│   │   ├── shell.py
│   │   ├── quick.py
│   │   ├── merge.py
│   │   ├── heap.py
│   │   ├── radix.py
│   │   ├── bucket.py
│   │   └── counting.py
│   ├── searching/
│   │   ├── sequential.py
│   │   ├── binary.py
│   │   ├── block.py
│   │   ├── hash.py
│   │   └── bst.py
│   ├── recursion/
│   │   ├── basic.py
│   │   ├── hanoi.py
│   │   ├── big_multiply.py
│   │   └── chessboard.py
│   ├── dp/
│   │   ├── fibonacci.py
│   │   ├── max_subarray.py
│   │   ├── knapsack_01.py
│   │   ├── knapsack_complete.py
│   │   ├── lis.py
│   │   ├── lcs.py
│   │   ├── edit_distance.py
│   │   ├── matrix_chain.py
│   │   ├── stone_merge.py
│   │   └── path.py
│   ├── greedy/
│   │   ├── activity.py
│   │   ├── coin.py
│   │   ├── huffman.py
│   │   ├── interval.py
│   │   └── fractional_knapsack.py
│   ├── graph/
│   │   ├── dfs.py
│   │   ├── bfs.py
│   │   ├── dijkstra.py
│   │   ├── bellman_ford.py
│   │   ├── spfa.py
│   │   ├── floyd.py
│   │   ├── prim.py
│   │   ├── kruskal.py
│   │   ├── topological.py
│   │   ├── critical_path.py
│   │   ├── hungarian.py
│   │   └── tarjan.py
│   ├── backtracking/
│   │   ├── framework.py
│   │   ├── permutation.py
│   │   ├── subset.py
│   │   ├── n_queen.py
│   │   ├── sudoku.py
│   │   ├── maze.py
│   │   └── eight_puzzle.py
│   ├── string_algo/
│   │   ├── naive_match.py
│   │   ├── kmp.py
│   │   ├── string_hash.py
│   │   ├── ac_automaton.py
│   │   └── manacher.py
│   ├── data_structure/
│   │   ├── array.py
│   │   ├── linked_list.py
│   │   ├── stack.py
│   │   ├── queue.py
│   │   ├── binary_tree.py
│   │   ├── bst.py
│   │   ├── avl.py
│   │   ├── b_tree.py
│   │   ├── huffman_tree.py
│   │   ├── heap.py
│   │   ├── graph.py
│   │   └── hash_table.py
│   ├── advanced/
│   │   ├── bidirectional_bfs.py
│   │   ├── ids.py
│   │   ├── astar.py
│   │   ├── gcd.py
│   │   ├── prime_sieve.py
│   │   ├── fast_pow.py
│   │   ├── convex_hull.py
│   │   ├── monte_carlo.py
│   │   └── matrix.py
│   ├── memory/
│   └── call_stack/
├── assets/
├── output/
└── examples/
```

---

# Success Criteria

## 基础验证：排序算法

输入：`bubble_sort` 代码
输出：1~3分钟教学视频

✓ 排序概念介绍
✓ 冒泡思想解释
✓ 相邻比较+交换动画
✓ 优化：无交换提前终止
✓ 中文字幕
✓ 中文语音讲解
✓ 变量变化展示
✓ 代码高亮跟踪
✓ 复杂度分析

## 进阶验证：动态规划

输入：`knapsack_01` 代码
输出：3~5分钟教学视频

✓ 背包问题描述
✓ 状态定义讲解
✓ DP表逐步填充动画
✓ 状态转移箭头标注
✓ 空间优化讲解
✓ 与完全背包对比

## 高级验证：图论算法

输入：`dijkstra` 代码
输出：3~5分钟教学视频

✓ 最短路径问题引入
✓ 贪心策略讲解
✓ 松弛操作动画
✓ 距离表实时更新
✓ 负权边失效演示
✓ 与BFS/Floyd对比

---

最终效果：像 AI 编程老师在上课，而不是展示代码执行日志。

---

> 本内容由 Coze AI 生成，请遵循相关法律法规及《人工智能生成合成内容标识办法》使用与传播。
