num = int(input())


for _ in range(num):
    data = input().split('-')
    first_start, first_end = data[0].split(',')
    second_start, second_end = data[1].split(',')
