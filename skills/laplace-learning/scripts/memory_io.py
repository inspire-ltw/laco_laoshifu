#!/usr/bin/env python3
"""Export/import ~/.laco-laoshifu/private-memory bundles to/from Desktop (stdlib only)."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import shutil
import sys
import zipfile

DEFAULT_MEMORY_DIR = Path.home() / ".laco-laoshifu" / "private-memory"
DEFAULT_DESKTOP = Path.home() / "Desktop"
MANIFEST_NAME = "memory-bundle-manifest.json"
ALLOWED_REL_PREFIXES = ("index.md", "profile.md", "projects/")


def is_allowed_file(rel: str) -> bool:
    if rel in {"index.md", "profile.md"}:
        return True
    return rel.startswith("projects/") and rel.endswith(".md") and ".." not in Path(rel).parts


def collect_memory_files(memory_dir: Path, project: str | None = None) -> list[tuple[str, Path]]:
    if not memory_dir.is_dir():
        raise FileNotFoundError(f"私有记忆目录不存在: {memory_dir}")
    files: list[tuple[str, Path]] = []
    for name in ("index.md", "profile.md"):
        p = memory_dir / name
        if p.is_file() and (project is None or name == "index.md"):
            files.append((name, p))
    projects_dir = memory_dir / "projects"
    if projects_dir.is_dir():
        for p in sorted(projects_dir.glob("*.md")):
            if project and p.stem != project:
                continue
            files.append((f"projects/{p.name}", p))
    if not files:
        raise ValueError("未找到可导出的有效记忆文件（不包含历史记录与敏感凭据）。")
    return files


def export_bundle(memory_dir: Path, output: Path | None = None, project: str | None = None) -> Path:
    files = collect_memory_files(memory_dir, project=project)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    scope_tag = f"-{project}" if project else ""
    if output is None:
        out_dir = DEFAULT_DESKTOP if DEFAULT_DESKTOP.is_dir() else Path.home()
        out_path = out_dir / f"laplace-memory{scope_tag}-{ts}.zip"
    else:
        out_path = output.expanduser().resolve()
        if out_path.is_dir():
            out_path = out_path / f"laplace-memory{scope_tag}-{ts}.zip"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    manifest = {
        "schema_version": 1,
        "exported_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "scope": project or "all",
        "files": [rel for rel, _ in files],
    }
    with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(MANIFEST_NAME, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        for rel, path in files:
            zf.write(path, arcname=rel)
    return out_path


def inspect_bundle(bundle_path: Path, memory_dir: Path) -> dict:
    bundle_path = bundle_path.expanduser().resolve()
    if not bundle_path.is_file():
        raise FileNotFoundError(f"找不到记忆包: {bundle_path}")
    new_files = []
    conflicts = []
    with zipfile.ZipFile(bundle_path, "r") as zf:
        if MANIFEST_NAME not in zf.namelist():
            raise ValueError(f"无效记忆包：缺少 {MANIFEST_NAME}")
        manifest = json.loads(zf.read(MANIFEST_NAME).decode("utf-8"))
        for name in zf.namelist():
            if name == MANIFEST_NAME or name.endswith("/"):
                continue
            if not is_allowed_file(name):
                raise ValueError(f"记忆包包含不支持的路径: {name}")
            target = memory_dir / name
            if target.exists():
                conflicts.append(name)
            else:
                new_files.append(name)
    return {"manifest": manifest, "new_files": new_files, "conflicts": conflicts}


def import_bundle(bundle_path: Path, memory_dir: Path, *, apply: bool = False, overwrite: bool = False) -> dict:
    preview = inspect_bundle(bundle_path, memory_dir)
    if not apply:
        return {**preview, "applied": False}
    memory_dir.mkdir(parents=True, exist_ok=True)
    history_dir = memory_dir / "history"
    written = []
    skipped = []
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    with zipfile.ZipFile(bundle_path.expanduser().resolve(), "r") as zf:
        for name in [*preview["new_files"], *preview["conflicts"]]:
            target = memory_dir / name
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                if not overwrite:
                    skipped.append(name)
                    continue
                backup = history_dir / f"pre-import-{ts}" / name
                backup.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(target, backup)
            target.write_bytes(zf.read(name))
            written.append(name)
    return {**preview, "applied": True, "written": written, "skipped": skipped}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--memory-dir", type=Path, default=DEFAULT_MEMORY_DIR)
    sub = parser.add_subparsers(dest="command", required=True)
    exp = sub.add_parser("export", help="打包导出私有记忆到桌面")
    exp.add_argument("--output", type=Path, help="输出 ZIP 路径或目录（默认桌面）")
    exp.add_argument("--project", help="仅导出指定项目文件（不含 .md 后缀）")
    imp = sub.add_parser("import", help="预览或导入记忆包")
    imp.add_argument("bundle", type=Path, help="待导入的 ZIP 记忆包路径")
    imp.add_argument("--apply", action="store_true", help="确认执行写入（默认仅预览）")
    imp.add_argument("--overwrite", action="store_true", help="允许覆盖同名文件（覆盖前自动备份到 history/）")
    args = parser.parse_args(argv)
    try:
        if args.command == "export":
            out = export_bundle(args.memory_dir, args.output, args.project)
            print(f"已导出记忆包: {out}")
        else:
            res = import_bundle(args.bundle, args.memory_dir, apply=args.apply, overwrite=args.overwrite)
            print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"错误: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())
