original_data = input()
data_stack = []
for ch in original_data:
    # push into the stack
    data_stack.append(ch)

reversed_data = ''
while data_stack:
    reversed_data += data_stack.pop()  # pop the top
print(reversed_data)