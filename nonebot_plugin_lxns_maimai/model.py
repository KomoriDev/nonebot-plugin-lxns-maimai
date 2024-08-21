from sqlalchemy.orm import Mapped, mapped_column
from nonebot_plugin_orm import Model, get_session


class User(Model):

    id: Mapped[int] = mapped_column(primary_key=True)
    """用户 ID"""
    friend_code: Mapped[int]
    """好友码"""


async def bind_user(id: int, friend_code: int) -> User:
    session = get_session()
    async with session.begin():
        user = await session.get(User, id)

        if not user:
            user = User(friend_code=friend_code)
            session.add(user)

        return user
