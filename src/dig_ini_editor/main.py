import sys
from typing import List
from .arguments import create_argument_parser


def main(args: List[str] = sys.argv[1:]) -> None:
    arguments = create_argument_parser().parse_args(args)
    print(arguments)
