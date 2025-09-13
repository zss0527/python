# -------INPUT-------
# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)

# name = input("Please enter your name: ")
# print(f"\nHello, {name}!")

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
# name = input(prompt)
# print(f"\nHello, {name}!")

# age = input("How old are you? ")
# age = int(age)  # convert string to integer
# if age >= 18:
#     print("You are old enough to vote!")
# else:
#     print("Sorry, you are too young to vote.")


# -------WHILE LOOP-------
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1 

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message.lower() != 'quit':
#     message = input(prompt)
#     if message.lower() != 'quit':
#         print(message) 

# use a flag to control the loop
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message.lower() == 'quit':
#         active = False
#     else:
#         print(message)

# while True:
#     message = input(prompt)
#     if message.lower() == 'quit':
#         break
#     else:
#         print(message)

# use continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
# remove all instances of specific values from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# fill a dictionary with user input
responses = {}
# set a flag to indicate that polling is active
polling_active = True
while polling_active:
    # prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # store the response in the dictionary
    responses[name] = response
    # find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False
# polling is complete. show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")    