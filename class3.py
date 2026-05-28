#Slide 5
#animals = ['doy', 'cat', 'cow', 'donkey', 'sheep']
#if 'cow' in animals:
#    print('moooo')
#    if 'pig' not in animals:
#        print('no pigs found')
#
#    age = 17
#    if age >= 18:
#        print("You are eligible to vote")
#    else:
#        print("Sorry, you are too young to vote.")
#        print("Please register to vote as soon as you turn 18!")

#Slide 6
# age = 17

# if age >= 18:
#     print("You are eligible to vote!")
# else:
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")

#Slide 9
# toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for topping in toppings:
#    if topping == 'green peppers':
#        print("Sorry, we are out of green peppers right now.")
#    else:
#        print(f"Adding {topping}.")
# print("\nFinished making your pizza!")

#Slide 11
# empty_list = []
# if empty_list: #means, if the list has in any items at all
#    print('The list contains at least one item')
# else:
#    print('The list is empty')

#Slide 13
# status = 403

# match status:
#     case 400:
#         print("Bad request")

#     case 401 | 403 | 404:
#         print("Not allowed")

#     case 418:
#         print("I'm a teapot")

#     case _:
#         print("Something's wrong with the internet")

#Slide 24
# person = {
#     'id': "m007",
#     'first': 'Michael',
#     'last': 'Johnson',
#     'title': 'Mr.',
#     'age': 20,
#     'married': True,
# }

# # Looping through the dictionary keys
# for k in person:
#     print(k)

# print(person)
# print(person.items())
# print(person.keys())
# print(person.values())

#Slide 27
# car_makers = {
#     'Rav4': 'Toyota',
#     'Swift': 'Suzuki',
#     'Vitz': 'Toyota',
#     'Tucson': 'Hyundai'
# }

# for maker in car_makers.values():
#     print(maker)

# print('No duplicates below:')
# for maker in set(car_makers.values()):
#     print(maker)

#Slide 33
# favorite_languages = {
#     'jen': ['python', 'java'],
#     'sarah': ['swift'],
#     'edward': ['c#', 'go', 'c++'],
#     'phil': ['python', 'kotlin'],
# }

# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are:")

#     for language in languages:
#         print(f"\t{language.title()}")