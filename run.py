import random
board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-",]

currentPlayer = "X"
winner= None
gameRunning= True

# game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("---------")
# check if a player has won
def check_win(board, player):
    win-combinations==[
        [board[0],board[1],board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
]
for combination in win_combinations:
    if all(cell==player for cell in combination):
       return True
    return False