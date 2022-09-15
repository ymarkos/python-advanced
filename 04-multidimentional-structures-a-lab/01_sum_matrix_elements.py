def read_matrix():
    rows, columns = [int(x) for x in input().split(', ')]
    matrix = []
    for _ in range(rows):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)
    return matrix


matrix = read_matrix()


def sum_matrix():
    total_sum = 0
    for el in matrix:
        total_sum += sum(el)
    return total_sum


tot_sum = sum_matrix()
print(tot_sum)
print(matrix)
