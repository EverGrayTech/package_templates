# TODO Remove this file if not in use.

# Imports

import json
import logging
from importlib.resources import files

# Globals

logger = logging.getLogger(__name__)


# Classes

class Example:
    """Description of this class."""

    def __repr__(self):
        package = ".".join(self.__module__.split(".")[:2])
        return f"<{package}.{self.__class__.__name__}: at {hex(id(self))}>"


# Functions

def get_example_data() -> dict:
    """Read the example package data."""
    return json.loads(files("{{cookiecutter.package_slug}}._data").joinpath("example.json").read_text())
