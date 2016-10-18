from enum import Enum


class Direction(Enum):
    asc = 1,
    desc = 2


class SortMode(Enum):
    auto = 1,
    alpha = 2,
    alpha_case = 3,
    num = 4


class Options(object):

    def __init__(self, count: int = None,
                 offset: int = None,
                 sort_dir: Direction = None,
                 sort_key: str = None,
                 sort_mode: SortMode = None,
                 search: str = None,
                 summarize: bool = None):
        self.count = count
        self.offset = offset
        self.sort_dir = sort_dir.name if sort_dir else None
        self.sort_key = sort_key
        self.sort_mode = sort_mode.name if sort_mode else None
        self.search = search
        self.summarize = summarize

    @property
    def dict(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}
