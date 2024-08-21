from pydantic import BaseModel

from .notes import Notes
from .enum import SongType, LevelIndex


class SongDifficulty(BaseModel):
    """谱面难度"""

    type: SongType
    """谱面类型"""
    difficulty: LevelIndex
    """难度"""
    level: str
    """难度等级"""
    level_value: float
    """谱面定数"""
    note_designer: str
    """谱师"""
    version: int
    """谱面首次出现版本"""
    notes: Notes | None
    """谱面物量"""


class SongDifficulties(BaseModel):
    """谱面难度"""

    standard: list[SongDifficulty]
    """曲目标准谱面难度列表"""
    dx: list[SongDifficulty]
    """曲目 DX 谱面难度列表"""


class Song(BaseModel):
    """曲目"""

    id: int
    """曲目 ID"""
    title: str
    """曲名"""
    artist: str
    """艺术家"""
    genre: str
    """曲目分类"""
    bpm: int
    """曲目 BPM"""
    version: int
    """曲目首次出现版本"""
    difficulties: SongDifficulties
    """谱面难度"""
