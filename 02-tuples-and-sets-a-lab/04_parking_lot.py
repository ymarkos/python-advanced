num = int(input())

existing_cars = set()
cars_string = [input() for _ in range(num)]

for car in cars_string:
    in_out, number_car = car.split(", ")
    if in_out == 'IN' and number_car:
        existing_cars.add(number_car)
    elif number_car in existing_cars:
        existing_cars.remove(number_car)

if existing_cars:
    for car in existing_cars:
        print(car)
else:
    print(f'Parking Lot is Empty')