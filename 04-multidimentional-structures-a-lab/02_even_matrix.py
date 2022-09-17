rows = int(input())


even_matrix = []
for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    even_matrix.append(
        [x for x in row if x % 2 == 0]
    )

print(even_matrix)

#
# rows = int(input())
# matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]
# print([[x for x in row if x % 2 == 0] for row in matrix])


# num = int(input())
# even_matrix = []
#
# for _ in range(num):
#     even = []
#     for el in [int(el) for el in input().split(', ')]:
#         if el % 2 == 0:
#             even.append(el)
#     even_matrix.append(even)
#
# print(even_matrix)
