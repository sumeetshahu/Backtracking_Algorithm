def solve(board, col, n):
    
	if col >= n: 
		return True

	for i in range(n): 
		if issafe(board, i, col, n): 
			board[i][col] = 1
			if solve(board, col + 1, n) == True: 
				return True
			board[i][col] = 0

	return False

def issafe(board, row, col, n): 

	for i in range(col): 
		if board[row][i] == 1: 
			return False

	for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False

	for i, j in zip(range(row, n, 1), range(col, -1, -1)): 
		if board[i][j] == 1: 
			return False

	return True

def printboard(board, n): 
	for i in range(n): 
		for j in range(n): 
			print (board[i][j], end=' ')
		print()

n = 6
print('{} x {} board'.format(n, n))
print()
game_board = [[0]*n for i in range(n)]
printboard(game_board, n)
print()
print("Solution with {} queens placed".format(n))
print()
solve(game_board, 0, n)
printboard(game_board, n)


    
        

