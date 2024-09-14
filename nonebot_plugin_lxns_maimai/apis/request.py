from io import BytesIO

import httpx

from ..config import config
from ..exception import FetchUserException
from ..schema import Song, Score, Trend, Player

url = config.api_url
token = config.api_token


class API:
    headers = {"Authorization": token}

    @classmethod
    async def get_player_info(cls, friend_code: int) -> Player:
        """
        通过好友码获取玩家信息。
        当好友码被绑定时，需要查分器用户开启 `allow_third_party_fetch_player` 权限。
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url=f"{url}/player/{friend_code}", headers=cls.headers
            )
        if response.status_code != 200:
            raise FetchUserException(response.json()["message"])
        return Player(**response.json()["data"])

    @classmethod
    async def get_rating_trend(cls, friend_code: int) -> Trend:
        """
        DX Rating 趋势
        当好友码被绑定时，需要查分器用户开启 `allow_third_party_fetch_history` 权限。
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url=f"{url}/player/{friend_code}/trend", headers=cls.headers
            )
        if response.status_code != 200:
            raise FetchUserException(response.json()["message"])
        return Trend(**response.json()["data"])

    @classmethod
    async def get_bests(
        cls, friend_code: int
    ) -> tuple[int, int, list[Score], list[Score]]:
        """
        获取玩家缓存的 Best50
        Args:
            friend_code: 好友码

        Returns:
            standard_total: 旧版本谱面 Best 35 总分
            dx_total: 现版本谱面 Best 15 总分
            standard: 旧版本谱面 Best 35 列表
            dx: 现版本谱面 Best 15 列表
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(
                url=f"{url}/player/{friend_code}/bests", headers=cls.headers
            )
        if response.status_code != 200:
            raise FetchUserException(response.json()["message"])
        data = response.json()["data"]
        standard_scores = [Score(**score) for score in data["standard"]]
        dx_scores = [Score(**score) for score in data["dx"]]
        return data["standard_total"], data["dx_total"], standard_scores, dx_scores

    @classmethod
    async def get_song_info(cls, song_id: int) -> Song:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{url}/song/{song_id}")
        return Song(**response.json())

    @classmethod
    async def download_player_icon(cls, player: Player) -> BytesIO | bytes:
        if not player.icon:
            return BytesIO()
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://assets.lxns.net/maimai/icon/{player.icon.id}.png!webp"
            )
        return BytesIO(response.content)
