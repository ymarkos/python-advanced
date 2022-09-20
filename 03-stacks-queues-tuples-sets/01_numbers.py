set_a = {int(x) for x in input().split()}
set_b = {int(x) for x in input().split()}
num_command = int(input())

for _ in range(num_command):
    data = input().split()
    command = data[0:2]
    if command == ['Add', 'First']:
        [set_a.add(int(x)) for x in data[2:]]

    elif command == ['Add', 'Second']:
        [set_b.add(int(x)) for x in data[2:]]

    elif command == ['Remove', 'First']:
        [set_a.remove(int(x)) for x in data[2:] if int(x) in set_a]

    elif command == ['Remove', 'Second']:
        [set_b.remove(int(x)) for x in data[2:] if int(x) in set_b]

    else:
        print(set_a.issubset(set_b) or set_b.issubset(set_a))


print(*sorted(set_a), sep=', ')
print(*sorted(set_b), sep=', ')


