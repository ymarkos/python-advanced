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

stack_clothes = [int(piece) for piece in input().split()]

rack_capacity = int(input())
current_rack_capacity = rack_capacity
count_rack = 1
while len(stack_clothes) >= 1:
    current_piece = stack_clothes[-1]
    if current_piece > current_rack_capacity:
        count_rack += 1
        current_rack_capacity = rack_capacity
    else:
        current_rack_capacity -= current_piece
        stack_clothes.pop()
print(count_rack)