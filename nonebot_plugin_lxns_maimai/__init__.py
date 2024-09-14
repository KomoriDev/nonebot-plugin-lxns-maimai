import httpx
from nonebot import require
from nonebot.rule import Rule
from nonebot.log import logger
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

require("nonebot_plugin_orm")
require("nonebot_plugin_user")
require("nonebot_plugin_waiter")
require("nonebot_plugin_alconna")
require("nonebot_plugin_htmlrender")
from nonebot_plugin_waiter import prompt
from nonebot_plugin_user import UserSession
from nonebot_plugin_orm import async_scoped_session
from nonebot_plugin_alconna.uniseg import Button, UniMessage, FallbackStrategy
from nonebot_plugin_alconna import Args, Match, Option, Alconna, CommandMeta, on_alconna

from .apis import API
from . import migrations
from .render import render_b50
from .schema import RenderProps
from .config import Config, config
from .model import User, bind_user
from .exception import FetchUserException

__plugin_meta__ = PluginMetadata(
    name="maimai DX 查分",
    description="maimai DX 查分插件",
    usage="/m b50",
    type="application",
    homepage="https://github.com/KomoriDev/nonebot-plugin-lxns-maimai",
    config=Config,
    supported_adapters=inherit_supported_adapters(
        "nonebot_plugin_alconna", "nonebot_plugin_user"
    ),
    extra={
        "unique_name": "maimai dx",
        "orm_version_location": migrations,
        "author": "Komorebi <mute231010@gmail.com>",
        "version": "0.1.2",
    },
)


if not config.api_token:
    logger.warning("缺失必要配置项，已禁用该插件")


def is_enable() -> Rule:

    def _rule() -> bool:
        return bool(config.api_token)

    return Rule(_rule)


mai = on_alconna(
    Alconna(
        "mai",
        Option("bind", Args["friend_code?#好友码", int], help_text="绑定好友码"),
        Option("best50", alias={"b50"}, help_text="查询 Best50"),
        meta=CommandMeta(
            description="maimai DX 查分",
            usage=__plugin_meta__.usage,
            example="/mai bind 123456; /mai b50",
            compact=True,
        ),
    ),
    rule=is_enable(),
    aliases={"m", "maimai"},
    use_cmd_start=True,
)


@mai.assign("bind")
async def _(friend_code: Match[int], user_session: UserSession):
    if friend_code.available:
        result = friend_code.result
    else:
        result = await prompt("请输入好友码", timeout=30)
        if result is None:
            await (
                UniMessage.text("等待超时")
                .keyboard(Button("input", label="重试", text="/mai bind"))
                .finish(at_sender=True, fallback=FallbackStrategy.ignore)
            )
        result = result.extract_plain_text()
    try:
        player = await API.get_player_info(int(result))
        await bind_user(user_session.user_id, player.friend_code)
        await (
            UniMessage.text(f"绑定成功！欢迎 {player.name}")
            .keyboard(Button("input", label="查询 Best50", text="/mai b50"))
            .finish(at_sender=True, fallback=FallbackStrategy.ignore)
        )
    except FetchUserException as e:
        await (
            UniMessage.text(f"绑定失败: {str(e)}")
            .keyboard(Button("input", label="重试", text="/mai bind"))
            .finish(at_sender=True, fallback=FallbackStrategy.ignore)
        )


@mai.assign("best50")
async def _(db_session: async_scoped_session, user_session: UserSession):
    user = await db_session.get(User, user_session.user_id)
    if user is None:
        await (
            UniMessage.text("暂未绑定 maimai DX 查分器账号。")
            .text("使用 /mai bind 命令进行绑定")
            .keyboard(Button("input", label="Bind", text="/mai bind"))
            .finish(at_sender=True, fallback=FallbackStrategy.ignore)
        )
    try:
        standard_total, dx_total, standard, dx = await API.get_bests(user.friend_code)
        player = await API.get_player_info(user.friend_code)
        props = RenderProps(
            player=player,
            standard_total=standard_total,
            dx_total=dx_total,
            standard=standard,
            dx=dx,
        )
        await UniMessage.image(raw=await render_b50(props)).finish(at_sender=True)
    except FetchUserException as e:
        await (
            UniMessage.text(f"Best 50 查询失败: {str(e)}")
            .keyboard(Button("input", label="重试", text="/mai b50"))
            .finish(at_sender=True, fallback=FallbackStrategy.ignore)
        )
    except httpx.ConnectError:
        await (
            UniMessage.text("Best 50 查询失败: 网络超时，请稍后再试")
            .keyboard(Button("input", label="重试", text="/mai b50"))
            .finish(at_sender=True, fallback=FallbackStrategy.ignore)
        )
