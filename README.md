# Human Gradient Descent

> **讲义炼丹炉：碳基神经网络手动反向传播系统**  
> *Train yourself like a neural network.*

人脑也是神经网络，只是反向传播需要手动完成。

本项目是一套面向课程学习、考试复习与知识库建设的可复用工作流：把课件和习题作为训练数据，把做题视为前向传播，根据错题计算 Loss，再通过错因诊断完成反向传播和参数更新。经过多个 Epoch 后，将真正理解、测试并纠正过的内容压缩成可检索的开卷讲义。

这里不生产“看过等于学会”的学习幻觉。每个知识点都需要经过概念理解、题型识别、独立作答、错误诊断和迁移测试，才能被标记为掌握。

**Slides are datasets. Exercises are training loops. Mistakes are gradients. Exams are inference.**

| 碳基训练过程 | 神经网络术语 |
|---|---|
| 阅读课件与接收题目 | Input / Dataset |
| 尝试独立作答 | Forward Pass |
| 对照答案与评分 | Loss Calculation |
| 定位错误原因 | Backpropagation |
| 修改理解与解题方法 | Parameter Update |
| 进入下一轮复习 | Next Epoch |
| 只会原题、不会变式 | Overfitting |
| 能迁移到历年题 | Generalization |
| 正式考试 | Inference |

这是一个可复制到新课程项目中的空白模板。它不是普通笔记目录，而是一套让 ChatGPT/Codex、Gemini/NotebookLM 与学生持续协作的学习状态系统。

## 1. 初始化（新课程只做一次）

1. 复制整个文件夹，并改成课程名称。
2. 填写 `config/course.yaml`。
3. 把课件、习题、官方答案和历年题放入 `sources/` 对应目录。
4. 在 `sources/manifest.yaml` 登记文件来源与范围。
5. 在 `status/mastery.yaml` 建立章节条目。
6. 第一次让 Agent 工作时，要求它先读取 `AGENTS.md`。

## 2. 推荐读取顺序

1. `AGENTS.md`
2. `config/course.yaml`
3. `status/mastery.yaml`
4. `mistakes/mistakes.md`
5. `output/openbook/`
6. `exam/exam_map.md`
7. 当前任务涉及的 `tests/`、`vocabulary/`、`kb/`、`exercise/`

不要只依据 `mastery.yaml` 判断掌握度；必须结合错题、测试记录和最近一次学习回执。

## 3. 核心工作流

```text
课件/习题/真题
  → 概念讲解
  → 学生复述或完成第一步
  → 分层提示与逐步解题
  → 小测和迁移题
  → 错误分类
  → 更新掌握度
  → 压缩进开卷材料
```

第二轮复习建议：闭卷回忆 → 题型识别 → 固定计算套路 → 独立习题 → 历年题迁移 → 综合测试 → 错因诊断 → 压缩开卷页。

## 4. 目录说明

| 路径 | 用途 |
|---|---|
| `config/` | 课程目标、考试形式和协作设置 |
| `sources/` | 原始课件、习题、答案、真题；不在此改写原文件 |
| `kb/` | 按章节整理的详细知识库 |
| `exercise/` | 独立习题讲解与练习记录 |
| `exam/` | 历年题及“题目—知识点—章节”映射 |
| `tests/` | 无答案提示的小测、综合测验及作答记录 |
| `mistakes/` | 错题与错误类型诊断 |
| `vocabulary/` | 中英术语和常见英文题干 |
| `status/` | 掌握度与最近学习状态 |
| `output/openbook/` | 高密度、可打印、双语开卷材料 |
| `handoff/` | 不同模型或新会话之间的只读交接 |

## 5. 文件命名

- 章节知识库：`kb/ch01_topic.md`
- 独立习题：`exercise/ch01/ex_01.md`
- 测试：`tests/ch01_test_01.md`
- 开卷页：`output/openbook/ch01.md`
- 使用两位数字章节号，保证排序稳定。

## 6. 状态定义

- `PASS`：能独立识别题型并完成核心步骤。
- `PARTIAL`：理解主要概念，但仍需提示或容易计算出错。
- `REVISIT`：概念、识别或公式调用仍不稳定，需要重新学习。
- `NOT_STARTED`：尚无有效学习证据。

## 7. 模型分工

- ChatGPT/Codex：概念讲解、难推导、首次习题、诊断、复习规划和仓库写入。
- Gemini/NotebookLM：基于上传来源做检索、选择题测试和只读交接。
- Gemini/NotebookLM 不直接修改本项目；把结果写入 `handoff/inbox.md`，再由 ChatGPT/Codex核验后更新。

## 8. 开卷材料原则

只收录已经理解、测试、纠正过且考试时能直接调用的内容。优先放：题型识别信号、关键公式、固定步骤、易混淆对比、典型错误和来源位置。详细推导留在 `kb/` 或 `exercise/`，不要把开卷页写成教材。

## 9. License

本仓库中的学习框架、文档、提示词和 Markdown 模板采用 [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/) 许可。

你可以出于非商业目的复制、修改和传播，但必须注明来源；公开传播修改版本时，必须继续采用相同或兼容许可。任何商业使用都需要事先取得作者的单独授权。课程课件、教材、历年试题、官方答案以及其他第三方材料不属于本授权范围，其著作权仍归各自权利人所有。详见 `LICENSE.md`。
