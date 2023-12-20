from results.types import ResultsList, ResultType


class Leaderboard:
    def __init__(self):
        self.results: ResultsList = []

    def __get_sorted_results(self):
        sorted_by_game_count = sorted(
            self.results,
            key=lambda player: sum(player["result"].values()),
        )
        return sorted(
            sorted_by_game_count,
            key=lambda player: player["result"][ResultType.WIN.value],
            reverse=True,
        )

    def __get_divider(_):
        return "--------------------------\n"

    def __get_header(_):
        return "   Player            w l d\n"

    def __get_content(self):
        content = ""
        sorted_results = self.__get_sorted_results()
        for i in range(len(self.results)):
            results = sorted_results[i]
            results_data = " ".join(
                str(number) for number in results["result"].values()
            )
            content += f"{i+1}. {results['name'].ljust(18)}{results_data}\n"

        return content

    def print_leaderboard(self):
        if len(self.results) == 0:
            print("Leaderboard is empty")
            return
        leaderboard = self.__get_header()
        leaderboard += self.__get_divider()
        leaderboard += self.__get_content()
        leaderboard += self.__get_divider()

        print(leaderboard)
