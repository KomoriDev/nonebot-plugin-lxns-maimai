from pydantic import BaseModel


class Trend(BaseModel):
    """DX Rating 趋势"""

    total: int
    """总 DX Rating"""
    standard: int
    """旧版本谱面总 DX Rating"""
    dx: int
    """现版本谱面总 DX Rating"""
    date: str
    """日期"""
