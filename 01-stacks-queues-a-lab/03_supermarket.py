"""
queue

loop:
    add input to queue
    if input is 'Paid':
        print an empty queue
    if input is 'End':
        print remaining
"""

from collections import deque

customers = deque()
while True:
    command = input()
    if command == 'End':
        print(f'{len(customers)} people remaining.')
        break
    elif command == 'Paid':
        while customers:
            print(customers.popleft())
    else:
        customers.append(command)
