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
                # Removes the object in the chosen index
                board_copy.insert(length * (n - 1), turn)
                # Inserts the turn value from the left
                
    elif push_from == "R":
        for n in range(1, length + 1):
            if index in range(length * (n - 1), length * n):
                board_copy.pop(index)
                board_copy.insert(length * n - 1, turn)
                # Inserts the turn value from the right
                
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
                    # The swapping of the index towards the bottom
                    count += 1

    elif push_from == "T":
        for n in range(1, length + 1):
            if index in range(length * (n - 1), length * n):
                count = 0
                board_copy[index] = turn
                while count < n - 1:
                    (
                        board_copy[index - length * count],
                        board_copy[index - length * (count + 1)],
                    ) = (
                        board_copy[index - length * (count + 1)],
                        board_copy[index - length * count],
                    )
                    # The swapping of the index towards the top
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
    right_diagonal = board[dim_board - 1 : dim_board**(2) -dim_board+1 : dim_board - 1]

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
            return 2

        elif len(player_1_score) == 0 and len(player_2_score) == 0:
            return 0

        else:
            return who_played

    elif who_played == 2:

        if 1 in player_1_score:

            return 1

        elif len(player_1_score) == 0 and len(player_2_score) == 0:
            return 0

        else:
            return who_played

# Function to filter list of valid parameters
def filter_list_of_perimeter_index(board, turn):
    # Get perimeter
    board_length = cal_board_length(board)
    list_of_perimeter_index = list(range(board_length)) + list(
        range(len(board) - board_length, len(board))
    )
    # left perimeter is c * n right side is c*n + n -1 ignore first and last row
    for c in range(1, board_length - 1):
        list_of_perimeter_index += [
            c * board_length,
            c * board_length + board_length - 1,
        ]
    # Filtering index
    list_of_perimeter_index = [
        value
        for value in list_of_perimeter_index
        if board[value] == turn or board[value] == 0
    ]
    return list_of_perimeter_index

#Filter valid pushes based on direction and whether the index can be chosen
def get_valid_push_directions(board, turn):
    filtered_list_of_board_perimeter_index = filter_list_of_perimeter_index(board,turn)
    list_of_directions = ["T", "B", "L", "R"]
    list_of_valid_push_directions = []
    # Create tuple of index and direction
    for index in filtered_list_of_board_perimeter_index:
        for direction in list_of_directions:
            if check_move(board, turn, index, direction):
                list_of_valid_push_directions.append((index, direction))
    return list_of_valid_push_directions



def choose_random_index_from_list(list_of_index):
    return list_of_index[random.randint(0, len(list_of_index) - 1)]




# Level 1 is just choosing any valid random move
# Level 2 is to select winning move or prevent choosing a losing move from valid moves
def computer_move(board, turn, level):
    # implement your function here
    list_of_valid_push = get_valid_push_directions(board, turn)
    if level == 1:
        return choose_random_index_from_list(list_of_valid_push)

    else: # level 2
        enemy = 2 if turn == 1 else 1
        list_of_neutral_and_losing_move = []
        list_of_losing_moves = []
        list_of_neutral_moves = []
        #Separate winning move if any
        for move in list_of_valid_push:
            hypothetical_board= apply_move(board,turn,move[0],move[1])
            victory = check_victory(hypothetical_board, turn)
            # if found a winning move immediately return and break loop
            if victory == turn:
                return move
            else:
                list_of_neutral_and_losing_move.append(move)
        # Filter neutral moves into losing moves and winning move
        for neutral_move in list_of_neutral_and_losing_move:
            neutral_hypothetical_board = apply_move(board,turn,neutral_move[0],neutral_move[1])
            is_losing_move = False
            # Get list of enemy moves with respect to the board
            for enemy_move in get_valid_push_directions(neutral_hypothetical_board, enemy):
                enemy_hypothetical_board = apply_move(neutral_hypothetical_board, enemy,enemy_move[0],enemy_move[1])
                # The moment the move is identified as losing can break loop
                if check_victory(enemy_hypothetical_board, enemy) == enemy:
                    is_losing_move = True
                    break
            # Append repective to the outcome
            if is_losing_move:
                list_of_losing_moves.append(neutral_move)
            else:
                list_of_neutral_moves.append(neutral_move)

        if list_of_neutral_moves:
            return choose_random_index_from_list(list_of_neutral_moves)
        else:
            # No neutral moves
            return choose_random_index_from_list(list_of_losing_moves)

def display_board(board):
    print("\n----------------Display Board----------------\n")
    board_length = cal_board_length(board)
    count = 0
    for x in range(len(board)):
        print(board[x], end=" ")
        count += 1

        if count % board_length == 0:
            print()
    print()
    pass

# Function to retrieve user input and convert into int
def get_user_input(input_statement):
    while True:
        try:
            return int(input(input_statement))
        except:
            print("Please enter a valid number\n")

# Function to validate input based on given list of options
def get_user_input_validate_range(list_of_options, input_statement, error_message):
    valid_input = False
    while not valid_input:
        print()  # For UI line separation
        user_input = get_user_input(input_statement)
        # range 1 to len(list) +1 is cause the options start from 1
        valid_input = user_input in range(1, len(list_of_options) + 1)
        if not valid_input:
            print(error_message)
        else:
            return user_input

# Function to generate a list of options from the list
def generate_options_for_display(list_of_options: list):
    display_string = ""
    for i in range(len(list_of_options)):
        display_string += "\n" + "[{0}] {1}".format(i + 1, list_of_options[i])
    return display_string + "\nEnter: "

# This is a function that request user to enter the index they want to move
def selecting_index(board, turn):
    valid_index = False
    while not valid_index:
        index = get_user_input(
            "Player {0}, Please select the piece you would like to move: ".format(turn)
        )
        print(filter_list_of_perimeter_index(board, turn))
        if index in filter_list_of_perimeter_index(board, turn):
            valid_index = True
            continue
        print("Invalid Selection: Index out of range")

    return index


# Basically setting player details. Computer player is associated with a
# difficulty tuple. Human players will have an empty tuple.
def initialise_player(player_num, players_detail):
    list_of_player_type = ["Human", "Computer"]
    list_of_computer_difficulty = ["Easy", "Medium"]
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
    print("Quixo Game")
    valid_board_size = False
    while not valid_board_size:
        print()
        size_of_board = get_user_input("Enter size of board: ")
        valid_board_size = size_of_board > 1
        if not valid_board_size and size_of_board != 1:
            print("Please enter a valid board size")
        elif not valid_board_size and size_of_board == 1:
            print("Board size one has no valid moves, Please enter a valid size")

    board = [0] * size_of_board**2
    players_detail = {}
    for player_num in [1,2]:
        initialise_player(player_num, players_detail)
    map_of_user_input_to_board_direction = {
        1: "T",
        2: "B",
        3: "L",
        4: "R",
    }
    list_of_push_values = list(map_of_user_input_to_board_direction.values())

    print("\nGame start!\n")
    turn = 1
    has_winner = False
    while not has_winner:
        print("Player {0} turn\n".format(turn))
        if players_detail[turn][0] == "Human":
            # logic for human
            valid_push = False
            while not valid_push:
                display_board(board)
                index = selecting_index(board, turn)
                push_from = map_of_user_input_to_board_direction[
                    get_user_input_validate_range(
                        list_of_push_values,
                        "Player {0}, Please select push directions{1}".format(
                            turn, generate_options_for_display(list_of_push_values)
                        ),
                        "Invalid Selection: Select push direction within range",
                    )
                ]
                valid_push = check_move(board, turn, index, push_from)
                if not valid_push:
                    print("Move entered is invalid.")
            board = apply_move(board, turn, index, push_from)

        else:
            move = computer_move(board, turn, players_detail[turn][1])
            print("(Computer) Player {0} applied move {1}".format(turn, str(move)))
            board = apply_move(board, turn, move[0], move[1])
            display_board(board)

        # Check victory logic
        winner = check_victory(board, turn)
        has_winner = winner != 0
        if has_winner:
            print("Winner is player {0}".format(winner))
        turn = 2 if turn == 1 else 1


if __name__ == "__main__":
    menu()
