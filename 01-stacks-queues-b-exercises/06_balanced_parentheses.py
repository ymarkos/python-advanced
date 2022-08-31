data = input()

data_stack = []
count = 0
for el in data:
    if el == "{":
        count -= 1
        data_stack.append(el)
    elif el == "[":
        count -= 1
        data_stack.append(el)
    elif el == "(":
        count -= 1
        data_stack.append(el)
    if el == ")" and data_stack[-1] == "(":
        count += 1
        data_stack.pop()
    elif el == "]" and data_stack[-1] == "[":
        count += 1
        data_stack.pop()
    elif el == "}" and data_stack[-1] == '{':
        count += 1
        data_stack.pop()

if count == 0:
    print('YES')
else:
    print('NO')