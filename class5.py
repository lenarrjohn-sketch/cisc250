# Slide 17 ==========
#def greet_user():
#    """Display a simple greeting."""
#    print("Hello!")
#greet_user()

# Slide 18 =========
# This will cause a NameError: name 'greet' is not defined greet() 
# def greet(): 
#     print("Hello, world!")

# Slide 20 =========
# Added username variable as a function parameter
# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello, {username.title()}!")

# greet_user('jesse')

# Slide 23 =========
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet('hamster', 'harry')

# describe_pet('hamster', 'harry')

# Slide 29 ==========
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# Slide 32 ========
# def build_person(first_name, last_name, age=None):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}

#     if age:
#         person['age'] = age

#     return person

# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# Slide 34 ========
# def greet_users(names):
#     """Print a simple greeting to each user in the list."""
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)

# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

# Slide 36 ========
# Start with some designs that need to be printed
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design until none are left
# # Move each design to completed_models after printing
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# # Display all completed models
# print("\nThe following models have been printed:")

# for completed_model in completed_models:
#     print(completed_model)

# Slide 37 =======
# def print_models(unprinted_designs, completed_models):
#     """
#     Simulate printing each design until none are left.
#     Move each design to completed_models after printing.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)


# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)


# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)  # can copy list here
# show_completed_models(completed_models)

# Slide 34 ========
# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make."""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")


# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Slide 42 ========
# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info


# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# print(user_profile)