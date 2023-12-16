from typing import Callable


class PlayersGreeter:
    def __init__(self):
        self.first_player: str
        self.second_player: str
        self.is_new_player: Callable[[str], bool]

    def __greet_new_player(self, username: str):
        print(f"Hi, {username} good luck")

    def __greet_old_player(self, username: str):
        print(f"Hi, {username} nice to see you again")

    def greet_users(self):
        if self.is_new_player(self.first_player):
            self.__greet_new_player(self.first_player)
        else:
            self.__greet_old_player(self.first_player)

        if self.is_new_player(self.second_player):
            self.__greet_new_player(self.second_player)
        else:
            self.__greet_old_player(self.second_player)

    def fill_users_data(self):
        self.first_player = input("Enter first player name: ")
        self.second_player = input("Enter second player name: ")

        while self.first_player == self.second_player:
            print("Name already taken")
            self.second_player = input("Enter second player name: ")
