from enum import Enum


class FSType(str, Enum):
    """FULL SYNC 类型"""

    fsdp = "FSD+"
    """FSD+"""
    fsd = "FSD"
    """FSD"""
    fsp = "FS+"
    """FS+"""
    fs = "FS"
    """FS"""
