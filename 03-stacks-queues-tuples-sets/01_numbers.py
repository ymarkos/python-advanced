set_a = {int(x) for x in input().split()}
set_b = {int(x) for x in input().split()}
num_command = int(input())

for _ in range(num_command):
    data = input().split()
    command = data[0:2]
    if data[0] == 'Check':
        if set_a.issubset(set_b) or set_b.issubset(set_a):
            print(True)
        else:
            print(False)
    elif command == ['Add', 'First']:
        numbers = [int(x) for x in (data[2:])]
        for num in numbers:
            set_a.add(num)
    elif command == ['Add', 'Second']:
        numbers = [int(x) for x in (data[2:])]
        for num in numbers:
            set_b.add(num)
    elif command == ['Remove', 'First']:
        numbers = [int(x) for x in (data[2:])]
        for num in numbers:
            if num in set_a:
                set_a.remove(num)
    elif command == ['Remove', 'Second']:
        numbers = [int(x) for x in (data[2:])]
        for num in numbers:
            if num in set_b:
                set_b.remove(num)
set_a = sorted(set_a)
set_b = sorted(set_b)

print(", ".join(map(str, set_a)))
print(", ".join(map(str, set_b)))


