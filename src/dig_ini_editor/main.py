import sys
from typing import List
from . import __version__
from .arguments import create_argument_parser, Arguments, Argument
from .editor import Editor


def main(args: List[str] = sys.argv[1:]) -> None:
    parser = create_argument_parser()
    arguments = parser.parse_args(args, Arguments())

    if arguments.get_boolean(Argument.VERSION):
        print(f"{parser.prog} {__version__}")
        return

    action = arguments.get_string_optional(Argument.ACTION)
    if action is None:
        parser.error("Require action")
        return

    editor = Editor()
    filename = arguments.get_string(Argument.FILENAME)
    if filename == "-":
        if arguments.get_boolean(Argument.IN_PLACE):
            raise RuntimeError("Can not write to in place file while reading from stdin")
        with sys.stdin as stream:
            editor.read(stream)
    else:
        if arguments.get_boolean(Argument.IN_PLACE) and not arguments.get_string_optional(Argument.OUTPUT) is None:
            raise RuntimeError("Can not write to output file and in place simultaneously")
        with open(filename, mode="rt", encoding="utf-8") as stream:
            editor.read(stream)

    print(arguments)
    print(editor)
