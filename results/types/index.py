from typing import List
from enum import Enum


class ResultType(Enum):
    WIN = "wins"
    LOSS = "losses"
    DRAW = "draws"


class PlayerResult:
    ResultType.WIN: int
    ResultType.LOSS: int
    ResultType.DRAW: int


class PlayerData:
    name: str
    result: PlayerResult


ResultsList = List[PlayerData]
