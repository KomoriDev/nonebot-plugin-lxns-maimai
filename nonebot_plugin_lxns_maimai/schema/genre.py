from pydantic import BaseModel


class Genre(BaseModel):
    """乐曲分类"""

    id: int
    """内部 ID"""
    title: str
    """分类标题"""
    genre: str
    """分类标题（日文）"""
