import game
from results import GameResults


class App:
    def __init__(self):
        self.player_results = GameResults()

    def __ask_command(self):
        command = input("Enter command: ")

        if command == "play":
            self.player_results.init()
            game.play(self.player_results.add_game_result)

        elif command == "leaderboard":
            self.player_results.leaderboard()

        elif command == "clear":
            self.player_results.clear()

        elif command == "exit":
            exit()

        else:
            print("Unknown command (play/leaderboard/clear/exit)")

    def launch(self):
        while True:
            self.__ask_command()


app = App()
app.launch()
