# TODO Remove this file if not in use.

import logging

from enum import Enum

import typer

logger = logging.getLogger(__name__)


class _LogLevel(str, Enum):
    debug = "debug"
    info = "info"
    warning = "warning"
    error = "error"


app = typer.Typer(
    help="TODO Summary of what this command does.",
    add_completion=False,
    context_settings={"help_option_names": ["-h", "--help"]},
    no_args_is_help=True,
)

@app.callback()
def set_logging(log_level: _LogLevel = _LogLevel.warning):
    """Set the desired logging level for any command."""
    logging.basicConfig(level=getattr(logging, log_level.value.upper()))


@app.command()
def jump_up(
    height: int,
) -> None:
    """TODO action that this CLI command will do."""
    # TODO Call whatever function(s) with the option values.

    typer.echo("Complete")  # TODO Replace with argument output.


@app.command()
def get_down(
    height: str = "ground",
) -> None:
    """TODO action that this CLI command will do."""
    # TODO Call whatever function(s) with the argument values.

    typer.echo("Complete")  # TODO Replace with informative output.
