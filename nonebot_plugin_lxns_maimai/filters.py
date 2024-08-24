from .config import COURSE_RANK
from .schema.enum import LevelIndex


def level_index_to_color(level_index: LevelIndex) -> tuple[str, str]:
    match level_index:
        case LevelIndex.BASIC:
            return "#E1FFE9", "#00FF4430"
        case LevelIndex.ADVANCED:
            return "#FFF7E1", "#FBFF0030"
        case LevelIndex.EXPERT:
            return "#FFE1E1", "#FF000030"
        case LevelIndex.MASTER:
            return "#E7E1FF", "#A100FF30"
        case LevelIndex.RE_MASTER:
            return "#F0F0F0", "#80808030"
        case _:
            return "#E1FFE9", "#00FF4430"


def star_count_to_color(count: int):
    if count == 1 or count == 2:
        return "#25FF00", "#0DFF00"
    elif count == 3 or count == 4:
        return "#FF5100", "#FF0000"
    else:
        return "#FFCF00", "#FFFB00"


def course_rank_id_to_text(course_rank: int) -> str:
    return COURSE_RANK[course_rank]
