# ------IF STATEMENTS------
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    elif car.lower() != 'audi':
        print(car.title())

ageList = list(range(1, 11))
ageBetween3And5 = []
ageList1 = []
ageOther = []

for age in ageList:
    if age <= 5 and age >= 3:
        ageBetween3And5.append(age)
    elif age <= 2 or (age >=6 and age <=8):
        ageList1.append(age)
    else:
        ageOther.append(age)
print(ageBetween3And5)
print(ageList1)
print(ageOther)

# IN, NOT IN
names = ['alice', 'bob', 'carol', 'david']
if 'alice' in names:
    print("Alice is in the list.")
if 'eve' not in names:
    print("Eve is not in the list.")
if 'bob' in names and 'carol' in names:
    print("Both Bob and Carol are in the list.")

# JUDGE LIST IS EMPTY OR NOT
requested_toppings = []
if requested_toppings:
    for topping in requested_toppings:
        print(f"Adding {topping}.")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("Finished making your pizza!")
