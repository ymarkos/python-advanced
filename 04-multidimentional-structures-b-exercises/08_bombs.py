def get_children(matrix, row, col):
    possible_children_cords = [
        [row - 1, col - 1],
        [row, col - 1],
        [row + 1, col - 1],
        [row - 1, col],
        [row + 1, col],
        [row - 1, col + 1],
        [row, col + 1],
        [row + 1, col + 1],

    ]
    result = []
    #validate if a cell is valid
    for child_row, child_col in possible_children_cords:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix) and matrix[child_row][child_col] > 0:
            result.append([child_row, child_col])
    return result


size = int(input())

matrix = []
for _ in range(size):
    matrix.append([int(el) for el in input().split()])

bombs = input().split()


for bomb in bombs:
    row, col = [int(el) for el in bomb.split(',')]
    power = matrix[row][col]
    if power <= 0:
        continue
    matrix[row][col] = 0
    children = get_children(matrix, row, col)
    for child_row, child_col in children:
        matrix[child_row][child_col] -= power

count_cells_alive = 0
sum_cells_alive = 0
for row in matrix:
    for el in row:
        if el > 0:
            count_cells_alive += 1
            sum_cells_alive += el
print(f'Alive cells: {count_cells_alive}')
print(f'Sum: {sum_cells_alive}')

for row in matrix:
    print(*row)


