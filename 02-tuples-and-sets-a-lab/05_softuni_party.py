num_guests = int(input())
invited_guests = {input() for _ in range(num_guests)}

while True:
    coming_guest = input()
    if coming_guest == 'END':
        break
    elif len(coming_guest) == 8 and coming_guest in invited_guests:
        invited_guests.remove(coming_guest)

vip_guests = set()
regular_guests = set()
for guest in invited_guests:
    if guest[0].isdigit():
        vip_guests.add(guest)
    else:
        regular_guests.add(guest)
if invited_guests:
    print(len(invited_guests))
else:
    invited_guests = 0
    print(invited_guests)
if vip_guests:
    vip_guests_sorted = sorted(vip_guests)
    for guest in vip_guests_sorted:
        print(guest)
if regular_guests:
    regular_guests_sorted = sorted(regular_guests)
    for guest in regular_guests_sorted:
        print(guest)



