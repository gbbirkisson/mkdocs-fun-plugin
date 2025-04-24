import subprocess
from itertools import islice
from pathlib import Path


def lines(file: str, start: int, end: int) -> str:
    with (Path(__file__).parent / file).open() as f:
        selected_lines = islice(f, start - 1, end)
        return "".join(selected_lines).strip()


def hello() -> str:
    return "world"


_refs = {
    "mcguffin": ("McGuffin", "/refs/mcguffin.md"),
}

_links = {
    "github": (":fontawesome-brands-github: Github", "https://www.github.com"),
}


def ref(key: str) -> str:
    r = _refs.get(key)
    assert r, f"No ref for '{key}' found"
    return f"[`{r[0]}`]({r[1]})"


def link(key: str) -> str:
    l = _links.get(key)
    assert l, f"No link for '{key}' found"
    return f'[{l[0]}]({l[1]}){{:target="_blank"}}'


def shell(cmd: str) -> str:
    return (
        subprocess.run(
            cmd,
            shell=True,
            check=True,
            capture_output=True,
        )
        .stdout.decode()
        .strip()
    )
