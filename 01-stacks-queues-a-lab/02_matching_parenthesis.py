expression = input()

stack_index = []
for index in range(len(expression)):
    ch = expression[index]
    if ch == '(':
        stack_index.append(index)
    elif ch == ')':
        start_index = stack_index.pop()
        end_index = index + 1
        subexpression = expression[start_index:end_index]
        print(subexpression)