import asyncio

from nonebot_plugin_htmlrender import template_to_pic

from .schema import RenderProps
from .config import TEMPLATES_DIR
from .utils import calc_star_count
from .filters import star_count_to_color, level_index_to_color


async def render_b50(props: RenderProps) -> bytes:
    tasks = [calc_star_count(score) for score in props.standard + props.dx]
    star_counts = await asyncio.gather(*tasks)

    for score, star_count in zip(props.standard + props.dx, star_counts):
        score.star_count = star_count

    return await template_to_pic(
        template_path=str(TEMPLATES_DIR),
        template_name="best50.html.jinja2",
        templates={"standard": props.standard, "dx": props.dx},
        filters={
            "level_index_to_color": level_index_to_color,
            "star_count_to_color": star_count_to_color,
        },
        pages={
            "viewport": {"width": 1080, "height": 1512},
            "base_url": f"file://{TEMPLATES_DIR}",
        },
    )
