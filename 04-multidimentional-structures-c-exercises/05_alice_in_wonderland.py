size = int(input())

matrix = []
alice_pos = []
tea_bags = 0

directions = {
    'down': (1, 0),
    'up': (-1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    line = input().split()
    matrix.append(line)
    if 'A' in line:
        alice_pos = [row, line.index('A')]
        matrix[row][alice_pos[1]] = '*'

while tea_bags < 10:
    direction = input()
    row = alice_pos[0] + directions[direction][0]
    col = alice_pos[1] + directions[direction][1]
    if not (0 <= row < size and 0 <= col < size):
        break
    alice_pos = [row, col]
    position = matrix[row][col]
    matrix[row][col] = '*'

    if position == 'R':
        break

    if position.isdigit():
        tea_bags += int(position)


if tea_bags < 10:
    print(f"Alice didn't make it to the tea party.")
else:
    print(f'She did it! She went to the party.')

for row in matrix:
    print(*row)