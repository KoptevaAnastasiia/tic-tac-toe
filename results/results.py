from results.types import ResultsList
from .utils import FileHelper, SaveGameResults, PlayersGreeter, Leaderboard


class GameResults(PlayersGreeter, FileHelper, Leaderboard, SaveGameResults):
    def __init__(self):
        self.first_player: str
        self.second_player: str
        self.results: ResultsList

        FileHelper.__init__(self)
        PlayersGreeter.__init__(self)
        Leaderboard.__init__(self)
        SaveGameResults.__init__(self)

    def init(self):
        self.fill_results_data()
        self.fill_users_data()
        self.greet_users()

    def leaderboard(self):
        self.fill_results_data()
        self.print_leaderboard()

    def clear(self):
        self.clear_results_data()
        print("Leaderboard cleared")
