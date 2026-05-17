"""Check Lean toolchain and run lake build."""
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    lean_path = shutil.which("lean")
    lake_path = shutil.which("lake")

    if not lean_path:
        print("Error: 'lean' not found in PATH.")
        print("Install Lean 4: https://leanprover.github.io/lean4/doc/setup.html")
        sys.exit(1)

    if not lake_path:
        print("Error: 'lake' not found in PATH.")
        print("Install Lean 4: https://leanprover.github.io/lean4/doc/setup.html")
        sys.exit(1)

    print(f"lean: {lean_path}")
    print(f"lake: {lake_path}")

    result = subprocess.run(
        ["lake", "build"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)

    if result.returncode == 0:
        print("lake build: passed")
        sys.exit(0)
    else:
        print("lake build: FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()
