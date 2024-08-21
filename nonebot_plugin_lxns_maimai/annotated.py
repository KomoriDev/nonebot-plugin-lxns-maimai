from typing import Annotated

from sqlalchemy import select
from nonebot.params import Depends
from nonebot_plugin_orm import SQLDepends

from .depends import get_user_id
from .model import User as _User

UserInfo = Annotated[
    _User, SQLDepends(select(_User).where(_User.id == Depends(get_user_id)))
]
