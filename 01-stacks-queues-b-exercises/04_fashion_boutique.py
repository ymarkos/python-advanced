"""
As an input --> huge box of clothes: each piece is an integer, use stack.
stack_clothes = [5 4 8 6 3 8 7 7 9]
rack_capacity = 16
current_rack_capacity = rack_capacity
count_rack = 1
While there are clothes:
    if there is no capacity:
        count_rack += 1
        current_rack_capacity = rack_capacity
    elif there is capacity:
        current_rack_capacity -= cloth
        remove the piece

print the count_rack

"""

# clothes_stack = [int(el) for el in input().split()]
clothes_stack = list(map(int, input().split()))

capacity_rack = int(input())
current_capacity = capacity_rack
count_rack = 1


while len(clothes_stack) >= 1:
    current_item = clothes_stack[-1]
    if current_item > current_capacity:
        current_capacity = capacity_rack
        count_rack += 1
        continue
    else:
        current_capacity -= current_item
        clothes_stack.pop()
print(count_rack)