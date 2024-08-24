from pathlib import Path

from pydantic import Field, BaseModel
from nonebot.plugin import get_plugin_config

RESOURCES_DIR: Path = Path(__file__).parent / "resources"
IMAGES_DIR: Path = RESOURCES_DIR / "images"
TEMPLATES_DIR: Path = RESOURCES_DIR / "templates"

COURSE_RANK = [
    "初学者",
    "初段",
    "二段",
    "三段",
    "四段",
    "五段",
    "六段",
    "七段",
    "八段",
    "九段",
    "十段",
    "真传",
    "真初段",
    "真二段",
    "真三段",
    "真四段",
    "真五段",
    "真六段",
    "真七段",
    "真八段",
    "真九段",
    "真十段",
    "真皆传",
    "里皆传",
]


class ScopedConfig(BaseModel):
    api_url: str = "https://maimai.lxns.net/api/v0/maimai"
    api_token: str = ""


class Config(BaseModel):
    maimai: ScopedConfig = Field(default_factory=ScopedConfig)
    """MaiMai Config"""


config = get_plugin_config(Config).maimai
