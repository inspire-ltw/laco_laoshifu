---
name: kd-context
description: 为 KD 光伏工艺（TOPCon、硼扩/BK、PECVD/PE、LPCVD、PK、OD）与管式设备检索本地知识、查询中英文简称及一词多义消歧，遇到未收录简称时汇总询问录入；不用于无关行业问答。
---

# KD 业务上下文

按真实路径（处理 `.agents/skills` 目录联接）向上定位含 `source/README.md` 与 `source/tools/kb.py` 的项目根。先读 [知识库入口](../../source/README.md) 按需取证，不整库装入上下文。

## 按问题取证

| 问题 | 优先入口 |
|---|---|
| 技术路线、工序顺序 | [工艺地图](../../source/knowledge/process-map.md) |
| 硼扩散、氧化、LPCVD、PECVD 与设备层次 | [设备知识](../../source/knowledge/equipment.md) |
| IV、EL、PL、寿命、材料与质量 | [测试与材料](../../source/knowledge/quality-and-materials.md) |
| 中文简称、英文缩写、数据集代号 | `source/glossary.json`、[名称对照表](../../source/knowledge/name-crosswalk.md) |
| 资料矛盾或现场定义不足 | [缺口与冲突](../../source/knowledge/gaps-and-conflicts.md) |

- 检索：`python source/tools/kb.py search "硼扩散" --limit 5`，引用数字前打开命中的 `source/references/kd/` 原文。索引失效或工具不可用时改用 `rg -n "关键词" source/references/kd source/knowledge source/workflows`，不因此改写原文。
- 查简称（支持单查与多词批量查）：`python source/tools/kb.py abbr BK PE PK --json`，或按概念查 `abbr 硼扩散`。同时核对 `kind`、`status`、`scope` 与 `sources`；候选不自动扩同义，不按拼音猜 LP/TX，局部证据不视为全厂规则，`curated_translation` 不称作原文明示。
- **一词多义消歧**：按 [名称消歧流程](../../source/workflows/name-disambiguation.md) 结合上下文推断并注明依据；仍多义、证据不足或冲突时列 2–3 个候选向用户确认，确认前暂停依赖该含义的计算或结论。
- **未收录简称汇总询问**：阅读文档或批量查词发现知识库未收录的新简称/缩写时，不在过程中逐条打断，任务阶段结束时**汇总询问一次**是否录入知识库。

## 使用证据

- 区分“原资料记载”“分析推断或建议”“待现场确认”；数字保留单位、工步、路线与资料年份，不同压力单位先换算再比较（如 `110 Torr` ≠ `110 Pa`）。
- 摘要与原文分歧时并列原文位置与冲突；本地库不含现场数据字典、OEE 映射、报警阈值与批准配方，缺失项仅限制依赖它的结论。重要结论附近标明文件名与章节。
