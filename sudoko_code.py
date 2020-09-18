#sudoko_solver

game_board = [[5,1,7,6,0,0,0,3,4],
              [2,8,9,0,0,4,0,0,0],
              [3,4,6,2,0,5,0,9,0],
              [6,0,2,0,0,0,0,1,0],
              [0,3,8,0,0,6,0,4,7],
              [0,0,0,0,0,0,0,0,0],
              [0,9,0,0,0,0,0,7,8],
              [7,0,3,4,0,0,5,6,0],
              [0,0,0,0,0,0,0,0,0]]

def solve(board):
    found = find_empty(board)
    
    if not found:
        return True
    else:
        row, col = found
        for i in range(1,10):
            if is_valid(board, i, (row, col)):
                board[row][col] = i
                if solve(board):
                    return True
                else:
                    board[row][col] = 0
        return False

def is_valid(board, num, pos):
    row, col = pos

    #check row
    if num in board[row]:
        return False

    #check column
    for l in board:
        if l[col] == num:
            return False

    #check boxes
    box_row, box_col = row//3, col//3
    for i in range(box_row*3, box_row+3):
        for j in range(box_col*3, box_col+3):
            if board[i][j] == num:
                return False

    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return False

def print_board(board):
    for i in range(len(board)):
        if i%3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(board[0])):
            if j%3 == 0 and j!=0:
                print('|', end=' ')
            print(board[i][j], end=' ')
        print()
        
print("Initial Gameboard: \n")
print_board(game_board)
print()
solve(game_board)
print("Solved Gameboard: \n")
print_board(game_board)
