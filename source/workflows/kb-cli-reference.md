# `kb.py` 检索、简称与维护命令参考

从 `D:\work\KD` 运行（Python 3.10+，仅用标准库）。工具按脚本真实路径定位知识库，可在任意目录调用。

## 常用检索与校验命令

```powershell
python source/tools/kb.py search "硼扩散 炉管" --limit 5
python source/tools/kb.py search "OEE 状态 分母" --category workflows --json
python source/tools/kb.py search "氮化硅" --category references
python source/tools/kb.py abbr BK PE PK --json
python source/tools/kb.py abbr "硼扩散"
python source/tools/kb.py abbr --category testing --limit 10
python source/tools/kb.py index --check
python source/tools/kb.py verify
```

Windows 本机 `python` 若指向应用执行别名，可调用指定解释器：

```powershell
$kdPython = 'C:\Users\tianw\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $kdPython source/tools/kb.py search "LPCVD 压力"
& $kdPython -m unittest discover -s source/tests -v
```

## 检索与简称规则说明

- 检索按标题、关键词、中文双字片段和已确认简称评分；命中 Markdown 表格数据行时自动保留表头。支持 `--category references|knowledge|workflows|templates|evidence` 与 `--limit 1..50`。索引异常时改用 `rg -n "关键词" source` 查证。
- `abbr` 支持单词、多词批量查询及省略查询列清单。`short_names` 记录 `kind`（`chinese_short|english_short|dataset_code|symbol`）、`status`（`user_confirmed|dataset_explicit|dataset_inferred|knowledge_explicit|curated`）、`scope` 与 `sources`。候选不自动扩同义，不按拼音猜 LP/TX，局部证据不自动升格为全厂规则。
- 一词多义按 [名称消歧工作流](name-disambiguation.md) 结合上下文判断；仍不足时向用户确认。

## 更新快照与维护索引

普通整理优先编辑 `knowledge/` 与 `workflows/`，保留 `references/kd/` 只读原文。仅在明确要求导入/更新原文快照时执行：

```powershell
python source/tools/kb.py snapshot --source 'C:\work\OEE\git\OEE_algo\KD\OEE_docs\kd'
# 原文变化时审阅差异后加 --update
python source/tools/kb.py crosswalk
python source/tools/kb.py index
python source/tools/kb.py verify
python source/tools/kb.py crosswalk --check
```

Windows 移动/复制工作区后，如 `.agents/skills/` 目录联接指向旧路径，确认移除旧联接后运行 `& .\source\tools\connect-skills.ps1` 重建。
