# =============================================================================
# Student Name: Michael Johnson
# Lab Title: Lab 4 - Food Truck Order Queue
# Date:
# =============================================================================

# Task 1.1: Create two lists
order_queue = []

menu = [
    "burger",
    "hot dog",
    "fries",
    "fried chicken wings",
    "buffalo wings",
    "soda",
    "bottled water",
    "local drink"
]
# Task 1.2: Display a welcome message and create an infinite while loop
# Display a welcome message
print("---- Welcome to the Food Truck ----")

# Infinite loop for taking orders
while True:

    print("\nType 'menu' to see what is available.")
    print("Type 'done' to complete your order.")
    print("Please enter items one at a time.")

    user_input = input("Enter a food item > ").lower()

# Task 2: Setup user input
    #2.2 If user is done ordering
    if user_input == "done":
        break

    #2.3  If the user input is empty (press enter only), continue to the start of the loop
    elif user_input == "":
        continue

    # Show the menu
    elif user_input == "menu":
        print("\nPlease choose from this menu:")
        
        for item in menu:
            print("", item)

        continue

    #2.4 Check if the user input is on the menu
    elif user_input not in menu:
        print("Invalid choice.")
        continue

    #2.5 If it is on the menu, find out how many of that item is requested, then append the item 
    #to the order queue list multiple times based on quantity requested. Update the display that 
    #the quantity of that each item was added.
    else: # meaning that it is in the menu
        try:
            quantity_input = input(f"How many {user_input} would you like > ")
            quantity = int(quantity_input) 

        except ValueError:
            print("Invalid quantity entered. Choose again.")
            continue

        else:
            # Add item multiple times based on quantity
            for i in range(quantity):
                order_queue.append(user_input)

            print(f"Added {user_input} x {quantity} to order queue.")


# Task 3: Process the order queue

# Display original queue
print(f"\nOriginal Order Queue: {order_queue}")

print("\n--- Processing Orders ---")


while order_queue:

    item = order_queue.pop(0)

    print(f"Fulfilling: {item} ({len(order_queue)} items remaining)")

print("\nAll order entries were fulfilled successfully.")