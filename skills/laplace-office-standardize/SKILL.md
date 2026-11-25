---
name: laplace-office-standardize
description: 将拉普拉斯 Word、Excel、PPT（.docx/.xlsx/.pptx）按选定模板与公司样式规范化并应用公司 Logo，支持单文件/批量处理、轻体检与新文档加入模板库；仅在用户明确选择“对齐到模板”时生效，不改写业务结论。
---

# 拉普拉斯 Office 文档规范化

对选定文件副本套用模板、统一样式并嵌入公司 Logo，交付规范化文件和处理报告。使用本目录 `scripts/office.py`（解析 `SKILL.md` 真实路径定位资源）。

## 触发时机与轻体检

- **按需生效**：写文档或修改文档过程中，不静默套用模板；应主动询问用户是否需要**“对齐到公司模板”**或仅做**“轻体检”**（只输出字体混用、分页/表头、Logo 规范等问题清单，不改动原版式）。仅在用户明确选择“对齐到模板”后才执行套模板。
- **新文档加入模板库**：当用户提供的新文档不属于当前模板库（[company-profile.json](assets/company-profile.json) 及已登记模板）时，**主动询问用户是否要将其加入模板库**。若用户选择“是”：
  1. 根据文件内容自动拟定**模板名称**（如“客户技术方案 Word 模板”）与**适用范围**（适用文档类型、受众、典型章节/表格特征）；
  2. 展示给用户确认后，再复制为新配置版本并登记模板路径、来源与 `approval_status=draft`，不覆盖已有模板。

## 模板与输入约定

- 默认配置：[company-profile.json](assets/company-profile.json)（`approval_status=draft` 为可审阅草案，不称作已批准标准）。
- 默认另存副本，脚本拒绝覆盖输入和已有输出。`.doc/.xls/.ppt` 旧格式需先转为现代格式；加密、受保护、含宏或数字签名文件单独处理，不静默移除保护或宏。

## 执行

在项目根运行（原生模板接口需 Windows + MS Office + PowerShell；`doctor` 仅查依赖）：

```powershell
python skills/laplace-office-standardize/scripts/office.py doctor
python skills/laplace-office-standardize/scripts/office.py apply "输入文件夹" --output "新的输出目录" --recursive --dry-run
python skills/laplace-office-standardize/scripts/office.py apply "输入文件夹" --output "新的输出目录" --recursive --pdf
```

其他配置在子命令前加 `--profile "配置路径"`；仅缺失模板或用户要求时运行 `templates`（不覆盖已有文件）。复杂表格、PPT 画布及对象边界见 [格式与保真约定](references/format-contract.md)。脚本不重写正文或重算业务指标。

## 检查与交付

- 核对 `standardization-report.json`（成功/失败、配置版本、保真检查、哈希与复核提示）；失败文件不作为成功结果交付。
- `processed_needs_visual_review` 仅表示程序检查通过，需人工或借 `--pdf` 副本复核分页、表格、公式、文字溢出及 Logo 遮挡；仅实际视觉检查后才表述为已检查版式。
- Logo 按原图比例使用，仅替换 `LaplaceDocs.CompanyLogo` 标记对象，避免重复叠加。交付时说明采用的是草案还是批准模板。
