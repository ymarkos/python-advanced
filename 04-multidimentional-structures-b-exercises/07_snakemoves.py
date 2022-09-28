rows, cols = [int(x) for x in input().split()]

word = input()
idx = 0
for row in range(rows):
    elements = [None] * cols
    if row % 2 == 0:
        for index in range(cols):
            ch = word[idx % len(word)]
            elements[index] = ch
            idx += 1
    else:
        for index in range(cols - 1, -1, -1):
            elements[index] = word[idx % len(word)]
            idx += 1
    print("".join(elements))
