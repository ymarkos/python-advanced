rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])


def is_valid_coordinates(row, col, rows):
    if 0 <= row < rows and 0 <= col < rows:
        return True


while True:
    commands = input()
    if commands == 'END':
        break
    commands = commands.split()
    if commands[0] == 'Add':
        row, col, num = [int(x) for x in commands[1:]]
        if is_valid_coordinates(row, col, rows):
            matrix[row][col] += num
        else:
            print('Invalid coordinates')
    elif commands[0] == 'Subtract':
        row, col, num = [int(x) for x in commands[1:]]
        if is_valid_coordinates(row, col, rows):
            matrix[row][col] -= num
        else:
            print('Invalid coordinates')


for row in matrix:
    print(*row)