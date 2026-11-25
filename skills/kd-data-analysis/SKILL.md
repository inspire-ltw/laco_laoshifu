---
name: kd-data-analysis
description: 分析 KD 光伏产线、管式设备、批次工艺、方阻/EL/PL 与 OEE 数据，识别粒度、单位、质量与统计口径；适用于相关 CSV、Excel、日志和 SQL 分析，不用于无关业务。
---

# KD 数据分析

按真实路径向上定位 KD 项目根，先读 [数据工作流](../../source/workflows/data-analysis.md)，按需查 [设备知识](../../source/knowledge/equipment.md)、[测试与材料](../../source/knowledge/quality-and-materials.md)、[缺口与冲突](../../source/knowledge/gaps-and-conflicts.md) 及 `source/templates/data-contract.yaml`。

## 术语与取证

- 检索背景用 `python source/tools/kb.py search "LPCVD" --limit 5`（索引异常时用 `rg` 查原文）；字段/日志含多个简称或代号时用 `python source/tools/kb.py abbr BK PE PK --json` 批量查证，结合 [名称对照表](../../source/knowledge/name-crosswalk.md) 核对 `status/scope`，保留 Voc、J₀、η 等符号与化学式。
- 一词多义按 [名称消歧流程](../../source/workflows/name-disambiguation.md) 结合邻列、单位、路径与工序判断；无法确定时先列候选确认，确认前不做依赖含义的改名、合并或结论。遇到多个未收录代号时**汇总询问一次**是否录入。

## 分析护栏

- **粒度与关联**：确认每行是设备、炉管、舟、批次、工步还是单片测试，核实主键与一对多关系再聚合。
- **单位与基准**：保留原始列，记录映射、单位换算与时区；区分设定/实测、绝压/表压、炉温/片温、工步/整批时长；未确认单位不横向排名。
- **数据质量**：明确处理重复、计数器复位、跨日批次、缺测、补录与状态重叠；未知 ≠ 零；加权先明分母。
- **对比与指标**：先按路线、工序、配方版本分组；原文范围只供排查，不作剔除规则或报警限。IV 核实测试条件与面积；EL/PL 须有判定规则才算良率；OEE 须有现场批准状态映射、计划时间、理想节拍与层级才出正式值，否则仅输出概况/时间线或标明假设的演示。

## 交付与复核

按 [分析报告模板](../../source/templates/analysis-report.md) 记录口径、数据问题、结果、证据与待确认项；校验关联前后行数与计数守恒、单位维度、时间覆盖与分母为零；保留可重跑脚本与参数，引用原文文件与章节。
