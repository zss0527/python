from pathlib import Path
import os

print(os.getcwd())

path = Path('10_file_exception/pi_digits.txt')


# ---------READ FROM FILE---------
contents = path.read_text()
print(contents)

# read by line
for line in contents.splitlines():
    print(line)

pi_string = ''
lines = contents.splitlines()
for line in lines:
    pi_string += line.strip()

print(f"\n{pi_string}")
print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


# ---------WRITE INTO FILE---------
path = Path('10_file_exception/receive.txt')
path.write_text("I love programming.\n")

contents = 'I love creating new games.\n'
contents += "I also love finding meaning in large datasets.\n"
contents += "I love creating apps that can run in a browser.\n"
path.write_text(contents)

