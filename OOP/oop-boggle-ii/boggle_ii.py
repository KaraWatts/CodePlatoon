test_board = ['IDVW','ECOQ','NBIR','ZPER']
match = "RIBN"
start_coord_list = []
for row in range(4):
    for col in range(4):
        match [row, col]:
            case [1, 1]:
                pass
            case [1,2]:
                pass
            case [2,1]:
                pass
            case [2,2]:
                pass
            case _:
                if test_board[row][col] == match[0]:
                    start_coord_list.append([row, col])


test_coord_list = [
    [1, -1],
    [1, 0],
    [1, 1],
    [-1, -1],
    [-1, 0],
    [-1, 1],
    [0, 1],
    [0, -1]
]
filtered_case_list = []
def cases(row, col):
    # match = 0
    for case in test_coord_list:
        test_row = row + case[0]
        test_col = col + case[1]

        if 0 <= test_row <= 3 and 0 <= test_col <= 3:
            if test_board[test_row][test_col] == match[1]:
                print(test_board[row][col], row, col, 1)
                print(test_board[test_row][test_col], test_row, test_col, 2)
                check_three(test_row, test_col, case)

def check_second(start_coord):
    row = start_coord[0]
    col = start_coord[1]
    cases(row, col)

def check_three(row, col, case):

    test_row = row + case[0]
    test_col = col + case[1]
    
    if 0 <= test_row <= 3 and 0 <= test_col <= 3:
        if test_board[test_row][test_col] == match[2]:
            print(test_board[test_row][test_col], row, col, 3)
            test_row = test_row + case[0]
            test_col = test_col + case[1]
            if test_board[test_row][test_col] == match[3]:
                print('Match', test_board[test_row][test_col], row, col, 4)
                return

for coord in start_coord_list:
    check_second(coord)

for row in test_board:
    print(row)


# print(start_coord_list)
