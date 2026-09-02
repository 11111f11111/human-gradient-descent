# Loss and Gradient Log

只记录有实际作答、用时或检索证据支持的 Loss。人的问题与资料的问题分开记录，不用总分评价个人。

| ID | Date | Test / Source | Topic | Context | Observed Loss | Attribution | Human gradient | Material gradient | Update | Retest | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|

## Attribution

- `HUMAN`：资料入口和内容足够，但概念、识别、公式、计算、语言、验证或迁移失败。
- `MATERIAL`：学习者知道或能说明方法，但资料缺失、难找、条件不全或无法直接执行。
- `BOTH`：人的能力与资料设计均有独立证据表明需要更新。
- `UNCERTAIN`：现有证据不足；必须设计最小验证题，不能武断归责。

## Human gradient

`CONCEPT` / `RECOGNITION` / `FORMULA` / `CALCULATION` / `LANGUAGE` / `VERIFICATION` / `TRANSFER`

## Material gradient

`MISSING` / `INDEXING` / `CONDITION` / `ACTIONABILITY` / `DENSITY` / `EXAMPLE_GAP` / `ERROR`

## Recording rules

1. `Context` 必须写 `OPEN_BOOK` 或 `CLOSED_BOOK`；开卷还要在测试记录中注明资料版本。
2. 资料梯度写入 `output/openbook/update_queue.md`，不直接修改正式开卷资料。
3. `Update` 记录人的训练或资料修改提案；未经用户授权的资料修改写 `PROPOSED`。
4. 只有同构或近似迁移复测确认 Loss 下降后，才能将记录标记为 `RESOLVED`。
5. 旧记录迁移时缺失字段标记 `UNKNOWN`，不得补写虚构证据。
