from io import BytesIO

import httpx

from ..config import config
from ..schema import Trend, Player
from ..exception import FetchUserException

url = config.api_url
token = config.api_token


class API:
    headers = {"Authorization": token}

    @classmethod
    async def get_player_info(cls, friend_code: int) -> Player | None:
        """
        通过好友码获取玩家信息。
        当好友码被绑定时，需要查分器用户开启 `allow_third_party_fetch_player` 权限。
        """
        async with httpx.AsyncClient() as client:
            info = await client.get(
                url=f"{url}/player/{friend_code}", headers=cls.headers
            )
        if info.status_code != 200:
            raise FetchUserException(info.json()["message"])
        return Player.model_validate(info.json()["data"])

    @classmethod
    async def get_rating_trend(cls, friend_code: int) -> Trend:
        """
        DX Rating 趋势
        当好友码被绑定时，需要查分器用户开启 `allow_third_party_fetch_history` 权限。
        """
        async with httpx.AsyncClient() as client:
            info = await client.get(
                url=f"{url}/player/{friend_code}/trend", headers=cls.headers
            )
        if info.status_code != 200:
            raise FetchUserException(info.json()["message"])
        return Trend.model_validate(info.json()["data"])

    @classmethod
    async def download_player_icon(cls, player: Player) -> BytesIO | bytes:
        if not player.icon:
            return BytesIO()
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://assets.lxns.net/maimai/icon/{player.icon.id}.png!webp"
            )
        return BytesIO(response.content)
