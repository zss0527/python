#--------python list-------
bicycles = ['trek', 'cannondale', 'redline', 'specialized']

# ger item from list
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
print(bicycles[-2])

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# update item in list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# add item to list
motorcycles.append('ducati')
print(motorcycles)

# insert item to list
motorcycles.insert(0, 'ducati')
print(motorcycles)

# delete item from list
del motorcycles[0]
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('yamaha')
print(motorcycles)

# manage list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))

cars.reverse()
print(cars)
print(len(cars))