There are three "almost" identical projects in this directory:

* pytest-blue-flit
* pytest-blue-hatchling
* pytest-blue-setuptools

They differ by 3 lines of `pyproject.toml`:

**flit**
```
build-system]
requires = ["flit_core >=3.2,<4"]
build-backend = "flit_core.buildapi"

[tool.flit.module]
name = "pytest_blue"
```

**hatcling**
```
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.version]
path = "src/pytest_blue/__init__.py"
```

**setuptools**
```
build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[tool.setuptools.dynamic]
version = {attr = "pytest_blue.__version__"}
```

## Building

You can build any of them with:
```
cd project
pip install build
python -m build
```

## Testing

You can test any of them (even without building) with:
```
cd project
pip install tox
tox 
```