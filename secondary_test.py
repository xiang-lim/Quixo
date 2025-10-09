# -*- coding: utf-8 -*-
"""
Created on Tue Oct  7 10:45:08 2025

@author: Xiang
"""
from quixo import *


## Cases that was caught
def fail_test(name):
    print("FAILED")


def pass_test(name):
    print("Pass")


def apply_board_test(number, description, board, board_result, turn, index, direction):
    print("Bug {0}:".format(number) + description)
    board_tmp = apply_move(board, turn, index, direction)
    if board_tmp == board_result:
        pass_test(number)
    else:
        fail_test(number)


def test():

    # Bug 03 - SOLVED
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    board_result = [1, 0, 0, 0, 0, 0, 0, 0, 0]
    apply_board_test(
        3,
        "Swapping of top rows had index out of range issues",
        board,
        board_result,
        1,
        6,
        "T",
    )
    print()

    # TODO Bug 04 - should have no victory condition
    print("Bug 04: There should not be a win for this condition")
    board = [0, 1, 1, 2, 0, 2, 1, 0, 1]
    if check_victory(board, 1) == 0:
        pass_test(2)
    else:
        fail_test(4)


test()
