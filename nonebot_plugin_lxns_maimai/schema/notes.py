from pydantic import Field, BaseModel


class Notes(BaseModel):
    """谱面数量"""

    total: int
    """总物量"""
    tap: int
    """TAP 物量"""
    hold: int
    """HOLD 物量"""
    slide: int
    """SLIDE 物量"""
    touch: int
    """TOUCH 物量"""
    break_: int = Field(alias="break")
    """BREAK 物量"""


class BuddyNotes(BaseModel):
    """仅宴会场曲目，BUDDY 谱面物量"""

    left: Notes
    """1P 谱面物量"""
    right: Notes
    """2P 谱面物量"""
