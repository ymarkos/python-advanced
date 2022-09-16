num_intr = int(input())

intersections = {}
for intersection in range(num_intr):
    a, b = input().split('-')
    a_st, a_end = a.split(',')
    start_a = int(a_st)
    end_a = int(a_end)
    current_a = set()
    for el in range(start_a, end_a + 1):
        current_a.add(el)
    b_st, b_end = b.split(',')
    start_b = int(b_st)
    end_b = int(b_end)
    current_b = set()
    for el2 in range(start_b, end_b + 1):
        current_b.add(el2)
    current_intersection = current_a & current_b
    current_intersection = tuple(current_intersection)
    if current_intersection not in intersections:
        intersections[current_intersection] = len(current_intersection)
max_value = max(intersections.values())
for key, value in intersections.items():
    if value == max_value:
        print(f'Longest intersection is {list(key)} with length {value}')
