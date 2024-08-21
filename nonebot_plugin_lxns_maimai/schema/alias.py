from pydantic import BaseModel


class Alias(BaseModel):
    """曲目别名"""

    song_id: int
    """曲目 ID"""
    aliases: list[int]
    """曲目所有别名"""
