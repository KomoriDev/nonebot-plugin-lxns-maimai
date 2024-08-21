from enum import Enum


class LevelIndex(Enum):
    """难度"""

    BASIC = 0
    ADVANCED = 1
    EXPERT = 2
    MASTER = 3
    RE_MASTER = 4

    @classmethod
    def get_level(cls, index: int):
        for level in LevelIndex:
            if level.value == index:
                return level.name
        raise ValueError("Invalid value")
