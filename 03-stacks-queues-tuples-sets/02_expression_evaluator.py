from collections import deque

elements = input().split()
numbers = deque()

for element in elements:
    # element is an operator
    if element in '*+-/':
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()
            result = 0
            if element == '*':
                result = first * second
            elif element == '+':
                result = first + second
            elif element == '-':
                result = first - second
            else:
                result = first // second

            numbers.appendleft(result)

    else:
        # element is a number
        numbers.append(int(element))

print(numbers.popleft())
