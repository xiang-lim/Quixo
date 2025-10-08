import random
import math


def check_move(board, turn, index, push_from):
    # implement your function here
    n = int(math.sqrt(len(board)))
    # [1st row, 1st col, last row, last col]
    perimeter_index = [j for j in range(n)] + \
                        [i * n for i in range(n)] + \
                            [(n - 1) * n + j for j in range(n)] + \
                                [i * n + (n - 1) for i in range(n)]
    perimeter_index = sorted(set(perimeter_index))

    # not an index for a cube in the perimeter OR the cube is not mine
    if index not in perimeter_index or board[index] not in [turn, 0]: 
        return False
    else:
        corner_index = [0*n , n-1, (n-1)*n, (n-1)*n + (n-1)]
        corner_moves = [["B", "R"], ["B", "L"], ["T", "R"], ["T", "L"]]

        # check if the index is for a cube at the corner
        if index in corner_index: 
            # create a dictionary of avail moves for each corner cube
            corner_moves_dict = {corner_index[i]:corner_moves[i] for i in range(len(corner_index))}
            # move is  avail for that specific corner cube
            if push_from in corner_moves_dict[index]:
                return True
            else: # move is not avail for that specific corner cube
                return False
        else: # in between 2 corners
            # Pick 2nd element from corner index, check if index less than, If no, pick the next larger element. 
            # Case 1: less than 2nd element >> B,L,R
            if (0 < index < corner_index[1]) and push_from in ["B", "L", "R"]:
                return True
            
            # Case 2: less than 3rd element
                    #   A: if index multiple of n means 1st col, 
                    #       >> T, B, R
                    #   B: else last col
                    #       >> T, B, L
            elif (corner_index[1] < index < corner_index[2]) and \
                ((index % n == 0 and push_from in ["T", "B", "R"]) or (index % n != 0 and push_from in ["T", "B", "L"])):
                    return True
            # Case 3: less than 4th aka largest element >> T,L,R
            elif (corner_index[2] < index < corner_index[3]) and push_from in ["T", "L", "R"]: 
                return True
            else:
                return False

def apply_move(board, turn, index, push_from):
    # implement your function here
    return board[:]

def check_victory(board, who_played):
    # implement your function here
    dim_board = int(math.sqrt(len(board)))
    
    player_1_score = []
    player_2_score =[]
    
    
    
    #Check left diagonal
    left_diagonal = board[0:len(board):dim_board+1]
    
    #Check left diagonal score
    if left_diagonal.count(1)==dim_board:
       player_1_score.append(1)
    
    elif left_diagonal.count(2)==dim_board:
        player_2_score.append(1)

    

    
    
    #Check right diagonal
    right_diagonal=board[dim_board-1:len(board):dim_board-1]
    
    #Check right diagonal score
    if left_diagonal.count(1)==dim_board:
       player_1_score.append(1)
    
    elif left_diagonal.count(2)==dim_board:
        player_2_score.append(1)
    
    
    

    
    #Check column:
    for c in range(dim_board):
        column = board[c::dim_board]
        
        if column.count(1)==dim_board:
            player_1_score.append(1)
            
        elif column.count(2)==dim_board:
            player_2_score.append(1)
            
            
            
    
    
    #Check row:
    for e in range(dim_board):
        row = board[e*dim_board:(e+1)*dim_board:1]
    
        if row.count(1)==dim_board:
            player_1_score.append(1)
            
        elif row.count(2)==dim_board:
            player_2_score.append(1)
            

    
    #Final deduction
    
    if who_played==1:
        
        if 1 in player_2_score:
            return who_played+1
        
        elif len(player_1_score)==0 and len(player_2_score)==0:
            return 0
        
        else:
            return who_played
    
    
    elif who_played==2:
        
            if 1 in player_1_score:
                
                return who_played-1
            
            elif len(player_1_score)==0 and len(player_2_score)==0:
                return 0
        
            else:
                return who_played
   

def computer_move(board, turn, level):
    # implement your function here
    return (0,'B')
    
def display_board(board):
    # implement your function here
    # 
    count=0
    for x in range(len(board)):
        print(board[x], end=" ")
        count+=1
        
        if count%5==0:
            print()
    pass

def menu():
    # implement your function here

    #Load board
    n = 5
    quixo_board = []
    for i in range(n**2):
        quixo_board.append(0)
        
        pass
    

 
if __name__ == "__main__":
    menu()


    
