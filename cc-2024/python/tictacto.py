symbol_x = 'X'
symbol_o = 'O'

cell_0_0 = "O"
cell_0_1 = "O"
cell_0_2 = " "

cell_1_0 = " "
cell_1_1 = "X"
cell_1_2 = " "

cell_2_0 = " "
cell_2_1 = " "
cell_2_2 = "O"

print(f"{cell_0_0}|{cell_0_1}|{cell_0_2}")
print("-----")
print(f"{cell_1_0}|{cell_1_1}|{cell_1_2}")
print("-----")
print(f"{cell_2_0}|{cell_2_1}|{cell_2_2}")

if (cell_0_0 == cell_1_1 == cell_2_2 or
    cell_0_2 == cell_1_1 == cell_2_0):
    print(f"{cell_0_0} won!")
else:
    print("No one won :-(")