from typing import Callable
from results.types import ResultsList, ResultType


class SaveGameResults:
    def __init__(self):
        self.first_player: str
        self.second_player: str
        self.results: ResultsList = []
        self.is_new_player: Callable[[str], bool]
        self.save_results_data: Callable[[], None]

    def is_new_player(self, username: str) -> bool:
        for player in self.results:
            if player["name"] == username:
                return False
        return True

    def __add_player_result(self, username: str, result_type: ResultType):
        is_new_player = self.is_new_player(username)

        if is_new_player:
            new_result = {r.value: 0 for r in ResultType}
            new_result[result_type.value] += 1

            self.results.append(
                {
                    "name": username,
                    "result": new_result,
                }
            )
        else:
            for player in self.results:
                if player["name"] == username:
                    player["result"][result_type.value] += 1
                    return

    def __add_first_player_result(self, result_type: ResultType):
        self.__add_player_result(self.first_player, result_type)

    def __add_second_player_result(self, result_type: ResultType):
        self.__add_player_result(self.second_player, result_type)

    def add_game_result(self, first_player_result: ResultType):
        if first_player_result == ResultType.WIN:
            self.__add_first_player_result(ResultType.WIN)
            self.__add_second_player_result(ResultType.LOSS)

        if first_player_result == ResultType.LOSS:
            self.__add_first_player_result(ResultType.LOSS)
            self.__add_second_player_result(ResultType.WIN)

        if first_player_result == ResultType.DRAW:
            self.__add_first_player_result(ResultType.DRAW)
            self.__add_second_player_result(ResultType.DRAW)

        self.save_results_data()
