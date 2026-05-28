#Slide 4
# prompt = "If you share your name, we can personalize the "
# prompt += "messages you see.\nWhat is your first name? "

# name = input(prompt)

# print(f"\nHello, {name}!")

#Slide 5
# age = input("How old are you? ")

# # Convert the string value to an integer
# age = int(age)

# if age >= 21:
#     print("You can legally drink alcohol in the US. Drink responsibly!")
# else:
#     print("You can't legally buy alcohol in the US.")

#Slide 13
# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end the program.\nInput > "

# active = True  # Initialize the flag variable to True

# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False  # Toggle the flag variable to False
#     else:
#         print(message)  # Only print the message if it is not 'quit'

#Slide 17
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# # Check if the list is not empty
# while unconfirmed_users:
#     print(f"Number of unconfirmed users: {len(unconfirmed_users)}")

#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")

#     confirmed_users.append(current_user)

# # Display all confirmed users
# print("\nThe following users have been confirmed:")

# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

#Slide 17
# responses = {}

# # Set a flag to indicate that polling is active
# polling_active = True

# while polling_active:
#     # Prompt for the person's name and response
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")

#     # Store the response in the dictionary
#     responses[name] = response

#     # Ask if another person wants to respond
#     repeat = input("Would you like to let another person respond? (yes/no) ")

#     if repeat == 'no':
#         polling_active = False

# # Polling is complete. Show the results.
# print("\n--- Poll Results ---")

# for name, response in responses.items():
#     print(f"{name} would like to climb {response}.")