from configparser import ConfigParser
from typing import TextIO

__all__ = ["Editor"]


class Editor:
    def __init__(self) -> None:
        self._config = ConfigParser()

    def __repr__(self) -> str:
        return f"Editor(config={self._config})"

    def read(self, stream: TextIO) -> None:
        self._config.read_file(stream)

    def write(self, stream: TextIO) -> None:
        self._config.write(stream)
