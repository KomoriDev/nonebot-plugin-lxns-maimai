from pathlib import Path

from pydantic import Field, BaseModel
from nonebot.plugin import get_plugin_config

RESOURCES_DIR: Path = Path(__file__).parent / "resources"
IMAGES_DIR: Path = RESOURCES_DIR / "images"
TEMPLATES_DIR: Path = RESOURCES_DIR / "templates"


class ScopedConfig(BaseModel):
    api_url: str = "https://maimai.lxns.net/api/v0/maimai"
    api_token: str = ""


class Config(BaseModel):
    maimai: ScopedConfig = Field(default_factory=ScopedConfig)
    """MaiMai Config"""


config = get_plugin_config(Config).maimai
