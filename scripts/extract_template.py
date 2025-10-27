import os
import shutil
import zipfile
from pathlib import Path

SRC_ZIP = Path("template-c1-next.zip")
TARGET_DIR = Path("thesys-ai")
TMP_DIR = Path(".tmp_extract")

def main():
    if not SRC_ZIP.exists():
        raise FileNotFoundError(f"Source zip not found: {SRC_ZIP}")

    if TARGET_DIR.exists():
        raise FileExistsError(f"Target directory already exists: {TARGET_DIR}")

    # Clean tmp dir if exists
    if TMP_DIR.exists():
        shutil.rmtree(TMP_DIR)

    TMP_DIR.mkdir(parents=True, exist_ok=True)

    # Extract entire zip to temp directory
    with zipfile.ZipFile(SRC_ZIP, "r") as zf:
        zf.extractall(TMP_DIR)

    # Detect if the zip has a single top-level folder
    # e.g., .tmp_extract/template-c1-next/*  => flatten it to TARGET_DIR/*
    entries = [p for p in TMP_DIR.iterdir()]
    top_level_dirs = [p for p in entries if p.is_dir()]
    top_level_files = [p for p in entries if p.is_file()]

    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    if len(top_level_dirs) == 1 and len(top_level_files) == 0:
        # Single folder at root of zip — move its contents up
        inner_root = top_level_dirs[0]
        for item in inner_root.iterdir():
            shutil.move(str(item), TARGET_DIR / item.name)
    else:
        # Multiple items at root — move them directly
        for item in entries:
            shutil.move(str(item), TARGET_DIR / item.name)

    # Clean up temp dir
    shutil.rmtree(TMP_DIR)

    print(f"Template extracted to: {TARGET_DIR.resolve()}")

if __name__ == "__main__":
    main()