def display_board(board):
    print("""
     {} | {} | {} 
    ---+---+---
     {} | {} | {} 
    ---+---+---
     {} | {} | {} """.format(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8]))

def check_board(board):
    if (board[0] == board[1] == board[2] == player) or (board[3] == board[4] == board[5] == player) or (board[6] == board[7] == board[8] == player) or (board[0] == board[3] == board[6] == player) or (board[1] == board[4] == board[7] == player) or (board[2] == board[5] == board[8] == player) or (board[0] == board[4] == board[8] == player) or (board[2] == board[4] == board[6] == player):
        return True

if __name__ == "__main__":
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player1_turn = True
    while True:
        player = input("Choose X or O: ")
        if player == "X" or player == "O":
            break
    display_board(board)
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    while True:
        if player1_turn and player == 'X':
            while True:
                selection = int(input("Player One, your location number: "))
                if board[selection - 1] == ' ':
                    break
                print("Your move is invalid")
            board[selection - 1] = player
            display_board(board)
            if check_board(board):
                print("Game Over. {} won".format(player))
                break
            else:
                print("Tie")
            player1_turn = False
            player = 'O'
        else:
            while True:
                selection = int(input("Player Two, your location number: "))
                if board[selection - 1] == ' ':
                    break
                print("Your move is invalid")
            board[selection - 1] = player
            display_board(board)
            if check_board(board):
                print("Game Over. {} won".format(player))
                break
            else:
                print("Tie")
            player1_turn = True
            player = 'X'
