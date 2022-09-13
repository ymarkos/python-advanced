"""
create an empty stack
input - int
for _ in n times receive queries:
    if queries == 1:
        push the number int into the stack
    elif queries == 2:
        delete the number at the top of the stack
    elif queries == 3:
        print the maximum number in the stack
    elif queries == 4:
        print the minimum number in the stack
print the stack from to the top to the bottom
"""
# 1st option
numbers = []
num_queries = int(input())

for _ in range(num_queries):
    data = input().split()
    query = int(data[0])
    if query == 1:
        number = int(data[1])
        numbers.append(number)
    elif query == 2 and len(numbers) >= 1:
        numbers.pop()
    elif query == 3 and len(numbers) >= 1:
        print(max(numbers))
    elif query == 4 and len(numbers) >= 1:
        print(min(numbers))

numbers_reversed = []
while numbers:
    numbers_reversed.append(str(numbers.pop()))
print(', '.join(numbers_reversed))

# # 2nd option
#
# n = int(input())
# stack = []
#
# for _ in range(n):
#     command = input()
#     query = command[0]
#     if query == '1':
#         stack.append(int(command.split()[1]))
#     elif query == '2':
#         if stack:
#             stack.pop()
#     elif query == '3':
#         if stack:
#             print(max(stack))
#     elif query == '4':
#         if stack:
#             print(min(stack))
#
# stack_length = len(stack)
# for idx in range(len(stack)):
#     spacing = ', ' if idx < len(stack) - 1 else ''
#     print(str(stack.pop()) + spacing, end="")
