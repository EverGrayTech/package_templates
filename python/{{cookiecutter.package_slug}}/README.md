# {{cookiecutter.package_name}}

{{cookiecutter.description}}

## Development

1. Clone this repo and `cd` into it.
2. Create a virtual environment.
   ```shell
   python -m venv venv --upgrade-deps
   ```
3. Activate the virtual environment. 
   ```shell
   # Windows
   venv\Scripts\Activate.ps1

   # Linux
   source venv/bin/activate
   ```
4. Build and install the package in editable mode, and install the extra dev dependencies.
   ```shell
   pip install --editable ".[dev]"
   ```
5. Install [pre-commit](https://pre-commit.com/) hooks.
   ```shell
   pre-commit install
   ```

### Code Style

This package uses [Ruff](https://docs.astral.sh/ruff/) to lint and format code.

Run `ruff check --fix ; ruff format` prior to every commit.
Once installed, the pre-commit hooks do this automatically.

### Versions

This package follows [Semantic Versioning](https://semver.org/).

`Major.Minor.Patch`

To bump the version, edit [`setup.cfg`](setup.cfg#L4), then `pip install -e .`.
