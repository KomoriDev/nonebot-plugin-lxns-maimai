from nonebot.compat import PYDANTIC_V2
from pydantic import BaseModel, ConfigDict

from .enum import FCType, FSType, RateType, SongType, LevelIndex


class Score(BaseModel):
    """游玩成绩"""

    id: int
    """曲目 ID"""
    song_name: str
    """仅获取 `Score` 时返回，曲名"""
    level: str
    """仅获取 `Score` 时返回，难度标级，如 `14+`"""
    level_index: LevelIndex
    """难度"""
    achievements: float
    """达成率"""
    fc: FCType | None = None
    """值可空，FULL COMBO 类型"""
    fs: FSType | None = None
    """值可空，FULL SYNC 类型"""
    dx_score: int
    """DX 分数"""
    dx_rating: float
    """仅获取 `Score` 时返回，DX Rating，计算时需要向下取整"""
    rate: RateType
    """仅获取 `Score` 时返回，评级类型"""
    type: SongType
    """谱面类型"""
    play_time: str | None = None
    """游玩的 UTC 时间，精确到分钟"""
    upload_time: str
    """仅获取 `Score` 时返回，成绩被同步时的 UTC 时间"""

    if PYDANTIC_V2:
        model_config = ConfigDict(extra="allow")  # type: ignore
    else:

        class Config:
            extra = "allow"
