import os
from pathlib import Path
from typing import Tuple, Any
from dataclasses import dataclass

from xdg import xdg_config_home

config_root: str = os.path.join(xdg_config_home(), 'scrummy')
config_file: str = os.path.join(config_root, '.scrummyrc')


@dataclass
class Config:
    """
    Config object for the scrummy application.
    """
    home: Path = Path('~/documents/scrummy').expanduser()
    todo_filename: str = 'todo.md'
    max_line_length: int = 80

    def __getitem__(self, key: str) -> Any:
        return getattr(self, key)

    def __setitem__(self, key: Any, value: Any):
        if hasattr(self, key):
            setattr(self, key, value)
        else:
            raise KeyError(f'{key} is not a valid configuration key.')

    @property
    def todo_file(self) -> str:
        return os.path.join(self.home, self.todo_filename)


def parse_line(line: str) -> Tuple[str, Any] | None:
    """
    Parses a line from the config file.

    Parameters
    ----------
    line: str

    Returns
    -------
    Tuple[str, Any]
        The key and value of the line.
    """
    if line.startswith('#'):
        return None
    if '=' not in line:
        return None
    key, value = line.split('=', 1)
    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1]
    if '~' in value:
        value = str(Path(value).expanduser())
    return key, value.strip()


def init_config() -> Config:
    """
    Initializes the config object.

    Returns
    -------
    Config
        The config object.
    """
    if os.path.exists(config_file):
        with open(config_file, 'rt') as f:
            data = f.readlines()
    else:
        return Config()
    config = Config()
    for line in data:
        try:
            key, val = parse_line(line)
            config[key] = val
        except TypeError:
            pass
    return config