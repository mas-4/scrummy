"""
1. Read in todo.md.
2. All numbered done tasks are marked done in scrum/.
3. All undone tasks are kept in the new todo.md.
4. All done tasks are deleted from todo.md.
5. Everything else is ignored.
"""
from datetime import datetime
import dateutil as du
from dateutil.parser import ParserError
from pathlib import Path

from common import conf
from common.models import Todo


def parse_todofile(filename: str | Path) -> tuple[datetime|None, list[Todo]]:
    """
    Parse a todo file into a list of Todo objects.

    Parameters
    ----------
    filename: str | Path

    Returns
    -------
    tuple[datetime|None, list[Todo]]
    """
    with open(filename, 'rt') as f:
        items = f.readlines()
    current_line: list[str] = []
    is_todo: bool = False
    todos: list[Todo] = []
    is_frontmatter: bool = False
    file_date: datetime | None = None

    for line in items:
        if line.strip() == '---':
            is_frontmatter = not is_frontmatter
        elif is_frontmatter:
            pass
        elif line.startswith('#'):
            try:
                file_date = du.parser.parse(line[1:].strip())
            except ParserError:
                pass
        elif line.startswith('* [') or line.startswith('- [x]'):
            if current_line:
                todos.append(Todo(current_line))
                current_line = []
            current_line.append(line)
            is_todo = True
        elif is_todo:
            if not line.strip():
                todos.append(Todo(current_line))
                current_line = []
                is_todo = False
            else:
                current_line.append(line)
        elif line.strip():
            continue
    return file_date, todos


def rollover_todo():
    date, todos = parse_todofile(conf.todo_file)
    pass


if __name__ == '__main__':
    rollover_todo()
