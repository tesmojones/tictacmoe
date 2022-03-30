from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    while True:
        user_input = input("Enter your move: ")
        try:
            if int(user_input) in range(1,10):
                for idxrow, row in enumerate(board):
                    for idxcol, col in enumerate(row):
                        if user_input == col:
                            board[idxrow][idxcol] = 'O'
                            display_board(board)
                            return
        except:
            print("", end="")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_list = []
    for idxrow, row in enumerate(board):
        for idxcol, col in enumerate(row):
            if col != 'X' and col != 'O':
                free_list.append(tuple([idxrow,idxcol]))
    
    return tuple(free_list)


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if board[0][0]==sign and board[0][1]==sign and board[0][2]==sign:
        return True
    if board[1][0]==sign and board[1][1]==sign and board[1][2]==sign:
        return True
    if board[2][0]==sign and board[2][1]==sign and board[2][2]==sign:
        return True
    
    if board[0][0]==sign and board[1][0]==sign and board[2][0]==sign:
        return True
    if board[0][1]==sign and board[1][1]==sign and board[2][1]==sign:
        return True
    if board[0][2]==sign and board[1][2]==sign and board[2][2]==sign:
        return True
    
    if board[0][0]==sign and board[1][1]==sign and board[2][2]==sign:
        return True
    if board[0][2]==sign and board[1][1]==sign and board[2][0]==sign:
        return True
    
    return False
    


def draw_move(board):
    free_list = make_list_of_free_fields(board)
    choice = randrange(len(free_list))
    board[free_list[choice][0]][free_list[choice][1]] = 'X'
    # The function draws the computer's move and updates the board.
    display_board(board)
    
    
board = [['1','2','3'],['4','X','6'],['7','8','9']]
display_board(board)
while True:
    
    enter_move(board)
    if victory_for(board, 'X'):
        print("Computer Won")
        break
    if victory_for(board, 'O'):
        print("You Won")
        break
    
    draw_move(board)
    if victory_for(board, 'X'):
        print("Computer Won")
        break
    if victory_for(board, 'O'):
        print("You Won")
        break

print("done")



