from nonebot_plugin_user import UserSession, get_user_by_id


async def get_user_id(user_session: UserSession) -> int:
    return (await get_user_by_id(user_session.user_id)).id
