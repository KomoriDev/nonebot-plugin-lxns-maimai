from enum import Enum


class FCType(str, Enum):
    """FULL COMBO 类型"""

    app = "app"
    """AP+"""
    ap = "ap"
    """AP"""
    fcp = "fcp"
    """FC+"""
    fc = "fc"
    """FC"""
