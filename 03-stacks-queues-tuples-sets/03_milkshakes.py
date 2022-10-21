from collections import deque


chocolate = [int(x) for x in input().split(', ')]
milk = deque([int(x) for x in input().split(', ')])

enough_milkshakes = False
milkshakes = 0

max_length = 0
if len(chocolate) >= len(milk):
    max_length = len(chocolate)
else:
    max_length = (len(milk))
max_length *= max_length

for _ in range(max_length*10):
    if chocolate and milk:
        current_amount_chocolate = chocolate[-1]
        current_cup_milk = milk[0]
        if current_amount_chocolate <= 0:
            chocolate.pop()
            continue
        if current_cup_milk <= 0:
            milk.popleft()
            continue
        if current_amount_chocolate == current_cup_milk:
            chocolate.pop()
            milk.popleft()
            milkshakes += 1
            if milkshakes >= 5:
                enough_milkshakes = True
                break
        else:
            milk.append(milk.popleft())
            current_amount_chocolate -= 5
    else:
        break

if enough_milkshakes:
    print(f'Great! You made all the chocolate milkshakes needed!')
else:
    print(f'Not enough milkshakes.')


if len(chocolate) >= 1:
    print(f'Chocolate: {", ".join(map(str, chocolate))}')
else:
    print(f'Chocolate: empty')

if len(milk) >= 1:
    print(f'Milk: {", ".join(map(str, milk))}')

else:
    print(f'Milk: empty')