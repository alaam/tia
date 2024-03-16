row0 = ["O", "O", ""]
row1 = ["X", "O", "O"]
row2 = ["X", "X", "O"]

player1_name = ""
player2_name = ""
first_player = ""
player1_symbol = ""
player2_symbol = ""

def display_row(row):
    print(row[0], '|', row[1], '|', row[2])


def is_equal_row(elements):
    return elements[0] == elements[1] == elements[2]


def is_equal_column(col):
    return row0[col] == row1[col] == row2[col]


def is_equal_diagonal():
    return (row0[0] == row1[1] == row2[2]) or (row0[2] == row1[1] == row2[0])


def display_board():
    display_row(row0)
    display_row(row1)
    display_row(row2)


def check_winner():
    one_of_cols_equal = is_equal_column(0) or is_equal_column(1) or is_equal_column(2)
    one_of_rows_equal = is_equal_row(row0) or is_equal_row(row1) or is_equal_row(row2)
    one_of_diagonals = is_equal_diagonal()

    return one_of_diagonals or one_of_rows_equal or one_of_cols_equal


def get_player_info():
    player1_name = input("Enter Player 1 name: ")
    player2_name =
    first_player =
    player1_symbol =
    player2_symbol =

# display_board()
# print(check_winner())
symbol = "X"
while symbol == "X" or symbol == "O":
    symbol = input("Enter a symbol - ")
    if symbol == "Y":
        print("Y breaks the loop")
        break
    print(symbol)

