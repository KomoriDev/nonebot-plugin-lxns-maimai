from pydantic import BaseModel

from .collection import Collection


class Player(BaseModel):
    """玩家"""

    name: str
    """游戏内名称"""
    rating: int
    """玩家 DX Rating"""
    friend_code: int
    """好友码"""
    trophy: Collection
    """仅[获取玩家信息](https://maimai.lxns.net/docs/api/maimai#get-apiv0maimaiplayerfriend_code)返回，称号"""
    trophy_name: str | None = None
    """仅[创建玩家信息](https://maimai.lxns.net/docs/api/maimai#post-apiv0maimaiplayer)必选，称号"""
    course_rank: int
    """段位 ID"""
    class_rank: int
    """阶级 ID"""
    star: int
    """搭档觉醒数"""
    icon: Collection | None = None
    """值可空，头像"""
    name_plate: Collection | None = None
    """值可空，姓名框"""
    frame: Collection | None = None
    """值可空，背景"""
    upload_time: str
    """
    仅[获取玩家信息](https://maimai.lxns.net/docs/api/maimai#get-apiv0maimaiplayerfriend_code)返回，
    玩家被同步时的 UTC 时间
    """
