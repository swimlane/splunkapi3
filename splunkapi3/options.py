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
    def __init__(self, count: int = 30, offset: int = 0, sort_dir: Direction = Direction.asc,
                 sort_key: str = 'name', sort_mode: SortMode = SortMode.auto, search: str = None,
                 summarize: bool = False):
        self.count = count
        self.offset = offset
        self.sort_dir = sort_dir.name
        self.sort_key = sort_key
        self.sort_mode = sort_mode.name
        self.search = search
        self.summarize = summarize
