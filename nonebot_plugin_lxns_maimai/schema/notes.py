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
