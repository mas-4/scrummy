import re
from dataclasses import dataclass
from common import conf


@dataclass
class Todo:
    id: str
    content: str
    completed: bool

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
        self.id = ident.group()
        end_of_id = ident.span()[-1]
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
        return self.split_line(f'- [{completed}] {self.id} {self.content}')
