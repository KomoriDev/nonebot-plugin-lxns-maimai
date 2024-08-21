from enum import Enum


class SongType(str, Enum):
    """谱面类型"""

    standard = "standard"
    """标准谱面"""
    dx = "dx"
    """DX 谱面"""
    utage = "utage"
    """宴会场谱面"""
