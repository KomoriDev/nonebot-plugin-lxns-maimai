from pydantic import BaseModel


class Version(BaseModel):
    """曲目版本"""

    id: int
    """内部 ID"""
    title: str
    """版本标题"""
    version: int
    """主要版本 ID"""
