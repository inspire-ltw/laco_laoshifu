---
name: kd-software-development
description: 开发或修改 KD 光伏产线数据处理、管式炉日志解析、工艺分析与 OEE 相关程序，将本地业务知识转为明确的数据契约与边界测试；不用于无关程序开发。
---

# KD 业务程序开发

按真实路径向上定位 KD 项目根，先读 [程序工作流](../../source/workflows/software-development.md)，按变更查 [设备知识](../../source/knowledge/equipment.md)、[工艺地图](../../source/knowledge/process-map.md) 与 [缺口与冲突](../../source/knowledge/gaps-and-conflicts.md)。先读目标仓库现有模型、接口、样例与测试，避免另造命名；可用 `source/templates/data-contract.yaml` 与 [变更检查表](../../source/templates/change-checklist.md) 记录约束。

## 术语与领域建模

- 查字段/日志中的简称或代号用 `python source/tools/kb.py abbr`（支持多词批量查）及 [名称对照表](../../source/knowledge/name-crosswalk.md)，一词多义按 [名称消歧流程](../../source/workflows/name-disambiguation.md) 核对，未确认候选不硬编码为全厂映射；遇到多个未收录代号时**汇总询问一次**。背景检索用 `kb.py search`（异常时 `rg` 查原文）。
- **实体与主键**：区分设备、炉管、舟、批次、配方版本、工步与片号，核实基数再连接聚合，不假设单设备单管或单批次单行。
- **单位与配置**：保留来源、时区与单位，转换显式可追溯（区分设定/实测、Torr/mbar/Pa、绝压/表压、时间戳/时长）。原文参考工艺参数不得硬编码为生产默认值或报警限，须通过配置注入并保留未配置态。
- **OEE 与边界**：无现场批准 OEE 口径时，仅实现解析、清洗、时间线或骨架，正式指标明确返回未配置/不可计算，不静默输出零。跨窗口、重复、乱序、计数器复位、区间重叠与缺测保留诊断信息，不静默吞数据。

## 验证交付

针对变更涉及场景编写边界测试（单位换算、重复与复位、跨日/跨班、重叠区间、未知状态、分母为零），使用脱敏或标明合成的样例。报告改动、已执行检查与仍受口径缺失限制的行为；新业务规则仅在用户要求维护知识库时入库。
