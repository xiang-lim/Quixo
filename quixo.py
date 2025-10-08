import random
import math


def cal_board_length(board: list):
    return int(math.sqrt(len(board)))


def check_move(board, turn, index, push_from):
    # implement your function here
    n = cal_board_length(board)
    # [1st row, 1st col, last row, last col]
    perimeter_index = (
        [j for j in range(n)]
        + [i * n for i in range(n)]
        + [(n - 1) * n + j for j in range(n)]
        + [i * n + (n - 1) for i in range(n)]
    )
    perimeter_index = sorted(set(perimeter_index))

    # not an index for a cube in the perimeter OR the cube is not mine
    if index not in perimeter_index or board[index] not in [turn, 0]:
        return False
    else:
        corner_index = [0 * n, n - 1, (n - 1) * n, (n - 1) * n + (n - 1)]
        corner_moves = [["B", "R"], ["B", "L"], ["T", "R"], ["T", "L"]]

        # check if the index is for a cube at the corner
        if index in corner_index:
            # create a dictionary of avail moves for each corner cube
            corner_moves_dict = {
                corner_index[i]: corner_moves[i] for i in range(len(corner_index))
            }
            # move is  avail for that specific corner cube
            if push_from in corner_moves_dict[index]:
                return True
            else:  # move is not avail for that specific corner cube
                return False
        else:  # in between 2 corners
            # Pick 2nd element from corner index, check if index less than, If no, pick the next larger element.
            # Case 1: less than 2nd element >> B,L,R
            if (0 < index < corner_index[1]) and push_from in ["B", "L", "R"]:
                return True

            # Case 2: less than 3rd element
            #   A: if index multiple of n means 1st col,
            #       >> T, B, R
            #   B: else last col
            #       >> T, B, L
            elif (corner_index[1] < index < corner_index[2]) and (
                (index % n == 0 and push_from in ["T", "B", "R"])
                or (index % n != 0 and push_from in ["T", "B", "L"])
            ):
                return True
            # Case 3: less than 4th aka largest element >> T,L,R
            elif (corner_index[2] < index < corner_index[3]) and push_from in [
                "T",
                "L",
                "R",
            ]:
                return True
            else:
                return False


def apply_move(board, turn, index, push_from):
    # implement your function here
    board_copy = board.copy()
    length = cal_board_length(board_copy)
    # Finds the length of each row

    if push_from == "L":
        for n in range(1, length + 1):
            if index in range(length * (n - 1), length * n):
                # Finds which row the index is in
                board_copy.pop(index)
                board_copy.insert(length * (n - 1), turn)

    elif push_from == "R":
        for n in range(1, length + 1):
            if index in range(length * (n - 1), length * n):
                board_copy.pop(index)
                board_copy.insert(length * n - 1, turn)

    elif push_from == "B":
        for n in range(1, length + 1):
            if index in range(length * (n - 1), length * n):
                count = 0
                board_copy[index] = turn
                while count < length - n:
                    # Determines the number of swaps
                    (
                        board_copy[index + length * count],
                        board_copy[index + length * (count + 1)],
                    ) = (
                        board_copy[index + length * (count + 1)],
                        board_copy[index + length * count],
                    )
                    # The swapping
                    count += 1

    elif push_from == "T":
        for n in range(1, length + 1):
            if index in range(length * (n - 1), length * n):
                count = 0
                board_copy[index] = turn
                while count < n - 1:
                    (
                        board_copy[index + length * count],
                        board_copy[index + length * (count - 1)],
                    ) = (
                        board_copy[index + length * (count - 1)],
                        board_copy[index + length * count],
                    )
                    count += 1

    return board_copy


def check_victory(board, who_played):
    # implement your function here
    dim_board = cal_board_length(board)

    player_1_score = []
    player_2_score = []

    # Check left diagonal
    left_diagonal = board[0 : len(board) : dim_board + 1]

    # Check left diagonal score
    if left_diagonal.count(1) == dim_board:
        player_1_score.append(1)

    elif left_diagonal.count(2) == dim_board:
        player_2_score.append(1)

    # Check right diagonal
    right_diagonal = board[dim_board - 1 : len(board) : dim_board - 1]

    # Check right diagonal score
    if right_diagonal.count(1) == dim_board:
        player_1_score.append(1)

    elif right_diagonal.count(2) == dim_board:
        player_2_score.append(1)

    # Check column:
    for c in range(dim_board):
        column = board[c::dim_board]

        if column.count(1) == dim_board:
            player_1_score.append(1)

        elif column.count(2) == dim_board:
            player_2_score.append(1)

    # Check row:
    for e in range(dim_board):
        row = board[e * dim_board : (e + 1) * dim_board : 1]

        if row.count(1) == dim_board:
            player_1_score.append(1)

        elif row.count(2) == dim_board:
            player_2_score.append(1)

    # Final deduction

    if who_played == 1:

        if 1 in player_2_score:
            return who_played + 1

        elif len(player_1_score) == 0 and len(player_2_score) == 0:
            return 0

        else:
            return who_played

    elif who_played == 2:

        if 1 in player_1_score:

            return who_played - 1

        elif len(player_1_score) == 0 and len(player_2_score) == 0:
            return 0

        else:
            return who_played


def computer_move(board, turn, level):
    # implement your function here
    return (0, "B")


def display_board(board):
    # implement your function here
    print("\n----------------Display Board----------------\n")
    board_length = cal_board_length(board)
    count = 0
    for x in range(len(board)):
        print(board[x], end=" ")
        count += 1

        if count % board_length == 0:
            print()
    pass


def get_user_input(input_statement):
    while True:
        try:
            return int(input(input_statement))
        except:
            print("Please enter a valid number")


def get_user_input_validate_range(list_of_options, input_statement, error_message):
    valid_input = False
    while not valid_input:
        print()  # For UI line separation
        user_input = get_user_input(input_statement)
        valid_input = user_input in range(1, len(list_of_options) + 1)
        if not valid_input:
            print(error_message)
        else:
            return user_input


def generate_options_for_display(list_of_options: list):
    display_string = ""
    for i in range(len(list_of_options)):
        display_string += "\n" + "[{0}] {1}".format(i + 1, list_of_options[i])
    return display_string + "\nEnter: "


# Basically setting player details. Computer player is associated with a
# difficulty tuple. Human players will have an empty tuple.
def initialise_player(player_num, players_detail):
    list_of_player_type = ["Human", "Computer"]
    list_of_computer_difficulty = ["Easy", "Medium", "Difficult"]
    player_type = get_user_input_validate_range(
        list_of_player_type,
        "Player {0}: Enter type of player{1}".format(
            player_num, generate_options_for_display(list_of_player_type)
        ),
        "Please enter a valid player type",
    )
    if player_type == 1:
        players_detail[player_num] = ("Human",)
    else:
        players_detail[player_num] = (
            "Computer",
            (
                get_user_input_validate_range(
                    list_of_computer_difficulty,
                    "Player {0}: Enter level of difficulty{1}".format(
                        player_num,
                        generate_options_for_display(list_of_computer_difficulty),
                    ),
                    "Please enter a valid difficulty level",
                )
            ),
        )


def menu():
    # implement your function here
    print("Quixo Game")
    valid_board_size = False
    while not valid_board_size:
        print()  # TO break line for ui
        size_of_board = get_user_input("Enter size of board: ")
        # TODO: is it valid to have a board size one? i mean the program can work but game wise feels...
        valid_board_size = size_of_board > 0
        if not valid_board_size:
            print("Please enter a valid board size")

    board = [0] * size_of_board**2
    players_detail = {}
    for player_num in range(1, 3):
        initialise_player(player_num, players_detail)
    map_of_user_input_to_board_direction = {1: "T", 2: "L", 3: "R", 4: "B"}
    list_of_push_values = list(map_of_user_input_to_board_direction.values())

    print("\nGame start!\n")
    turn = 1
    has_winner = False
    while not has_winner:
        if players_detail[turn][0] == "Human":
            # logic for human
            valid_index = False
            display_board(board)
            print ("Player {0} turn".format(turn))
            while not valid_index:
                index = get_user_input_validate_range(
                    board,
                    "Player {0}, Please select the piece you would like to move: ".format(turn),
                    "Invalid Selection: Piece select out of board range",
                )
                valid_index = board[index - 1] != turn or board[index - 1] != 0
                if not valid_index:
                    print("Invalid Selection: Piece selection is invalid.")
            valid_push = False
            while not valid_push:
                push_from = map_of_user_input_to_board_direction[
                    get_user_input_validate_range(
                        list_of_push_values,
                        "Player {0}, Please select push directions{1}".format(turn,
                            generate_options_for_display(list_of_push_values)
                        ),
                        "Invalid Selection: Select push direction within range",
                    )
                ]
                valid_push = check_move(board, turn, index, push_from)
                if not valid_push:
                    print("Move entered is invalid.")
            board = apply_move(board, turn, index, push_from)

        else:
            move = computer_move(board, turn, players_detail[player_num][0])
            print("computer don't know how to move yet :(")

        # Check victory logic
        winner = check_victory(board, turn)
        has_winner = winner != 0
        if has_winner:
            print("Winner is player {0}".format(winner))
        turn = 2 if turn == 1 else 1


if __name__ == "__main__":
    menu()
