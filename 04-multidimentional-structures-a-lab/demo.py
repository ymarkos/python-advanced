rows, columns = [int(el) for el in input().split(', ')]


mm = []
tot_sum = 0
for _ in range(rows):
    current_row = [int(el) for el in input().split(', ')]
    mm.append(current_row)

for el in mm:
    tot_sum += sum(el)

print(tot_sum)
print(mm)





