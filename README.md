<h1>
  <p align="center">
    <a href="https://github.com/gbbirkisson/mkdocs-fun-plugin">
      <img src="logo.png" alt="Logo" height="128">
    </a>
    <br>mkdocs-fun-plugin
  </p>
</h1>

<p align="center">
  Dead simple custom python <b>fun</b>ctions with <b>mkdocs</b>
</p>

<!-- vim-markdown-toc GFM -->

* [Usage 📖](#usage-)
* [Configuration 🎛](#configuration-)
* [Examples 💡](#examples-)
  * [Reusable components](#reusable-components)
  * [References and links](#references-and-links)
  * [Shell](#shell)

<!-- vim-markdown-toc -->

## Usage 📖

Install the plugin in your project ...

```bash
pip install TODO
```

... add it to your mkdocs configuration ...

```yaml
# mkdocs.yaml
plugins:
  - fun
```

... create a `docs/fun.py` file ...

```python
# docs/fun.py
def hello() -> str:
    return "world"
```

... and start using your functions in your docs ...

```markdown
<!-- docs.md -->
This #!hello() comes from my function!
```

... becomes ...

```markdown
This world comes from my function!
```

## Configuration 🎛

You can customize the plugin behaviour with configuration:

```yaml
# mkdocs.yaml
plugins:
  - fun:
      pattern: "#!(?P<func>[^\(]+)\((?P<params>[^\)]*)\)"  # Regex to match functions
      module: fun.py  # Filename for your functions
```

## Examples 💡

### Reusable components

```python
# docs/fun.py
def lines(file: str, start: int, end: int) -> str:
    with (Path(__file__).parent / file).open() as f:
        selected_lines = islice(f, start - 1, end)
        return "".join(selected_lines).strip()
```

```markdown
<!-- docs.md -->
Some awesome documentation ...

#!lines(fun.py, 2, 5)
```

... becomes ...

```markdown
Some awesome documentation ...

def lines(file: str, start: int, end: int) -> str:
    with (Path(__file__).parent / file).open() as f:
        selected_lines = islice(f, start - 1, end)
        return "".join(selected_lines).strip()
```

### References and links

```python
# docs/fun.py
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
```

```markdown
<!-- docs.md -->
Look at our internal #!ref(mcguffin) docs for more info. Also open up #!link(github).
```

... becomes ...

```markdown
Look at our internal [`McGuffin`](/refs/mcguffin.md) docs for more info. Also open up [:fontawesome-brands-github: Github](https://www.github.com){:target="_blank"}.
```

### Shell

```python
# docs/fun.py
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
```

```markdown
<!-- docs.md -->
#!shell("echo hello | cowsay")
```

... becomes ...

```markdown
_______
< hello >
 -------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```
