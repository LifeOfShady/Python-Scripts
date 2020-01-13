import random

def full_board_check(board):
    for i in range(0,9):
        if board[i]=="":
            return True
        else:
            continue
    print("It's a draw!!")
    return False
    
def win_check(board, mark):
    win_combs = [[0,1,2],
                 [3,4,5],
                 [6,7,8],
                 [0,3,6],
                 [1,4,7],
                 [2,5,8],
                 [0,4,8],
                 [2,4,6]]
    indexes=[]
    for i in range(0,9):
        if board[i]==mark:
            indexes.append(i)
    
    for each in win_combs:
        if set(each).issubset(indexes):
            return True


def choose_first():
    p1 = input("Enter Player 1 name:")
    p2 = input("Enter Player 2 name:")
    i = random.randint(1,2)
    if i==1:
        print(f"{p1} will go first.")
        return p1,p2
    else:
        print(f"{p2} will go first.")
        return p2,p1
    
    return p1,p2

def player_input(p1,p2):
    player1=""
    player2=""
    
    while True:
        marker = input("Select your marker - 'X' or 'O' : ")
        if(marker=="O" or marker=="X"):
            break
        else:
            print("Invalid choice")
        continue
    
    player1 = marker
    if player1=="X":
        player2 = "O"
    else:
        player2 = "X"
    print(f"{p1} chose {player1} and {p2} chose {player2}. Let's start the Game!!!")
    return player1,player2
    
def display_board(board):
    
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    
    
def space_check(board, position):
    if board[position-1]=="":
        return True
    else:
        return False
    
    
def place_marker(board, pc, pos):
    board[pos-1] = pc
    
def player_choice(board, pc):
    pos = int(input(f"Enter position for {pc}: "))
    yesorno = space_check(board,pos)
    if yesorno==True:
        place_marker(board, pc, pos)
    else:
        print("Space already occupied")
        return False
        
         
        
print('Welcome to Tic Tac Toe!')

p1,p2 = choose_first()
test_board = ['','','','','','','','','']
p1c, p2c = player_input(p1,p2)
display_board(test_board)

while True:
    if full_board_check(test_board):
        player_choice(test_board, p1c)
        display_board(test_board)

        if win_check(test_board,p1c):
            print(f"{p1} WINS!!!")
            break
    if full_board_check(test_board):
        player_choice(test_board, p2c)
        display_board(test_board)

        if win_check(test_board,p2c):
            print(f"{p2} WINS!!!")
            break
