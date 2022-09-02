def is_vip(guest):
    return guest[0].isdigit()


num_reservations = int(input())

vip_guest = set()
regular_guest = set()

for _ in range(num_reservations):
    reservation = input()
    if is_vip(reservation):
        vip_guest.add(reservation)
    else:
        regular_guest.add(reservation)

while True:
    coming_guest = input()
    if coming_guest == 'END':
        break
    if is_vip(coming_guest):
        vip_guest.remove(coming_guest)
    else:
        regular_guest.remove(coming_guest)

number = len(vip_guest) + len(regular_guest)
if number > 0:
    print(number)
else:
    print(0)
[print(guest) for guest in sorted(vip_guest)]
[print(guest) for guest in sorted(regular_guest)]
