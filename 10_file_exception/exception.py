from pathlib import Path


# ---------ZeroDivisonError--------------
try:
    5/0
except ZeroDivisionError:
    print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(f"{first_number} divided by {second_number} is {answer}")


path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    print(contents)

def count_words(file_path):
    """Count the approximate number of words in a file."""
    try:
        contents = file_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # print(f"Sorry, the file {file_path} does not exist.")
        # keep calm and carry on
        pass
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {file_path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', '10_file_exception/receive.txt','moby_dick.txt']
for filename in filenames:
    path = Path(filename)
    count_words(path)

