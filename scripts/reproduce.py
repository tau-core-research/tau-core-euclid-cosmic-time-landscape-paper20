#!/usr/bin/env python3
"""
End-to-end reproducibility runner for Paper 20 (`tau-core-euclid-cosmic-time-landscape-paper20`):
1. Generates all 7 publication-grade figures (300 DPI) and derived data summaries.
2. Compiles `paper20_submission_source/main.tex` -> `paper20_submission_source/main.pdf`.
3. Compiles `paper20_hungarian_source/main.tex` -> `paper20_hungarian_source/main.pdf`.
4. Packages the source-only `arxiv_submission_source.zip`.
5. Runs the automated verification test suite (`pytest -q`).
"""

import os
from pathlib import Path
import shutil
import subprocess
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
TINYTEX_BIN = Path("/Users/jolcsak/Library/TinyTeX/bin/universal-darwin")


def get_env_with_latex() -> dict:
    env = os.environ.copy()
    if TINYTEX_BIN.exists():
        env["PATH"] = f"{TINYTEX_BIN}:{env.get('PATH', '')}"
    return env


def run_step(cmd: list[str], cwd: Path, env: dict) -> None:
    print(f"[reproduce] Running: {' '.join(cmd)} (in {cwd})")
    result = subprocess.run(cmd, cwd=str(cwd), env=env, check=False)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed with exit code {result.returncode}: {' '.join(cmd)}")


def compile_latex_folder(folder: Path, env: dict) -> None:
    pdflatex = shutil.which("pdflatex", path=env.get("PATH"))
    bibtex = shutil.which("bibtex", path=env.get("PATH"))
    if not pdflatex or not bibtex:
        raise RuntimeError("pdflatex or bibtex not found in PATH or TinyTeX directory.")

    run_step([pdflatex, "-interaction=nonstopmode", "-halt-on-error", "main.tex"], cwd=folder, env=env)
    run_step([bibtex, "main"], cwd=folder, env=env)
    run_step([pdflatex, "-interaction=nonstopmode", "-halt-on-error", "main.tex"], cwd=folder, env=env)
    run_step([pdflatex, "-interaction=nonstopmode", "-halt-on-error", "main.tex"], cwd=folder, env=env)


def main() -> None:
    env = get_env_with_latex()

    # 1. Generate figures and derived tables
    run_step([sys.executable, str(REPO_ROOT / "scripts" / "generate_paper20_figures_and_summaries.py")], cwd=REPO_ROOT, env=env)

    # 2. Compile English submission manuscript
    compile_latex_folder(REPO_ROOT / "paper20_submission_source", env=env)

    # 3. Compile Hungarian companion manuscript
    compile_latex_folder(REPO_ROOT / "paper20_hungarian_source", env=env)

    # 4. Build arXiv source zip
    run_step([sys.executable, str(REPO_ROOT / "scripts" / "build_arxiv_source.py")], cwd=REPO_ROOT, env=env)

    # 5. Run pytest verification suite
    run_step([sys.executable, "-m", "pytest", "-q"], cwd=REPO_ROOT, env=env)

    print("PAPER20_EUCLID_TIME_LANDSCAPE_REPRODUCTION_COMPLETE")


if __name__ == "__main__":
    main()
