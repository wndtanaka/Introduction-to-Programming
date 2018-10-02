def display_board(board):
    print("""
{}|{}|{}
-----
{}|{}|{}
-----
{}|{}|{}""".format(board[0][0], board[1][0], board[2][0], board[0][1], board[1][1], board[2][1], board[0][2],
                   board[1][2], board[2][2]))


def check_board(board):
    if (board[0][0] == board[0][1] == board[0][2] == player) or (
            board[1][0] == board[1][1] == board[1][2] == player) or (
            board[2][0] == board[2][1] == board[2][2] == player) or (
            board[0][0] == board[1][0] == board[2][0] == player) or (
            board[0][1] == board[1][1] == board[2][1] == player) or (
            board[0][2] == board[1][2] == board[2][2] == player) or (
            board[0][0] == board[1][1] == board[2][2] == player) or (
            board[0][2] == board[1][1] == board[2][0] == player):
        return True
    else:
        if number_of_turns >= 9:
            return False


if __name__ == "__main__":
    number_of_turns = 0
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player_turn = True
    player = 'X'
    selection = input()
    while player_turn:
        player = 'X'
        selection = selection.split()
        a = int(selection[0])
        b = int(selection[1])
        board[a][b] = player
        number_of_turns += 1
        if check_board(board):
            print(player + " wins!")
            display_board(board)
            break
        display_board(board)
        player_turn = False
    while True:
        if check_board(board):
            break
        while player_turn and not check_board(board):
            player = 'X'
            print()
            selection = input()
            selection = selection.split()
            a = int(selection[0])
            b = int(selection[1])
            number_of_turns += 1
            board[a][b] = player
            if number_of_turns >= 9:
                print("Draw")
                check_board(board)
                display_board(board)
                break
            if check_board(board):
                print(player + " wins!")
                display_board(board)
                print()
                break
            display_board(board)
            player_turn = False
        if not check_board(board) and number_of_turns >= 9:
            print()
            break
        while not player_turn and not check_board(board):
            player = 'O'
            print()
            selection = input()
            selection = selection.split()
            a = int(selection[0])
            b = int(selection[1])
            number_of_turns += 1
            board[a][b] = player
            if number_of_turns >= 9:
                print("Draw")
                check_board(board)
                display_board(board)
                break
            if check_board(board):
                print(player + " wins!")
                display_board(board)
                print()
                break
            display_board(board)
            player_turn = True