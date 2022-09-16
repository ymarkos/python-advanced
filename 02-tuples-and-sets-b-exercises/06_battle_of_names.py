num = int(input())

even_names = set()
odd_names = set()

for it in range(1, num + 1):
    current_name = input()
    current_sum = 0
    for el in current_name:
        current_sum += ord(el)
    current_sum //= it
    if current_sum % 2 == 0:
        even_names.add(current_sum)
    else:
        odd_names.add(current_sum)

sum_even = sum(even_names)
sum_odd = sum(odd_names)

if sum_even == sum_odd:
    union = even_names & odd_names
    print(", ".join(map(str, union)))

elif sum_odd > sum_even:
    difference = odd_names - even_names
    print(", ".join(map(str, difference)))


elif sum_even > sum_odd:
    symmetric_diff = odd_names ^ even_names
    print(", ".join(map(str, symmetric_diff)))
