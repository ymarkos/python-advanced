size = int(input())

matrix = [(list(x for x in input()))for _ in range(size)]

knight_movements = (
    (-2, 1),
    (-2, -1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2)


)

deleted = 0
while True:
    max_attacks = 0
    knight_with_most_attacks_position = []
    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                attacks = 0
                for mov in knight_movements:
                    mov_row = row + mov[0]
                    mov_col = col + mov[1]
                    if size > mov_row >= 0 and size > mov_col >= 0:
                        if matrix[mov_row][mov_col] == 'K':
                            attacks += 1
                if attacks > max_attacks:
                    knight_with_most_attacks_position = [row, col]
                    max_attacks = attacks
    if knight_with_most_attacks_position:
        matrix[knight_with_most_attacks_position[0]][knight_with_most_attacks_position[1]] = '0'
        deleted +=1
    else:
        break


print(deleted)












