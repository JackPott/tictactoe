# pylint: disable=missing-function-docstring,global-statement,invalid-name,missing-module-docstring

# TODO: Make the player tokens 1 and 2
# TODO: Calculate win condition based on cell equality instead of sums
# TODO: Stop it crashing for out of range inputs
# TODO: Stop it crashing for non intable inputs (harder)
# TODO: Stop global scoping everything

# GAME TIME!
top_row = [0, 0, 0]
mid_row = [0, 0, 0]
bot_row = [0, 0, 0]
board = [top_row, mid_row, bot_row]
current_player = 1
TOKEN = (0, 5, 7)  # There is no player 0


def show_board():
    for row in board:
        print(row)


def end_turn():
    global current_player
    if current_player == 1:
        current_player = 2
    elif current_player == 2:
        current_player = 1


def place_tile(col: int, row: int, tile: int) -> bool:
    if board[row][col] == 0:
        board[row][col] = tile
    else:
        print('nogo, try again')
        return False
    return True


def winner(who: int):
    show_board()
    print(f"Huzzah! Player {who} is the winner!")
    quit()


def diag1_sum():
    return board[0][0] + board[1][1] + board[2][2]


def diag2_sum():
    return board[0][2] + board[1][1] + board[2][0]


def check_for_winner(total: int):
    if total == TOKEN[1]*3:
        winner(1)
    elif total == TOKEN[2]*3:
        winner(2)


while True:
    show_board()
    row = int(input(f"PLAYER {current_player}: Pick a row: "))-1
    col = int(input(f"PLAYER {current_player}: Pick a column: "))-1

    if place_tile(col=col, row=row, tile=TOKEN[current_player]):
        end_turn()

    # Check win (rows)
    for row in board:
        check_for_winner(sum(row))

    # Check win (cols)
    for i in range(0, 3):
        check_for_winner(board[0][i] + board[1][i] + board[2][i])

    # Check win (diags)
    check_for_winner(diag1_sum())
    check_for_winner(diag2_sum())
