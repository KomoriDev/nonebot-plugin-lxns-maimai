from nonebot_plugin_htmlrender import template_to_pic

from .config import TEMPLATES_DIR


async def render_b50() -> bytes:

    return await template_to_pic(
        template_path=str(TEMPLATES_DIR),
        template_name="best50.html.jinja2",
        templates={},
        pages={
            "viewport": {"width": 1080, "height": 1512},
            "base_url": f"file://{TEMPLATES_DIR}",
        },
    )
