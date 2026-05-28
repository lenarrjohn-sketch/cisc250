# =============================================================================
# Student Name: Michael Johnson
# Lab Title: Invoice Creator
# Date: 
# =============================================================================

# TASK 1: Nesting - Create a dictionary of dictionaries of the products being 
# purchased. Complete the nested dictionary below with the data in the lab 
# table.
product_list = {
    "el2234": { 
        "name": "Head Phones", 
        "category": "Electronics", 
        "price": 19.99, 
        "quantity": 2
    },
    "sh9989": {
        "name": "Running Shoes",
        "category": "Footwear",
        "price": 99.99,
        "quantity": 1
    },
    "ap0098": {
        "name": "Smart Toaster",
        "category": "Appliance",
        "price": 130.00,
        "quantity": 1
    },
    "cl3321": {
        "name": "Cotton Shirt",
        "category": "Clothing",
        "price": 10.00,
        "quantity": 4
    }
}
# Task 2.1: Create a dictionary to hold the customer data
customer = {"customer_name": "Hannah Davis", "loyalty_tier": "Gold"}


# Task 2.2: Print a processing order statement using an f string
# Print using f-string
print(f"Processing Order for: {customer['customer_name']} [{customer['loyalty_tier']} Tier Member]…")



# Task 3: Loop through dictionary with match-case discount calculations

for p in product_list.values():
    subtotal = p['price'] * p['quantity']

    match p['category']:
        case "Appliances":
            discount = subtotal * 0.20
        case "Clothing":
            discount = subtotal * 0.10
        case _:
            discount = 0

    print(f"{p['name']}: Subtotal ${subtotal}, Discount ${discount}, Final ${subtotal - discount}")

# Task 4: Subtotals, membership discounts, and final invoice total
 
# Customer data
customer = {"customer_name": "Hannah Davis", "tier": "Gold"}

# Initialize
totals = 0  

# Loop through each product to calculate subtotal, discount, and final price
for product in product_list.values():
    price = product["price"]
    quantity = product["quantity"]
    category = product["category"]
    
    subtotal = price * quantity
    
    # if-elif-else
    if category == "Appliances":
        discount_rate = 0.20
    elif category == "Clothing":
        discount_rate = 0.10
    else:
        discount_rate = 0.0  
    
    discount = subtotal * discount_rate  # Calculate discount amount
    final_price = subtotal - discount
    
    totals += final_price  

# Membership discount
tier = customer['tier']
if tier == "Platinum":
    member_discount_rate = 0.16
elif tier == "Gold":
    member_discount_rate = 0.11
elif tier == "Silver":
    member_discount_rate = 0.05
else:
    member_discount_rate = 0.0

# Calculate membership discount and final total
member_discount = totals * member_discount_rate
final_total = totals - member_discount

# Display 
print("Total after product discounts:", totals)
print("Membership discount (", tier, "Tier):", member_discount)
print("Final Total Owed:", final_total)