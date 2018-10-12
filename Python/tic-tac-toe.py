#define the playing area
board = {
	#top row
	't-left': ' ',
	't-mid': ' ',
	't-right': ' ',
	#middle row
	'm-left': ' ',
	'm-mid': ' ',
	'm-right': ' ',
	#bottom row
	'l-left': ' ',
	'l-mid': ' ',
	'l-right': ' '
}

#print board on screen
def printBoard(board):
	print(board['t-left'] + '   |  ' +board['t-mid'] + '|   ' +board['t-right'])
	print(board['t-left'] + '   |  ' +board['t-mid'] + '|   ' +board['t-right'])
	
	print(' ---+---+---')
	
	print(board['m-left'] + '   |  ' +board['m-mid'] + '|   ' +board['m-right'])
	print(board['m-left'] + '   |  ' +board['m-mid'] + '|   ' +board['m-right'])
	
	print(' ---+---+---')
	
	print(board['l-left'] + '   |  ' +board['l-mid'] + '|   ' +board['l-right'])
	print(board['l-left'] + '   |  ' +board['l-mid'] + '|   ' +board['l-right'])

#turn is initially assigned to player X
turn = 'X'

#9 turns; for each turn:
#  - print board
#  - ask player for board coordinates via input
#  - switch player after input
for i in range(9):
	printBoard(board)
	print('\n' turn +turn.' + '. Which space do you want to mark?')
	move = input()
	board[move] = turn
	if turn == 'X':
		turn = 'O'
	else:
		turn = 'X'

printBoard(board)

#todo:
# - handle user trying to set mark in already marked space
# - determine winner