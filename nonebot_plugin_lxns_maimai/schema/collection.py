from pydantic import BaseModel

from .enum import FCType, FSType, RateType, SongType


class CollectionGenre(BaseModel):
    """收藏品分类"""

    id: int
    """收藏品分类 ID"""
    title: str
    """分类标题"""
    genre: str
    """分类标题（日文）"""


class CollectionRequiredSong(BaseModel):
    """收藏品要求曲目"""

    id: int
    """曲目 ID"""
    title: str
    """曲名"""
    type: SongType
    """谱面类型"""
    completed: bool | None = None
    """值可空，要求的曲目是否完成"""
    completed_difficulties: list[int] | None = None
    """值可空，已完成的难度"""


class CollectionRequired(BaseModel):
    """收藏品要求"""

    difficulties: list[int] | None = None
    """	值可空，要求的谱面难度"""
    rate: RateType | None = None
    """	值可空，要求的评级类型"""
    fc: FCType | None = None
    """	值可空，要求的 FULL COMBO 类型"""
    fs: FSType | None = None
    """	值可空，要求的 FULL SYNC 类型"""
    songs: list[CollectionRequiredSong] | None = None
    """	值可空，要求的曲目"""
    completed: bool | None = None
    """值可空，要求是否全部完成"""


class Collection(BaseModel):
    """收藏品"""

    id: int
    """收藏品 ID"""
    name: str
    """收藏品名称"""
    color: str | None = None
    """值可空，仅玩家称号，称号颜色"""
    description: str | None = None
    """收藏品说明"""
    genre: str | None = None
    """值可空，除玩家称号，收藏品分类（日文）"""
    required: list[CollectionRequired] | None = None
    """值可空，收藏品要求"""
