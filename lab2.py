# Name: Michael Johnson
#
#============================

# Question 1
#============
messy_menu = "    PizZA, burGER, SaLAd "
messy_menu = messy_menu.strip()
# Lowercase the entire string 
messy_menu = messy_menu.lower()
# Display 
print("Today's special menu list:", messy_menu)

# Question 2
#==========
# Even numbers from 2 to 50
numbers = list(range(2, 51, 2))

# Display the list
print(numbers)

# Print total number of items
print("Total items:", len(numbers))

# Print the sum of all numbers
print("Sum:", sum(numbers))

MULTIPLIER = 5

answer = MULTIPLIER * (max(numbers) + min(numbers))

print("Answer:", answer)

# Question 3
#==========
# Guest list with four names
guests = ["alex", "devon", "mike", "kim"]
print(guests)

# Add linus to the end
guests.append("linus")
print(guests)

# Add guido to the beginning
guests.insert(0, "guido")
print(guests)

# Sort the list
guests.sort()
print(guests)

# Create invitations list
invitations = [
    "You are invited, " + guests[0].capitalize() + "!",
    "You are invited, " + guests[1].capitalize() + "!",
    "You are invited, " + guests[2].capitalize() + "!",
    "You are invited, " + guests[3].capitalize() + "!",
    "You are invited, " + guests[4].capitalize() + "!",
    "You are invited, " + guests[5].capitalize() + "!"
]

print(invitations)

# Print the first three invitations
print(invitations[:3])
