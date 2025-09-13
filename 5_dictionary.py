# -------DICTIONARY-------
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
print(f"empty alien_0: {alien_0}")
alien_0['color'] = 'green'
alien_0['points'] = 5
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(f"inited alien_0: {alien_0}")

# UPDATE VALUE IN DICTIONARY
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# MOVE THE ALIEN
alien_0['speed'] = 'medium'
print(f"Original x_position: {alien_0['x_position']}")
# move the alien to the right
# determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else: # fast
    x_increment = 3
# the new position is the old position plus the increment
alien_0['x_position'] += x_increment
print(f"New x_position: {alien_0['x_position']}")

# DELETE KEY-VALUE PAIR
print(alien_0)
del alien_0['points']
print(alien_0)

# DICTIONARY WITH LIST
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print(favorite_languages)
print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.")

# USE GET TO ACCESS VALUE
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# LOOP THROUGH ALL KEY-VALUE PAIRS
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',       
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# LOOP THROUGH ALL THE KEYS IN A DICTIONARY
for name in favorite_languages.keys():
    print(name.title())
print("\n")
# same as above
for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# LOOP THROUGH A DICTIONARY'S KEYS IN ORDER
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# LOOP THROUGH ALL VALUES IN A DICTIONARY
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# use set() to get unique values
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# NESTING
# list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# make 30 green aliens
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
# show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")
# change the first 3 aliens to yellow and medium speed
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
# show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")

# list in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
print(f"You ordered a {pizza['crust']}-crust pizza ""with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite language is {languages[0].title()}.")
# dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")


