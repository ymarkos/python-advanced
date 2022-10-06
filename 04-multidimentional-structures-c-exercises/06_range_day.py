def move(direction, steps):
    r = my_position[0] + (directions[direction][0] * steps)
    c = my_position[1] + (directions[direction][1] * steps)

    if not (0 <= r < size and 0 <= c < size):
        return my_position
    if field[r][c] == 'x':
        return my_position

    return [r, c]


def shoot(direction):
    r = my_position[0] + (directions[direction][0])
    c = my_position[1] + (directions[direction][1])
    while 0 <= r < size and 0 <= c < size:
        if field[r][c] == 'x':
            field[r][c] = '.'
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


size = 5

field = []

targets = 0
hit_targets = 0
hit_targets_positions = []
my_position = []

directions = {
    'right': (0, 1),
    'left': (0, -1),
    'up': (-1, 0),
    'down': (1, 0)
}

for row in range(size):
    line = input().split()
    field.append(line)
    if 'A' in line:
        my_position = [row, line.index('A')]
        field[row][my_position[1]] = '.'
    targets += line.count('x')

num_commands = int(input())

for _ in range(num_commands):
    command_info = input().split()

    if command_info[0] == 'move':
        my_position = move(command_info[1], int(command_info[2]))

    elif command_info[0] == 'shoot':
        target_down_pos = shoot(command_info[1])

        if target_down_pos:
            hit_targets_positions.append(target_down_pos)
            hit_targets += 1
        if hit_targets == targets:
            print(f'Training completed! All {hit_targets} targets hit.')
            break

if hit_targets < targets:
    print(f'Training not completed! {targets-hit_targets} targets left.')

[print(target_pos) for target_pos in hit_targets_positions]
