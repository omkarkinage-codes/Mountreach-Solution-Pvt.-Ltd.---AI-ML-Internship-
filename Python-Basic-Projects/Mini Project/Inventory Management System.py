# Project 5: Inventory Management System

# Initialize dictionary 
inventory_db = {}


# Function to load data from text file 
def load_inventory():
    try:
        # Open file in read mode
        file = open("inventory.txt", "r")
        for line in file:
            # Strip newline and split by comma
            data = line.strip().split(",")
            if len(data) == 5:
                p_id, name, category, price, quantity = data

                inventory_db[p_id] = {
                    "name": name,
                    "category": category,
                    "price": float(price),
                    "quantity": int(quantity),
                }
        file.close()
        print("Inventory data loaded from inventory.txt")
    except FileNotFoundError:
        # If file doesn't exist, start with empty database safely
        print("No existing inventory file found. Starting fresh.")


# Function to save data to text file on exit
def save_inventory():
    file = open("inventory.txt", "w")
    for p_id, details in inventory_db.items():

        line = f"{p_id},{details['name']},{details['category']},{details['price']},{details['quantity']}\n"
        file.write(line)
    file.close()
    print("Inventory data saved to inventory.txt")


# Function to add a new product
def add_product():
    print("\nAdd New Product ")
    p_id = input("Enter Product ID (e.g., P001): ").strip().upper()

    # Unique Product ID enforcement
    if p_id in inventory_db:
        print("This Product ID already exists!")
        return

    name = input("Enter Product Name: ").strip()
    category = input("Enter Category: ").strip()
    price = float(input("Enter Unit Price (Rs.): "))
    quantity = int(input("Enter Initial Quantity: "))

    # Store inside nested structure
    inventory_db[p_id] = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
    }
    print(f"Product '{name}' added to inventory.")


# Function for Stock-In (Restocking)
def stock_in():
    print("\nStock-In (Add Stock) ")
    p_id = input("Enter Product ID: ").strip().upper()

    if p_id in inventory_db:
        qty_to_add = int(input("Enter quantity to add: "))
        if qty_to_add <= 0:
            print("Quantity must be greater than 0!")
            return

        # Add to existing quantity
        inventory_db[p_id]["quantity"] += qty_to_add
        print(f"Success: Added {qty_to_add} items. New Quantity: {inventory_db[p_id]['quantity']}")
    else:
        print("Product ID not found.")


# Function for Stock-Out (Sales)
def stock_out():
    print("\nStock-Out (Sell Stock) ")
    p_id = input("Enter Product ID: ").strip().upper()

    if p_id in inventory_db:
        qty_to_remove = int(input("Enter quantity to sell: "))
        if qty_to_remove <= 0:
            print("Quantity must be greater than 0!")
            return

        # Check stock level validation before stock-out
        if inventory_db[p_id]["quantity"] >= qty_to_remove:
            inventory_db[p_id]["quantity"] -= qty_to_remove

            print(f"Sold {qty_to_remove} items. Remaining Quantity: {inventory_db[p_id]['quantity']}")
        else:
            print(f"Insufficient stock! Available quantity is only {inventory_db[p_id]['quantity']}.")
    else:
        print("Product ID not found.")


#  Function to view all stock inventory details
def view_inventory():
    print("\nCurrent Inventory Status ")
    if not inventory_db:
        print("Inventory is empty.")
        return

    for p_id, details in inventory_db.items():
        print(f"ID: {p_id} | Name: {details['name']} | Category: {details['category']} | Price: Rs.{details['price']} | Qty: {details['quantity']}")


# Function to generate a simple total value calculation report
def generate_report():
    print("\nINVENTORY REPORT ")
    total_products = len(inventory_db)
    total_value = 0.0

    # Calculate sum of price x quantity for all items
    for p_id, details in inventory_db.items():
        total_value += details["price"] * details["quantity"]

    print(f"Total Unique Products : {total_products}")
    print(f"Total Stock Valuation : Rs. {total_value:.2f}")


# Run file 
load_inventory()

#  Main Interactive Menu Control Loop
while True:
    print("\nINVENTORY MANAGEMENT SYSTEM ")
    print("1. Add Product")
    print("2. Stock In (Restock)")
    print("3. Stock Out (Sale)")
    print("4. View Inventory")
    print("5. Valuation Report")
    print("6. Save & Exit")

    choice = input("Enter choice (1-6):- ").strip()

    if choice == "1":
        add_product()
    elif choice == "2":
        stock_in()
    elif choice == "3":
        stock_out()
    elif choice == "4":
        view_inventory()
    elif choice == "5":
        generate_report()
    elif choice == "6":
        # Save inventory to text 
        save_inventory()
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please choose a number from 1 to 6.")