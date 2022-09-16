num = int(input())

unique_names = set()
for _ in range(num):
    unique_names.add(input())

[print(name) for name in unique_names]