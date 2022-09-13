# 1st option
data = [int(x) for x in input().split()]

while data:
    print(data.pop(), end=' ')

# 2nd option
# line = list(input().split())
# reversed_line = []
# while line:
#     reversed_line.append(line.pop())
# print(' '.join(reversed_line))
