import argparse
import shutil
import zipfile
from pathlib import Path

SRC_ZIP = Path("template-c1-next.zip")
TMP_DIR = Path(".tmp_extract")

def move_item(item: Path, dest_dir: Path):
    target = dest_dir / item.name
    if target.exists():
        if item.is_dir():
            backup = dest_dir / f"{item.name}.incoming"
            shutil.move(str(item), backup)
        else:
            name_lower = item.name.lower()
            if name_lower == "readme.md":
                backup = dest_dir / "README.repo.md"
                if target.exists():
                    shutil.move(str(target), backup)
                shutil.move(str(item), target)
            elif item.name == ".gitignore":
                template_ignore = dest_dir / ".gitignore.template"
                shutil.move(str(item), template_ignore)
            else:
                backup = dest_dir / f"{item.name}.incoming"
                shutil.move(str(item), backup)
    else:
        shutil.move(str(item), target)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dest", default="thesys-ai", help="Destination directory when not promoting to root")
    parser.add_argument("--promote-to-root", action="store_true", help="Extract and place contents into repo root")
    args = parser.parse_args()

    if not SRC_ZIP.exists():
        raise FileNotFoundError(f"Source zip not found: {SRC_ZIP}")

    dest_dir = Path(".") if args.promote_to_root else Path(args.dest)

    if not args.promote_to_root and dest_dir.exists():
        raise FileExistsError(f"Target directory already exists: {dest_dir}")

    if TMP_DIR.exists():
        shutil.rmtree(TMP_DIR)
    TMP_DIR.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(SRC_ZIP, "r") as zf:
        zf.extractall(TMP_DIR)

    entries = [p for p in TMP_DIR.iterdir()]
    top_level_dirs = [p for p in entries if p.is_dir()]
    top_level_files = [p for p in entries if p.is_file()]

    if not args.promote_to_root:
        dest_dir.mkdir(parents=True, exist_ok=True)

    if len(top_level_dirs) == 1 and len(top_level_files) == 0:
        inner_root = top_level_dirs[0]
        for item in inner_root.iterdir():
            move_item(item, dest_dir)
    else:
        for item in entries:
            move_item(item, dest_dir)

    shutil.rmtree(TMP_DIR)

    if args.promote_to_root:
        print(f"Template extracted and promoted to repo root: {Path('.').resolve()}")
    else:
        print(f"Template extracted to: {dest_dir.resolve()}")

if __name__ == "__main__":
    main()