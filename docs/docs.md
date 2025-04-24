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
{{lines(fun.py, 12, 13)}}
```

... and start using your functions in your docs ...

```markdown
<!-- docs.md -->
This #!hello() comes from my function!
```

... becomes ...

```markdown
This {{hello()}} comes from my function!
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
{{lines(fun.py, 6, 9)}}
```

```markdown
<!-- docs.md -->
Some awesome documentation ...

#!lines(fun.py, 2, 5)
```

... becomes ...

```markdown
Some awesome documentation ...

{{lines(fun.py, 6, 9)}}
```

### References and links

```python
# docs/fun.py
{{lines(fun.py, 15, 33)}}
```

```markdown
<!-- docs.md -->
Look at our internal #!ref(mcguffin) docs for more info. Also open up #!link(github).
```

... becomes ...

```markdown
Look at our internal {{ref(mcguffin)}} docs for more info. Also open up {{link(github)}}.
```

### Shell

```python
# docs/fun.py
{{lines(fun.py, 37, 47)}}
```

```markdown
<!-- docs.md -->
#!shell("echo hello | cowsay")
```

... becomes ...

```markdown
{{shell("echo hello | cowsay")}}
```
