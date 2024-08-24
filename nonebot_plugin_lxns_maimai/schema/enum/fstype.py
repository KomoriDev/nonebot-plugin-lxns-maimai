from enum import Enum


class FSType(str, Enum):
    """FULL SYNC 类型"""

    fsdp = "fsdp"
    """FSD+"""
    fsd = "fsd"
    """FSD"""
    fsp = "fsp"
    """FS+"""
    fs = "fs"
    """FS"""
    sync = "sync"
