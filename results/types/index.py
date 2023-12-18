from typing import TypedDict, List
from enum import Enum


class ResultType(Enum):
    WIN = "wins"
    LOSS = "losses"
    DRAW = "draws"


class PlayerResult(TypedDict):
    ResultType.WIN: int
    ResultType.LOSS: int
    ResultType.DRAW: int


class PlayerData(TypedDict):
    name: str
    result: PlayerResult


ResultsList = List[PlayerData]
