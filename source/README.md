# KD 工作知识库

本知识库服务于光伏制造（TOPCon 与管式硼扩散、氧化、LPCVD、PECVD）的数据处理、技术文档和程序开发，建于 2026-10-28。这是参考资料整理与工作方法，不是已核准的工厂规范。

## 按主题查阅

全景见 [KD 知识体系树](knowledge/knowledge-tree.md) 与 [光伏知识体系导读](knowledge/pv-knowledge-map.md)；原文出处查 [KD 原始总目录](references/kd/00_index.md)、[光伏图书与标准原件目录](references/photovoltaics/README.md) 与 [拉普拉斯公开研究与专利](references/laplace-public/README.md)。

| 当前问题 | 入口 |
|---|---|
| 工艺路线、电池技术、晶硅制造原理 | [工艺地图](knowledge/process-map.md)、[晶硅电池制造工艺原理](knowledge/pv-device-and-manufacturing.md) |
| 炉管、舟、温区、真空、气路、配方 | [设备知识](knowledge/equipment.md) |
| IV、EL、PL、寿命、材料与器件结构 | [质量与材料](knowledge/quality-and-materials.md)、[光伏材料、界面与器件结构](knowledge/pv-device-physics.md) |
| 钙钛矿叠层、组件发电与系统维护 | [钙钛矿与叠层产业化](knowledge/perovskite-scale-up.md)、[光伏系统性能与维护](knowledge/pv-system-and-maintenance.md) |
| 简称、缩写、数据集代号与一词多义 | [名称对照表](knowledge/name-crosswalk.md)、[术语表](glossary.json)、[名称消歧工作流](workflows/name-disambiguation.md) |
| 缺口、资料冲突与待确认口径 | [缺口与冲突](knowledge/gaps-and-conflicts.md) |
| 数据分析 / 文档编写 / 程序开发工作流 | [数据工作流](workflows/data-analysis.md)、[文档工作流](workflows/document-writing.md)、[程序工作流](workflows/software-development.md) |
| Office 模板规范化、轻体检与 Logo | [laplace-office-standardize](../skills/laplace-office-standardize/SKILL.md) |

## 资料层次与可信范围

- `references/kd/`：只读原文快照（`manifest.json` 记 SHA-256），描述参考条件，不自动代表现场标准。
- `knowledge/` / `evidence/` / `workflows/` / `templates/`：派生摘要、数据集局部证据、Agent 工作建议与契约模板（`null` 表示未知，非零或已确认）。
- 时效性数据（效率纪录、市场份额、成本）保留原文年份；现役数据库、点位、排班、批准 OEE 口径与验收/报警限须以现场资料为准。

## 常用命令（完整说明见 [CLI 命令参考](workflows/kb-cli-reference.md)）

```powershell
python source/tools/kb.py search "硼扩散 炉管" --limit 5
python source/tools/kb.py abbr BK PE PK --json
python source/tools/kb.py crosswalk; python source/tools/kb.py index; python source/tools/kb.py verify
```

实体 skills 位于 `skills/`（`.agents/skills/` 为目录联接），路由见 [AGENTS.md](../AGENTS.md)。
