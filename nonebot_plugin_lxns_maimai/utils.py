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


async def calc_star_count(scores: list[Score]) -> list[int]:
    """计算 DX 分数星星数量"""

    song_list = await API.get_song_list(is_notes=True)
    song_dict = {song.id: song for song in song_list}

    matched_songs = []
    for score in scores:
        if song := song_dict.get(score.id):
            matched_songs.append((song, score))

    star_counts = []
    for song, score in matched_songs:

        difficulty = get_difficulty(song, score.type, score.level_index)

        if not difficulty or not difficulty.notes:
            star_counts.append(0)
            continue

        if isinstance(difficulty, SongDifficultyUtage):
            percentage = (
                score.dx_score / (difficulty.notes.left + difficulty.notes.right) * 3  # type: ignore
            ) * 100
        else:
            percentage = score.dx_score / (difficulty.notes.total * 3) * 100  # type: ignore

        if percentage >= 97:
            star_counts.append(5)
        elif percentage >= 95:
            star_counts.append(4)
        elif percentage >= 93:
            star_counts.append(3)
        elif percentage >= 90:
            star_counts.append(2)
        elif percentage >= 85:
            star_counts.append(1)
        else:
            star_counts.append(0)

    return star_counts
