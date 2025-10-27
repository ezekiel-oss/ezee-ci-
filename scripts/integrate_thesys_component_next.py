import argparse
import shutil
import zipfile
from pathlib import Path
from urllib.request import urlopen

REPO_ZIP_URL = "https://github.com/thesysdev/template-c1-component-next/archive/refs/heads/main.zip"
DOWNLOAD_ZIP = Path(".tmp_thesys_component.zip")
TMP_DIR = Path(".tmp_thesys_component_extract")

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

def download_zip(url: str, dest: Path):
    with urlopen(url) as resp:
        data = resp.read()
    dest.write_bytes(data)

def main():
    parser = argparse.ArgumentParser(description="Integrate thesysdev/template-c1-component-next into this repo")
    parser.add_argument("--dest", default=".", help="Destination directory (default: repo root)")
    parser.add_argument("--promote-to-root", action="store_true", help="Place contents into repo root (overrides --dest)")
    parser.add_argument("--url", default=REPO_ZIP_URL, help="Zip URL of the template repository")
    args = parser.parse_args()

    dest_dir = Path(".") if args.promote_to_root else Path(args.dest)

    # Prepare temp dirs
    if TMP_DIR.exists():
        shutil.rmtree(TMP_DIR)
    TMP_DIR.mkdir(parents=True, exist_ok=True)

    # Download
    print(f"Downloading template from: {args.url}")
    download_zip(args.url, DOWNLOAD_ZIP)

    # Extract
    print(f"Extracting to temp dir: {TMP_DIR}")
    with zipfile.ZipFile(DOWNLOAD_ZIP, "r") as zf:
        zf.extractall(TMP_DIR)

    # Find inner root (GitHub archive produces a single top-level folder)
    entries = [p for p in TMP_DIR.iterdir()]
    top_level_dirs = [p for p in entries if p.is_dir()]
    if len(top_level_dirs) != 1:
        raise RuntimeError("Unexpected archive layout: expected a single top-level directory")

    inner_root = top_level_dirs[0]

    # Create destination dir if not root
    if dest_dir != Path("."):
        dest_dir.mkdir(parents=True, exist_ok=True)

    # Move contents with conflict handling
    for item in inner_root.iterdir():
        move_item(item, dest_dir)

    # Cleanup
    print("Cleaning up temporary files")
    try:
        DOWNLOAD_ZIP.unlink(missing_ok=True)
    except Exception:
        pass
    shutil.rmtree(TMP_DIR)

    print(f"Template integrated into: {dest_dir.resolve()}")

if __name__ == "__main__":
    main()