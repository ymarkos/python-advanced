num = int(input())

matrix = []
for _ in range(num):
    chars = list(input())
    matrix.append(chars)

position = None
searched_ch = input()
for index_row in range(num):
    for index_colon in range(num):
        if searched_ch == matrix[index_row][index_colon]:
            position = (index_row, index_colon)
            print(position)
            break
    if position:
        break

if not position:
    print(f'{searched_ch} does not occur in the matrix')


