from .apis import API
from .schema.enum import SongType, LevelIndex
from .schema import Song, Score, SongDifficulty, SongDifficultyUtage


def get_difficulty(
    song: Song, type: SongType, level_index: LevelIndex
) -> SongDifficulty | SongDifficultyUtage | None:
    if type == SongType.utage and song.difficulties.utage:
        return song.difficulties.utage[level_index.value]
    elif type == SongType.standard:
        return song.difficulties.standard[level_index.value]
    elif type == SongType.dx:
        return song.difficulties.dx[level_index.value]
    else:
        return None


async def calc_star_count(score: Score) -> int | None:
    """计算 DX 分数星星数量"""

    song = await API.get_song_info(score.id)
    difficulty = get_difficulty(song, score.type, score.level_index)

    if not difficulty or not difficulty.notes:
        return None

    if isinstance(difficulty, SongDifficultyUtage):
        percentage = (
            score.dx_score / (difficulty.notes.left + difficulty.notes.right) * 3  # type: ignore
        ) * 100
    else:
        percentage = score.dx_score / (difficulty.notes.total * 3) * 100  # type: ignore

    if percentage >= 97:
        return 5
    elif percentage >= 95:
        return 4
    elif percentage >= 93:
        return 3
    elif percentage >= 90:
        return 2
    elif percentage >= 85:
        return 1
    else:
        return 0
