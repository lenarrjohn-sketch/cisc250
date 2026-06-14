# =============================================================================
# Student Name: Michael Johnson
# Lab Title: Lab 5
# Date:
# =============================================================================


# 1.1 Create a Product class
class Product:
    """A product in the inventory."""

    def __init__(self, name, price, stock=0):
        """Create a product."""
        # Store the product name
        self.name = name
        # Store the product price
        self.price = price
        # Store the product stock amount
        self.stock = stock

    # 1.3 Display 
    def display_details(self):
        """Show product details"""
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Stock: {self.stock}")

    def update_stock(self, quantity):
        """Update the stock amount"""
        if self.stock + quantity >= 0:
            self.stock = self.stock + quantity
        else:
            print("Stock cannot go below 0.")


# 2.1 Create child class that inherits from Product
class DigitalProduct(Product):
    """Digital product"""

    # 2.2 Create constructor/initializer method with three parameters
    def __init__(self, name, price, download_link):
        """Create a digital product."""
        super().__init__(name, price, 9999)
        # Store the download link
        self.download_link = download_link

    # 2.3 
    def display_details(self):
        """Show digital product details."""
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")
        print(f"Download Link: {self.download_link}")


# 3.1 Create objects
product = Product("Laptop", 20, 10)
digital = DigitalProduct("Python Course", 150, "www.download.com")


# Before update
print("Before update")
product.display_details()

# Add stock
product.update_stock(5)
print("After adding 5")
product.display_details()

# Decrement it but above zero
product.update_stock(-8)
print("After removing 8")
product.display_details()

# Decrement it 
product.update_stock(-20)
print("After removing 20")
product.display_details()

# Display digital product
print("Digital Product")
digital.display_details()