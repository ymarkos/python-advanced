'''
read initial water quantity
append people into a queue
loop until End:

    if command == 'refill ...':
        add water to quantity
    else:
        if water enough:
            remove water from quantity

        remove person from a queue
'''
from collections import deque

quantity_dispenses = int(input())
people = deque()
while True:
    name = input()
    if name == 'Start':
        break
    people.append(name)

while True:
    data = input().split()
    command = data[0]
    if command == 'End':
        print(f'{quantity_dispenses} liters left')
        break
    elif command == 'refill':
        quantity_dispenses += int(data[1])
    else:
        liters = int(command)
        current_person = people.popleft()
        if liters <= quantity_dispenses:
            quantity_dispenses -= liters
            print(f'{current_person} got water')
        else:
            print(f'{current_person} must wait')
