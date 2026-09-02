# Tests

测试题正文不附答案提示。每次测试分别保存：

- `*_paper.md`：题目、范围、计时、评分方式和考试条件；
- `*_response.md`：学生原始作答，不在评分后覆盖；
- `*_review.md`：答案、评分、逐项 Loss、梯度、更新和复测。

## Required metadata

每组测试至少记录：

```yaml
operation_id:
test_id:
context: OPEN_BOOK | CLOSED_BOOK
started_at:
completed_at:
source_scope: []
openbook_material_version: null
```

闭卷测试的 `openbook_material_version` 保持 `null`。开卷测试必须记录实际使用的 Git commit、文件版本或等价快照。

## Open-book mock exam

模拟考试测试的是“学生 + 当前版资料”的联合系统。除答案与得分外，每题还要记录：

- 作答用时；
- 使用的检索关键词或入口；
- 检索耗时；
- 是否找到所需内容；
- 找到后是否可以直接执行；
- `HUMAN`、`MATERIAL`、`BOTH` 或 `UNCERTAIN`；
- 对应的人梯度与资料梯度；
- 更新后的同构或近似迁移复测。

资料梯度只能进入 `output/openbook/update_queue.md`。用户明确授权前，不得在评分或复测过程中静默修改正式开卷资料。

## Status update

- 开卷测试只更新 `mastery.yaml` 的 `open_book` context。
- 闭卷测试只更新 `closed_book` context。
- 一次总分不能无依据地降低所有知识点或所有维度。
- 只有写后验证成功、测试文件可重新读取时，才能将证据链接到掌握度。
