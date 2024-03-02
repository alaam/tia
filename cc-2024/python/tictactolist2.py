row0 = ["O", "O", ""]
row1 = ["X", "O", "O"]
row2 = ["X", "X", "O"]

def display_row(whatever):
    print(whatever[0], '|', whatever[1], '|', whatever[2])

def equal_row(elements):
    return elements[0] == elements[1] == elements[2]

def equal_column(row0, row1, row2, col):
    return row0[col] == row1[col] == row2[col]

def equal_diagonal(row0, row1, row2):
    return (row0[0] == row1[1] == row2[2]) or (row0[2] == row1[1] == row2[0])

def display_board():
    display_row(row0)
    display_row(row1)
    display_row(row2)

def check_winner():

display_board()
