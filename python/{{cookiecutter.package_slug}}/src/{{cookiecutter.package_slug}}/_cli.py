# TODO Remove this file if not in use.

import argparse
import logging
from typing import Optional

logger = logging.getLogger(__name__)


def _parse_arguments(args_list: Optional[list[str]]=None) -> argparse.Namespace:
    """Create an ArgParser and parse the given argument values."""
    parser = argparse.ArgumentParser(
        description="TODO Summary of what this command does.",
    )

    # TODO Add any arguments necessary for your command.

    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument(
        "--info",
        help="Set logging level to INFO.",
        action="store_const",
        const=logging.INFO,
        dest="logging_level",
    )
    verbosity.add_argument(
        "--debug",
        help="Set logging level to DEBUG.",
        action="store_const",
        const=logging.DEBUG,
        dest="logging_level",
    )

    args = parser.parse_args(args_list)
    # args, extra_args = parser.parse_known_args(args_list)

    logging.basicConfig(level=args.logging_level)
    logger.debug("Parsed Arguments:\n\t%s", vars(args))

    return args


def run_example(args_list: Optional[list[str]]=None):
    """Execute the 'example' command."""
    args = _parse_arguments(args_list=args_list)

    # TODO Call whatever function(s) with the argument values from the args namespace.

    print(args)  # TODO Remove this line.
