from pydantic import BaseModel

from .notes import Notes, BuddyNotes
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
    notes: Notes | None = None
    """谱面物量"""


class SongDifficultyUtage(SongDifficulty):
    """宴会场曲目谱面难度"""

    kanji: str
    """谱面属性"""
    description: str
    """谱面描述"""
    is_buddy: bool
    """是否为 BUDDY 谱面"""
    notes: Notes | BuddyNotes | None = None
    """	值可空，谱面物量。is_buddy 为 true 时，notes 为 BuddyNotes。"""


class SongDifficulties(BaseModel):
    """谱面难度"""

    standard: list[SongDifficulty]
    """曲目标准谱面难度列表"""
    dx: list[SongDifficulty]
    """曲目 DX 谱面难度列表"""
    utage: list[SongDifficultyUtage] | None = None
    """可选，宴会场曲目谱面难度列表"""


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
    rights: str | None = None
    """曲目版权信息"""
    disabled: bool | None = False
    """值可空，是否被禁用，默认值为 false"""
    difficulties: SongDifficulties
    """谱面难度"""
