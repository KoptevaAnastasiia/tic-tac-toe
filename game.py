from results import ResultType
from typing import Callable

winner = None
game_field = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    ]
first_player = 'O'
second_player = 'X'


def print_game_field(game_field):
    print(game_field[0])
    print(game_field[1])
    print(game_field[2])
    return game_field


def input_move(current_player, number_of_moves):
    global coordinates_x, coordinates_y, coordinates
    bring = input(f"{current_player}, введіть координати x y ")
    print(bring)

    coordinates = bring.split(" ")
    coordinates_x = int(coordinates[0]) - 1
    coordinates_y = int(coordinates[1]) - 1
    print(coordinates_x, coordinates_y)
    return coordinates_x, coordinates_y


def print_game_board(board):
    for row in board:
        print("  |  ".join(row))
        print("-------------")


def check_winner(game_field, current_player):
    global winner
    if game_field[0][0] == game_field[2][0] == game_field[1][0] != ' ' or game_field[1][1] == game_field[0][1] == game_field[2][1] != " " or game_field[0][2] == game_field[1][2] == game_field[2][2] != " ":
        congratulate_player(current_player)
        winner = current_player
        return winner
    if game_field[2][0] == game_field[2][1] == game_field[2][2] != " " or game_field[1][0] == game_field[1][1] == game_field[1][2] != " " or game_field[0][0] == game_field[0][1] == game_field[0][2] != " ":
        congratulate_player(winner, current_player)
        winner = current_player
        return winner
    if game_field[2][0] == game_field[1][1] == game_field[0][2] != " " or game_field[0][0] == game_field[1][1] == game_field[2][2] != " ":
        congratulate_player(winner, current_player)
        winner = current_player
        return winner
    else:
        winner = None
        return None


def congratulate_player(current_player):
    print(current_player, "you won ^_^!")




def play(save_result: Callable[[ResultType], None]):
    player_choice = "yes"
    while player_choice == "yes":
        game_field = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        current_player = first_player
        number_of_moves = 9
        winner = None
        while number_of_moves > 0:
            input_move(current_player, number_of_moves)
            if current_player == first_player:
                current_player = second_player
            else:
                current_player = first_player
            if winner is None:
                if coordinates_x > 2 or coordinates_y > 2:
                    print("you entered the wrong coordinates")
                    continue
                if game_field[coordinates_y][coordinates_x] != " ":
                    print("this seat is already taken")
                    continue

                if game_field[coordinates_y][coordinates_x] == ' ':
                    number_of_moves = number_of_moves - 1
                    game_field[coordinates_y][coordinates_x] = current_player
                    print_game_board(game_field)
                    print(coordinates, "coordinates")
                    winner = check_winner(game_field, current_player)

            if winner is not None:
                save_result(ResultType.WIN if winner == first_player else ResultType.LOSS)
                break

        player_choice = input("again? (yes/no): ")
