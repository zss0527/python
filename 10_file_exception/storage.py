from pathlib import Path
import json

numbers =  list(range(1,200))

path = Path('10_file_exception/storage.json')
contents = json.dumps(numbers)

print(contents)
path.write_text(contents)

contents = path.read_text()
numbers = json.loads(contents)

print(numbers)


username = input("What is your name? ")
path = Path('10_file_exception/username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"We'll remember you when you come back, {username}!")

contents = path.read_text()
username = json.loads(contents)
print(f"Welcome back, {username}!")