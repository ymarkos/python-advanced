data = input()

occurrences = {}
for el in data:
    if el not in occurrences:
        occurrences[el] = 0
    occurrences[el] += 1


for el, count in sorted(occurrences.items()):
    print(f'{el}: {count} time/s')

