# {{cookiecutter.package_name}}

{{cookiecutter.description}}

## Development

This package uses the following tooling:

- [MyPy](https://www.mypy-lang.org/) - static type checking
- [PyTest](https://docs.pytest.org/en/stable/) - testing framework
- [pytest-cov](https://pytest-cov.readthedocs.io/) - coverage reporting
- [Ruff](https://docs.astral.sh/ruff/) - linting and formatting
- [Semantic Versioning](https://semver.org/) - `Major.Minor.Patch`
- [UV](https://docs.astral.sh/uv/) - environment management

### Setting up a development environment

1. Clone this repo and `cd` into it.
2. Create a virtual environment.
   ```shell
   uv venv
   ```
3. Activate the virtual environment.
   ```shell
   # Windows
   .venv\Scripts\Activate.ps1

   # Linux
   source .venv/bin/activate
   ```
4. Install the package in editable mode with development dependencies.
   ```shell
   uv pip install --editable ".[dev]"
   ```
5. Install [pre-commit](https://pre-commit.com/) hooks.
   ```shell
   pre-commit install
   ```

### Useful developer commands

```shell
pytest -q
ruff check --fix
ruff format
mypy src
```
