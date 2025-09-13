message = "Hello Python World!"
print(message)
message = "Hello Python Crash Course World!"
print(message)

# ---------String in python----------
str1 = 'I told my friend, "Python is my favorite language!"'
print(str1)
str2 = "One of Phthon's strengths is its diverse community."
print(str2)

name = "method in sTring"
print(name.title())
print(name.upper())
print(name.lower())

#use variable in string
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

#use \t and \n in string
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#remove space in string
favorite_language = ' python '
print(favorite_language)
print(favorite_language.rstrip())
print(favorite_language.lstrip())
print(favorite_language.strip())

#remove prefix
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

universe_age = 14_000_000_000
print(universe_age)

x, y, z = 0,3,2
print(x, y, z)

MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)


