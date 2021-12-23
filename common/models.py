import re
from dataclasses import dataclass
from __future__ import annotations

from common import conf


class Epic:
    items: list[Todo] = []


@dataclass
class Todo:
    id: str = None
    content: str = None
    completed: bool = None
    parent: Todo | None = None

    def __init__(self, lines):
        """
        Parses a multi-line todo of the form:

        ```
        * [ ] 234-4 <content>
        ```
        Parameters
        ----------
        lines: List[str]
        """
        self.completed = bool(re.search(r'\[x]', lines[0]))
        ident = re.search(r'[\d-]+', lines[0])
        if ident:
            self.id = ident.group()
            end_of_id = ident.span()[-1]
        else:
            end_of_id = len('* [ ] ')
        self.content = ''.join([lines[0][end_of_id:], *lines[1:]]).replace('\n', '')

    @staticmethod
    def split_line(line):
        n: int = conf.max_line_length
        split_strings = [line[index: index + n] for index in range(0, len(line), n)]
        for i in range(len(split_strings[1:])):
            split_strings[i] = ' ' * len('* [ ] ') + split_strings[i]
        return '\n'.join(split_strings)

    def __str__(self):
        completed = 'x' if self.completed else ' '
        ident = self.id if self.id else ''
        return self.split_line(f'- [{completed}] {ident} {self.content}')
