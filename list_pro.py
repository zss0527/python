# ------FOR LOOP------
magicians = ['david copperfield', 'criss angel', 'penn and teller']
for magician in magicians:
    print(magician)

    print(f"{magician.title()}, that was a great trick!")
print("Thank you, everyone. That was a great magic show!")

# methods to create list
age = range(1, 5) #age is not list now
print(age)
for value in age:
    print(value)
# use list() and range() to make a list
numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

# list comprehension
squares_comprehension = [value ** 2 for value in range(1, 11)]
print(squares_comprehension)

# slice list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:]) # last 3 items

# loop through a slice
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# copy a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favorite foods are:")
print(my_foods) 
print("My friend's favorite foods are:")
print(friend_foods) 

# assign a list to another list will not copy it, but create a reference
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
print("My favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favorite foods are:")
print(my_foods)
print("My friend's favorite foods are:")
print(friend_foods)

# tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 250 # error, tuple is immutable
for dimension in dimensions:
    print(dimension)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)
