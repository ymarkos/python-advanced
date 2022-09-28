size = int(input())
commands = input().split()
matrix = []
miner_row = 0
miner_col = 0
total_coal = 0
game_over = False

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)
    for col in range(size):
        element = row_elements[col]
        if element == 's':
            miner_row = row
            miner_col = col
        elif element == 'c':
            total_coal += 1


def get_next_pos(matrix, row, col):
    if command == 'up':
        return row - 1, col
    if command == 'down':
        return row + 1, col
    if command == 'right':
        return row, col + 1
    if command == 'left':
        return row, col - 1


for command in commands:
    next_row, next_col = get_next_pos(matrix, miner_row, miner_col)
    if 0 > next_row < 0 or next_row >= size or next_col < 0 or next_col >= size:
        continue

    miner_row = next_row
    miner_col = next_col

    if matrix[miner_row][miner_col] == 'e':
        print(f'Game over! ({miner_row}, {miner_col})')
        game_over = True
        break

    elif matrix[miner_row][miner_col] == 'c':
        matrix[miner_row][miner_col] = '*'
        total_coal -= 1
        if total_coal == 0:
            game_over = True
            print(f'You collected all coal! ({miner_row}, {miner_col})')
            break


if not game_over:
    print(f'{total_coal} pieces of coal left. ({miner_row}, {miner_col})')