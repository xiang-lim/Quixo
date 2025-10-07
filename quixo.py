import random
import math

def check_move(board, turn, index, push_from):
    # implement your function here
    return True

def apply_move(board, turn, index, push_from):
    # implement your function here
    return board[:]

def check_victory(board, who_played):
    # implement your function here
    return -1

def computer_move(board, turn, level):
    # implement your function here
    return (0,'B')
    
def display_board(board):
    # implement your function here
    count=0
    for x in range(len(board)):
        print(board[x], end=" ")
        count+=1
        
        if count%5==0:
            print()
    
        
    pass

def menu():
    # implement your function here
    pass

 
if __name__ == "__main__":
    menu()


    
