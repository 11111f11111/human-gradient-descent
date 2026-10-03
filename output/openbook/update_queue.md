# Open-book Update Queue

本文件保存 Agent 判断“值得修改”的候选项，不代表已经获得正式修改授权。

| ID | Date | Scope | Trigger | Evidence | Proposed change | Expected benefit | Priority | Authorization | Applied version | Validation | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Field rules

- `Trigger`：`NEW_SOURCE` / `MATERIAL_GRADIENT` / `SOURCE_CONFLICT` / `VERIFIED_CONTENT`。
- `Evidence`：测试 ID、题号、来源页码、资料版本或可核验链接。
- `Authorization`：默认 `NOT_REQUESTED`；用户确认具体范围后改为 `APPROVED`。
- `Status`：`PENDING` / `APPROVED` / `APPLIED` / `VALIDATED` / `REJECTED`。
- `Applied version`：实际修改正式资料时填写 Git commit 或等价版本。
- `Validation`：记录检索测试或近似迁移题结果；没有验证不得标记 `VALIDATED`。

## Constraints

1. Agent 可以自动新增或更新提案，但不得据此直接修改正式开卷资料。
2. 上传新文件只触发差异评估；没有新增考试价值时不创建待办。
3. 用户授权仅覆盖明确确认的待办和范围，不是长期自动授权。
4. 发现正式资料存在错误时立即提醒用户并提高优先级；未经授权仍不得静默更正。
5. 已应用但验证失败的修改必须回滚或重新标记为 `PENDING`。

## Learner shorthand

- `[s]`：将紧邻标记的问题或术语用简短、易懂的中文解释；只说明核心区别或关键因果，不展开长篇背景。

## 学习体验反馈与设计候选

- **用户反馈**：使用 HGD 系统的一大乐趣，是在学习过程中不断得到快速纠错，并逐步建立正确的认知理解。
- **设计候选**：反馈流程应尽可能及时指出错误，说明错误产生的原因，并帮助学习者重建正确的概念模型；随后用简短复述或迁移题确认理解。
- **依据**：用户在强化学习学习过程中，针对公式符号和 Bellman 策略评估的含义提出疑问；经逐项解释和原理推导后，能够概括出固定策略价值是对动作选择及环境转移结果进行概率加权的期望。
- **状态**：已记录为教学交互设计候选，尚未修改 HGD 的正式规范或开卷材料。
