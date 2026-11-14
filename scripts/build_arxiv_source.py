#!/usr/bin/env python3
"""
Builds the clean source-only arXiv submission archive (`arxiv_submission_source.zip`)
for Paper 20 from `paper20_submission_source/`, strictly excluding compiled PDFs
and LaTeX auxiliary files (.aux, .log, .out, .toc, .blg).
"""

from pathlib import Path
import zipfile

REPO_ROOT = Path(__file__).resolve().parent.parent
SUBMISSION_DIR = REPO_ROOT / "paper20_submission_source"
OUTPUT_ZIP = REPO_ROOT / "arxiv_submission_source.zip"

EXCLUDED_EXTENSIONS = {".pdf", ".aux", ".log", ".out", ".toc", ".blg", ".synctex.gz", ".fls", ".fdb_latexmk"}


def build_arxiv_zip() -> Path:
    if not SUBMISSION_DIR.exists():
        raise FileNotFoundError(f"Missing submission directory: {SUBMISSION_DIR}")

    with zipfile.ZipFile(OUTPUT_ZIP, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(SUBMISSION_DIR.rglob("*")):
            if not file_path.is_file():
                continue
            if file_path.name.startswith("."):
                continue
            if file_path.suffix.lower() in EXCLUDED_EXTENSIONS:
                continue
            rel_path = file_path.relative_to(SUBMISSION_DIR)
            zf.write(file_path, arcname=str(rel_path))

    print(f"Built source-only arXiv package: {OUTPUT_ZIP} ({OUTPUT_ZIP.stat().st_size:,} bytes)")
    return OUTPUT_ZIP


if __name__ == "__main__":
    build_arxiv_zip()
