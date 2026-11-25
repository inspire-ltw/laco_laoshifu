---
name: kd-document-writing
description: 为 KD 光伏工艺（TOPCon、硼扩/BK、LPCVD、PECVD）和管式设备编写或修订技术说明、分析报告、需求文档与 SOP 草稿，统一术语、核实参数并标注出处；写文档时主动询问是否对齐公司模板。
---

# KD 业务文档

按真实路径向上定位 KD 项目根，先读 [文档工作流](../../source/workflows/document-writing.md)，按主题查 [工艺地图](../../source/knowledge/process-map.md)、[设备知识](../../source/knowledge/equipment.md) 或 [测试与材料](../../source/knowledge/quality-and-materials.md)。从输入推断受众、用途与修改边界（可用 [文档简报模板](../../source/templates/document-brief.md)）；修订已有文档时延续其结构与术语。

## 写作约束

- **术语与消歧**：用 `python source/tools/kb.py abbr`（支持多词批量查）及 [名称对照表](../../source/knowledge/name-crosswalk.md) 统一名称。默认英文缩写首次写“中文名（英文全称，缩写）”，纯中文简称/代号首次说明概念与范围；整理译名、符号与化学式不强行展开。一词多义按 [名称消歧流程](../../source/workflows/name-disambiguation.md) 结合上下文确认。
- **未收录简称汇总询问**：阅读输入文档时遇到未收录的新缩写/简称，**不在过程中逐条打断**，在阶段输出时**汇总询问一次**是否录入知识库。
- **参数与证据**：用 `kb.py search` 定位并回查 `source/references/kd/` 原文（索引异常时用 `rg`）。参数写明单位、对象、工步、路线与参考性质；行业典型值、设备能力、现场设定值与验收限不可互换；SOP/配方/验收条款仅采纳现场批准依据，缺失项标待补。效率分清电池/组件、实验室/量产及资料年份；资料冲突查 [缺口与冲突](../../source/knowledge/gaps-and-conflicts.md) 并列出处，不平均取值；安全描述不替代设备手册与 SDS。

## 交付与模板对齐

- 正文区分“资料事实”“分析或设计建议”“待确认事项”，结论附近标注文件名与章节。交付前核对数字、单位、术语、路线与未决事项。
- **主动询问模板对齐**：产出或修改 Word/Excel/PPT 文档时，先完成业务内容，再**主动询问用户**是否需要“对齐到公司模板”或仅做“轻体检”；**仅在用户明确选择“对齐到模板”后**才调用 [laplace-office-standardize](../laplace-office-standardize/SKILL.md) 生效。
