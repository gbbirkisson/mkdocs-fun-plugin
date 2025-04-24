import argparse
import re
import sys
from pathlib import Path

from mkdocs_fun_plugin.plugin import _Executor

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("module")
    parser.add_argument("pattern")
    args = parser.parse_args()
    e = _Executor(module=Path(args.module), pattern=re.compile(args.pattern))
    for line in sys.stdin:
        print(e(line), end="")  # noqa: T201
