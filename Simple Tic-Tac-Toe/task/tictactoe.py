# definitions
grids = []
for i in range(3):
    grids.append([])
    for x in range(3):
        grids[i].append(' ')
# Analyze if there are 3 in a row
win_cells = [grids[0], grids[1], grids[2], [grids[0][0], grids[1][0], grids[2][0]],
             [grids[0][1], grids[1][1], grids[2][1]],
             [grids[0][2], grids[1][2], grids[2][2]],
             [grids[0][0], grids[1][1], grids[2][2]],
             [grids[0][2], grids[1][1], grids[2][0]]]


def print_grid():
    print('---------')
    print('| ' + ' '.join(grids[0]) + ' |')
    print('| ' + ' '.join(grids[1]) + ' |')
    print('| ' + ' '.join(grids[2]) + ' |')
    print('---------')


# check input coordinates
def check_co(cos):
    global c
    global grids
    numbers = list('0123456789')
    while c == 0:
        if cos[0] in ['1', '2', '3'] and cos[1] in ['1', '2', '3']:
            if grids[int(cos[0])-1][int(cos[1])-1] in ['X', 'O']:
                print('This cell is occupied! Choose another one!')
                cos = input('Enter the coordinates:').split()
                c = 0
            else:
                global i
                if i % 2 == 0:
                    grids[int(cos[0])-1][int(cos[1])-1] = 'X'
                    c = 1
                else:
                    grids[int(cos[0])-1][int(cos[1])-1] = 'O'
                    c = 1
        elif cos[0] in numbers and cos[1] in numbers:
            print('Coordinates should be from 1 to 3!')
            cos = input('Enter the coordinates:').split()
            c = 0
        else:
            print('You should enter numbers!')
            cos = input('Enter the coordinates:').split()
            c = 0


# print a blank grid
print_grid()

# input the coordinates and put 'X' or 'O' in the grid
for i in range(9):
    coordinates = input('Enter the coordinates:').split()
    c = 0  # check if coordinates is available
    check_co(coordinates)
    print_grid()
    x3_in_row = ['X', 'X', 'X'] in win_cells
    o3_in_row = ['O', 'O', 'O'] in win_cells
    print(win_cells)
    if x3_in_row:
        print('X wins')
        break
    elif o3_in_row:
        print('O wins')
        break
    elif i == 8:
        print('Draw')
        print(x3_in_row)
