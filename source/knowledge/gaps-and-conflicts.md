# 知识缺口与原文冲突

2026-11-20 复核。下表记录原文差异、公开证据和剩余核验条件。公开研究中的样品与工况、计量定义和现场待确认项分别保留适用范围。原始文件保存为可回查的历史原文。

## 已发现的差异与歧义

| 编号 | 原文位置与表述 | 核查结论与证据 | 剩余核验 |
|---|---|---|---|
| C01 | [15 概述与第 5.2 节](../references/kd/15_tube_furnace_equipment.md)、[07 第 3 节](../references/kd/07_topcon_cells.md)列出不同 TOPCon 工序顺序 | **有证据支持工艺变体。** [PV08](../references/photovoltaics/README.md) 第 6.3.2 节图 6.3 展示先硼扩散再做 TOPCon 层。[ISC Konstanz 图 7](https://www.pv-tech.org/wp-content/uploads/legacy-publication-pdfs/708bb95d4d-topcon-technology-what-exactly-is-it-and-how-mature-is-it-in-production.pdf)记录先沉积后硼扩的公开示例。[Fraunhofer ISE 实验图 3](https://www.ise.fraunhofer.de/content/dam/ise/de/documents/publications/conference-paper/37th-eupvsec-2020/Driessen_2BO23.pdf)另验证了预先沉积 TOPCon 层、再硼扩与晶化的实验路线 | 产品、线别、硼扩与背面工序实际顺序及配方版本 |
| C02 | [07 第 3 节](../references/kd/07_topcon_cells.md)与[15 第 1.4 节](../references/kd/15_tube_furnace_equipment.md)的硼扩温度和发射极方阻范围不同 | **条件依赖得到证实。** 公开 BCl₃ 管扩实验报道过 90–110 Ω/sq，另一项无硼选择性发射极工艺报道 140–150 Ω/sq。选择性发射极研究还分别考察驱入、后氧化和气源对掺杂剖面、复合及接触的影响。[90–110 Ω/sq 样品](https://www.sciencedirect.com/science/article/pii/S0749603620312696) · [140–150 Ω/sq 样品](https://www.sciencedirect.com/science/article/pii/S0927024823004063) · [硼管扩参数实验](https://www.sciencedirect.com/science/article/pii/S0927024823000521) | 原文范围对应的气源、预沉积/驱入/后氧化、测量阶段、SE 区域和批准方阻 |
| C03 | [15 概述及第 2.4、3.4、5.1 节](../references/kd/15_tube_furnace_equipment.md)并列 10–110 Pa、氧化 110 Torr 和沉积约 10 Pa | **换算已核实。** 110 Torr ≈ 14.67 kPa，约为 110 Pa 的 133 倍。氧化和沉积是不同工步，汇总区间不能直接覆盖氧化所列值。[NIST 压力换算](https://www.nist.gov/pml/owm/metric-si/unit-conversion/pressure-and-gas-flow-unit-conversions) | 查批准配方、压力通道、绝压/表压及原始 HMI 单位，确认是否存在抄录错误 |
| C04 | [15 第 3.4 节](../references/kd/15_tube_furnace_equipment.md)同一 SiH₄ 行标为最大 0.4 SLM、最优 790 sccm | **同基准下数值倒挂。** 0.4 SLM = 400 sccm。同标准温压、同气体/等效标定、同通道且同设定含义时，两值不能同时作为上限和推荐点。NIST 也提示 sccm 可能采用不同参考温度。[NIST 气体流量换算](https://www.nist.gov/pml/owm/metric-si/unit-conversion/pressure-and-gas-flow-unit-conversions) | 查 MFC 铭牌和校准证书、气体修正、量程、单路或合计，以及配方导出 |
| C05 | [15 第 2.2、2.7 节](../references/kd/15_tube_furnace_equipment.md)混写 HCl、TCA 和 TCE | **物质身份可区分。** HCl 是氯化氢（CAS 7647-01-0），TCE 在此指三氯乙烯（79-01-6）。TCA 在第 2.7 节只展开为三氯乙烷，需要确认异构体，1,1,1- 为 71-55-6，1,1,2- 为 79-00-5。[NIOSH CAS 索引](https://www.cdc.gov/niosh/npg/npgdcas.html) · [氯化氢](https://www.cdc.gov/niosh/npg/npgd0332.html) · [1,1,1-三氯乙烷](https://www.cdc.gov/Niosh/npg/npgd0404.html) · [1,1,2-三氯乙烷](https://www.cdc.gov/niosh/npg/npgd0628.html) | 查物料编码、CAS、安全数据表（SDS）、管路标识和批准工艺 |
| C06 | [08 第 3–4 节](../references/kd/08_hjt_cells.md)区分低温金属化与退火，[15 第 4.5 节](../references/kd/15_tube_furnace_equipment.md)写 HJT 全程低于 200 ℃ | **全程上限缺乏依据。** 氢化非晶硅钝化的热敏感性支持低热预算；公开异质结实验包含达到 200 ℃ 及超过 200 ℃ 的独立热处理/光热处理步骤。[低温钝化与金属化研究](https://www.sciencedirect.com/science/article/pii/S0038092X18300951) · [光热处理研究](https://www.sciencedirect.com/science/article/pii/S1369800122007181) | 分别确认沉积、退火、浆料固化的温度、时长、温度测量对象及批准热预算 |
| C07 | [15 第 3.9、5.3 节](../references/kd/15_tube_furnace_equipment.md)将气泡归于 PECVD，另在 LPCVD 栏列出同一条目并称 LPCVD 免疫 | **氢起泡机制有实验证据，免疫表述超出证据。** 研究在特定 LPCVD 样品未见氢泡，PECVD 样品则受氢、膜微结构、表面和热历史共同影响。按失效层、形貌和实际路线排查。[Scientific Reports 氢起泡实验](https://www.nature.com/articles/s41598-020-66801-4) | 样品层位、沉积路线、是否氢化、退火历史及显微证据 |
| C08 | [15 第 1.7 节](../references/kd/15_tube_furnace_equipment.md)列出的 BSG 厚度、去除时间和刻蚀速率不能相互覆盖 | **原文数字不能组成同一工况。** 按原报约 20 nm/min，1–2 min 仅对应 20–40 nm，低于原列保护层厚度。公开实验在其路线中将去绕镀和后续 BSG 去除分别执行，未验证这组厚度、时间与速率。[Fraunhofer ISE／RENA 去绕镀实验，第 2 节](https://publica-rest.fraunhofer.de/server/api/core/bitstreams/90ea6835-a3c9-4e34-8275-3608673eb512/content) | 批准湿法工艺、同条件前后膜厚、验证记录和终点判据 |
| C09 | [14 第 2.4 节](../references/kd/14_key_materials.md)单耗表头 g/片，单元格 mg/片 | **表内单位冲突已定位。** 数字解析优先保留单元格显式单位。80–120 mg/片相当于 0.080–0.120 g/片，100–150 mg/片相当于 0.100–0.150 g/片。换算只复述原表数据，单耗未独立验证 | 称量记录、片型、印刷面、银浆湿重/干重/银含量口径及适用版本 |
| C10 | [13 第 3.1、3.3 节](../references/kd/13_cell_testing_characterization.md)的 EQE 和 SR 积分复用 Φ，输入容易混淆 | **量纲已厘清。** EQE 对光子通量积分，SR 对光谱辐照度积分。统一波长坐标与单位后两式等价，详见[测试质量](quality-and-materials.md#短路电流密度的光谱积分)。[Sandia SR 与 QE 关系](https://pvpmc.sandia.gov/modeling-guide/2-dc-module-iv/effective-irradiance/spectral-response/) · [IEC 60904-3:2019](https://webstore.iec.ch/en/publication/61084) | 现场光谱文件、波长和面积单位、参考光谱版本、测试校准 |

对资料层面已厘清的条目，现场值仍按右列取证。确认记录应附来源、版本、适用设备与生效时间。

## 缺少的现场知识

2026-10-28 已从数据集补充局部字段名称及工序代号证据，见[名称对照表](name-crosswalk.md)、[800G证据](../evidence/dataset-800g-aliases.json)与[其他数据集证据](../evidence/dataset-other-aliases.json)。这使部分原始字段可解释，但以下缺口仍不能视为已获得现役全厂批准口径。尤其用户已确认 `PK=磷扩散`，旧800G文档的 `pk=退火` 只保留历史标签；`OD` 的方阻和膜厚检测用途分别限定范围，均不自动做全局同义展开。

| 编号 | 已补证据 | 尚需现场或项目确认 | 可先完成的工作 |
|---|---|---|---|
| G01 | 公开资料可说明工艺与指标的通用背景 | 实际工厂、线别、目标岗位、交付及审批口径 | 按交付对象记录适用范围 |
| G02 | 工艺地图与设备知识提供技术路线和分析粒度，数据集提供局部命名样例 | 设备台账、炉管/温区层级、舟与批次关联、实际技术路线 | 检查候选键、对象分布及关联覆盖 |
| G03 | 已有局部数据集名称证据和[通用采集字段建议](oee-measurement.md#现场数据与核验) | 部署版数据字典、表结构、状态码、采集周期和质量码 | 结合真实样本做字段和缺失画像，标注候选映射 |
| G04 | 已有[生产时间与跨日班次](oee-measurement.md#现场数据与核验)的核对项 | 现场时区、班次排班与跨日、生产日定义及同步记录 | 统计时间分布、重复、乱序与间隔 |
| G05 | 已登记[通用 A/P/Q、OEE 公式和行业标准](oee-measurement.md#指标与适用范围) | 计划时间、状态优先级、分类、理想节拍、返工/计数及汇总规则 | 展示原始区间与产量分布，按假设口径演算 |
| G06 | 已核查典型工艺变体、失效机理与原文参数冲突（C01–C08） | 批准配方、工艺窗口、报警与联锁阈值、产品规格和生效时间 | 按实际路线分层查看历史分布，定位需要确认的工步 |
| G07 | 已登记 [I–V、参考光谱与光谱响应标准](quality-and-materials.md#短路电流密度的光谱积分)及积分量纲 | 校准记录、现场测试条件、抽样、质量等级、缺陷判定、复测规则 | 检查同测量条件和样本完整性后分组比较 |
| G08 | 知识库提供[软件工作流](../workflows/software-development.md)与[变更清单](../templates/change-checklist.md) | 实际仓库版本、正式接口配置、环境、权限与部署流程 | 在项目仓库核对接口并验证离线处理 |
| G09 | 已核实 Torr/Pa、SLM/sccm 公共计量关系（C03、C04） | 绝压/表压、测点含义、MFC 标准温压、气体修正和设备量程 | 保留原值、单位和工步，按确认基准换算 |

补充现场资料时建议记录：条目、值或规则、来源文件/责任方、版本、适用范围、生效时间、确认状态。仅有样本推断时保持“候选”，不能自动升格为批准规则。

## 时效与证据边界

[00 索引](../references/kd/00_index.md)、[07 TOPCon](../references/kd/07_topcon_cells.md)、[10 技术对比](../references/kd/10_technology_comparison.md)及其他资料包含2024–2026年的效率纪录、市场份额、成本、产能、材料价格和预测。文件复制日期或修改日期不代表这些数据已更新。

当前仅把它们作为带出处的历史参考，不确认其在2026年10月仍然最新。用户要求当前市场、纪录、标准适用性或采购成本时，应另行核验原始发布方和日期；新证据单独入库，不覆盖原始快照。

原资料的“优秀值”“量产推荐”“必须”“强制更换”等措辞也不能自动变成现场审批要求、质量验收线或维护工单。应以实际已批准资料及明确适用范围为依据。
