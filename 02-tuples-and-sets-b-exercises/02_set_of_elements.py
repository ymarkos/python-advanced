a, b = input().split()
length_a = int(a)
length_b = int(b)
set_a = {input() for _ in range(length_a)}
set_b = {input() for _ in range(length_b)}
set_intersection = set_a.intersection(set_b)
[print(el) for el in set_intersection]


# first_length, second_length = [int(x) for x in input().split()]
# first_set = set()
# second_set = set()
# for _ in range(first_length):
#     char = input()
#     first_set.add(int(char))
#
# for _ in range(second_length):
#     char = input()
#     second_set.add(int(char))
# intersection = first_set & second_set
# [print(el) for el in intersection]