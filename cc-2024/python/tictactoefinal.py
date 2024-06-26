import random

row0 = ["", "", ""]
row1 = ["", "", ""]
row2 = ["", "", ""]

symbol = "o"

player1_name = ""
player2_name = ""
first_player = ""
current_player = ""


def display_row(row):
    print(row[0], '|', row[1], '|', row[2])


def is_equal_row(elements):
    return (elements[0] != "") and elements[0] == elements[1] == elements[2]


def is_equal_column(col):
    return (row0[col] != "") and row0[col] == row1[col] == row2[col]


def is_equal_diagonal():
    return ((row0[0] != "") and row0[0] == row1[1] == row2[2]) or ((row0[2] != "") and row0[2] == row1[1] == row2[0])


def display_board():
    print("------")
    display_row(row0)
    print("------")
    display_row(row1)
    print("------")
    display_row(row2)
    print("------")


def someone_won():
    one_of_cols_equal = is_equal_column(0) or is_equal_column(1) or is_equal_column(2)
    one_of_rows_equal = is_equal_row(row0) or is_equal_row(row1) or is_equal_row(row2)
    one_of_diagonals = is_equal_diagonal()

    return one_of_diagonals or one_of_rows_equal or one_of_cols_equal


def get_player_info():
    global player1_name
    global player2_name
    global first_player
    global symbol
    global current_player

    player1_name = input("Enter Player 1 name: ")
    player2_name = input("Enter Player 2 name: ")
    first_player = input("Enter first Player: ")
    current_player = first_player
    symbol = input("Enter Player 1 symbol: ")


# function that displays player info
def display_player_info():
    print("Player1 name is :", player1_name)
    print(f"Player1 name is : {player1_name}")


def cell_is_empty(row, column):
    if row == 0:
        return row0[column] == ""

    if row == 1:
        return row1[column] == ""

    if row == 2:
        return row2[column] == ""


def get_row_column():
    row = random.randrange(start=0, stop=3, step=1)
    column = random.randrange(start=0, stop=3, step=1)
    while not cell_is_empty(row, column):
        row = random.randrange(start=0, stop=3, step=1)
        column = random.randrange(start=0, stop=3, step=1)

    return row, column

def next_play():
    global row0
    global row1
    global row2
    global symbol
    global player1_name
    global current_player

    if current_player == "computer":
        row, column = get_row_column()
        print(f"computer chose {row} {column}")
    else:
        row_str, column_str = input(f"{current_player}, which row column? ").split()
        row = int(row_str)
        column = int(column_str)

    if row == 0:
        row0[column] = symbol

    if row == 1:
        row1[column] = symbol

    if row == 2:
        row2[column] = symbol

    symbol = "o" if symbol == "x" else "x"
    if not someone_won():
        current_player = player1_name if current_player == player2_name else player2_name

get_player_info()
while not someone_won():
    display_board()
    next_play()
display_board()
print(f"{current_player} won!!!!")
