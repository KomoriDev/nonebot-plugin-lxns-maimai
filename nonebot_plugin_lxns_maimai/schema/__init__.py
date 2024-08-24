from pydantic import BaseModel

from .song import Song as Song
from .alias import Alias as Alias
from .genre import Genre as Genre
from .notes import Notes as Notes
from .score import Score as Score
from .trend import Trend as Trend
from .player import Player as Player
from .version import Version as Version
from .collection import Collection as Collection
from .song import SongDifficulty as SongDifficulty
from .song import SongDifficulties as SongDifficulties
from .song import SongDifficultyUtage as SongDifficultyUtage
from .collection import CollectionRequired as CollectionRequired
from .collection import CollectionRequiredSong as CollectionRequiredSong


class RenderProps(BaseModel):
    player: Player
    standard_total: int
    dx_total: int
    standard: list[Score]
    dx: list[Score]
