'''
occurrences_dict
loop values:
    occurrences_dict[value] +=1
'''

number_strings = input()
occurrences_count = {}
numbers = [float(num) for num in number_strings.split()]
for number in numbers:
    if number not in occurrences_count:
        occurrences_count[number] = 0
    occurrences_count[number] +=1


for key, value in occurrences_count.items():
    print(f'{key:.1f} - {value} times')
