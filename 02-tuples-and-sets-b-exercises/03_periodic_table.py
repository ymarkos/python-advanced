num = int(input())

elements = set()

for _ in range(num):
    elements_str = input().split()
    for element in elements_str:
        elements.add(element)

[print(element) for element in elements]

