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
