row0 = ["", "O", ""]
row1 = ["X", "O", "X"]
row2 = ["X", "X", "X"]


def equal_row_cells(row):
    return row[0] == row[1] == row[2]


print(f"{row0[0]}|{row0[1]}|{row0[2]}")
print("-----")
print(f"{row1[0]}|{row1[1]}|{row1[2]}")
print("-----")
print(f"{row2[0]}|{row2[1]}|{row2[2]}")

if (equal_row_cells(row0)):
    print(f"{row0[0]} won")

if (equal_row_cells(row1)):
    print(f"{row1[0]} won")

if (equal_row_cells(row2)):
    print(f"{row2[0]} won")
