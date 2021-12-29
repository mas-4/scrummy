from __future__ import annotations
import os
from pathlib import Path
from typing import Any
from dataclasses import dataclass

from xdg import xdg_config_home

from scrummy.utils import parse_line

config_root: str = os.path.join(xdg_config_home(), 'scrummy')
config_file: str = os.path.join(config_root, 'scrummyrc')


@dataclass
class Config:
    """
    Config object for the scrummy application.
    """
    home: Path = Path('~/documents/scrummy').expanduser()
    todo_filename: str = 'todo.md'
    max_line_length: int = 80
    indent_size: int = 2
    date_format: str = '%Y/%m/%d'
    list_indicator: str = '-'

    __instance: Config = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Config, cls).__new__(cls)
        return cls.__instance

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


def init_config(file_to_read: str = config_file) -> Config:
    """
    Initializes the config object.

    Parameters
    ----------
    file_to_read: str
        The file to read the configuration from. Default is the scrummyrc file in $XDG_CONFIG/scrummy/.

    Returns
    -------
    Config
        The config object.
    """
    if os.path.exists(file_to_read):
        with open(file_to_read, 'rt') as f:
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


# The main config object for the application.
conf: Config = init_config()
