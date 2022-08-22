from collections import deque

kids_string = input()
tosses_count = int(input())

kids = deque(kids_string.split())
current_count = 0

while len(kids) > 1:
    # the current toss
    current_count +=1

    # the current kid
    kid = kids.popleft()
    if current_count < tosses_count:
        kids.append(kid)
    else:
        print(f'Removed {kid}')
        current_count = 0

print(f'Last is {kids.popleft()}')






