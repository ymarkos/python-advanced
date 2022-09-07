a, b = input().split()
length_a = int(a)
length_b = int(b)
set_a = {input() for _ in range(length_a)}
set_b = {input() for _ in range(length_b)}
set_intersection = set_a.intersection(set_b)
[print(el) for el in set_intersection]