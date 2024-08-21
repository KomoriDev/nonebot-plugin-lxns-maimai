from enum import Enum


class FCType(str, Enum):
    """FULL COMBO 类型"""

    app = "AP+"
    """AP+"""
    ap = "AP"
    """AP"""
    fcp = "FC+"
    """FC+"""
    fc = "FC"
    """FC"""
