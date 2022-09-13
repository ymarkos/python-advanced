"""
Receive as an input int quantity of the food
A queue with the int amounts of each order
Print the biggest order
enough_food = True
For loop --> number of orders -->Star serving food:
    if not enough quantity:
        enough_food = False
        stop
    else:
        remove order
        reduce quantity

if not enough_food:
    print(f'Orders left: {order1} {order2} .... {orderN}')
else:
    print(f'Orders complete')


"""
from collections import deque

enough_food = True
quantity = int(input())
orders_queue = deque(int(el) for el in input().split())
orders_left = orders_queue.copy()
max_order = (max(orders_queue))

for num_order in range(len(orders_queue)):
    current_order = orders_queue[num_order]
    if quantity < current_order:
        enough_food = False
        break
    else:
        quantity -= current_order
        orders_left.popleft()

print(max_order)
if not enough_food:
    print(f'Orders left:', end=' ')
    for order in orders_left:
        print(order, end=' ')
else:
    print(f'Orders complete')

# from collections import deque
#
# tot_amount = int(input())
#
# orders = deque(int(el) for el in input().split())
#
# while len(orders) >= 1:
#     current_customer = orders[0]
#     if tot_amount < current_customer:
#         break
#     else:
#         tot_amount -= current_customer
#         orders.popleft()
#
# print(max(orders))
#
# if len(orders) == 0:
#     print('Orders complete')
# else:
#     remaining = [str(el) for el in orders]
#     print(f'Orders left: {" ".join(remaining)}')