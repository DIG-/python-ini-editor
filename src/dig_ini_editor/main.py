import sys
from typing import List
from . import __version__
from .arguments import create_argument_parser, Arguments, Argument


def main(args: List[str] = sys.argv[1:]) -> None:
    parser = create_argument_parser()
    arguments = parser.parse_args(args, Arguments())

    if arguments.get_boolean(Argument.VERSION):
        print(f"{parser.prog} {__version__}")
        return

    print(arguments)
