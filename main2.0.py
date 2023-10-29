def create_hospital():
    # Input hospital details
    hospital_code = input("Enter Hospital Code: ")
    hospital_name = input("Enter Hospital Name: ")

    # Check if the hospital code is unique
    if not is_hospital_code_unique(hospital_code):
        print("Hospital with the same code already exists.")
        return

    # Create a new hospital entry
    new_hospital = f"{hospital_code},{hospital_name}\n"

    # Append the new hospital entry to the hospitals.txt file
    with open("hospitals.txt", "a") as hospital_file:
        hospital_file.write(new_hospital)

    print("Hospital created successfully!")


def is_hospital_code_unique(hospital_code):
    try:
        with open("hospitals.txt", "r") as hospital_file:
            for line in hospital_file:
                parts = line.strip().split(',')
                if len(parts) >= 1 and parts[0] == hospital_code:
                    return False
    except FileNotFoundError:
        print("File not found: hospitals.txt")
    return True


def create_supplier():
    # Input supplier details
    supplier_code = input("Enter Supplier Code: ")
    supplier_name = input("Enter Supplier Name: ")

    # Check if the supplier code is unique
    if not is_supplier_code_unique(supplier_code):
        print("Supplier with the same code already exists.")
        return

    # Create a new supplier entry
    new_supplier = f"{supplier_code},{supplier_name}\n"

    # Append the new supplier entry to the suppliers.txt file
    with open("suppliers.txt", "a") as suppliers_file:
        suppliers_file.write(new_supplier)

    print("Supplier created successfully!")


def is_supplier_code_unique(supplier_code):
    try:
        with open("suppliers.txt", "r") as suppliers_file:
            for line in suppliers_file:
                parts = line.strip().split(',')
                if len(parts) >= 1 and parts[0] == supplier_code:
                    return False
    except FileNotFoundError:
        print("File not found: suppliers.txt")
    return True


def receive_items_from_supplier():

    # Input supplier details and item information
    supplier_code = input("Enter Supplier Code: ")
    item_code = input("Enter Item Code: ")
    quantity_received = int(input("Enter Quantity Received: "))

    # Check if the supplier code and item code are valid
    if not is_supplier_code_valid(supplier_code):
        print("Invalid Supplier Code.")
        return
    if not is_item_code_valid(item_code):
        print("Invalid Item Code.")
        return

    # Update inventory with received items
    update_inventory(item_code, quantity_received)

    # Record the transaction in transactions.txt
    record_transaction(item_code, supplier_code, quantity_received, "Received")

    print("Items received and inventory updated successfully!")


def distribute_items_to_hospital():

    # Input hospital details and item information
    hospital_code = input("Enter Hospital Code: ")
    item_code = input("Enter Item Code: ")
    quantity_distributed = int(input("Enter Quantity Distributed: "))

    # Check if the hospital code and item code are valid
    if not is_hospital_code_valid(hospital_code):
        print("Invalid Hospital Code.")
        return
    if not is_item_code_valid(item_code):
        print("Invalid Item Code.")
        return

    # Check if there is enough quantity in stock
    if not is_quantity_sufficient(item_code, quantity_distributed):
        print("Insufficient quantity in stock.")
        return

    # Update inventory with distributed items
    update_inventory(item_code, -quantity_distributed)

    # Record the transaction in transactions.txt
    record_transaction(item_code, hospital_code, quantity_distributed, "Distributed")

    print("Items distributed and inventory updated successfully!")

# function to check if the supplier code is valid
def is_supplier_code_valid(supplier_code):
    try:
        with open("suppliers.txt", "r") as suppliers_file:
            for line in suppliers_file:
                parts = line.strip().split(',')
                if len(parts) >= 1 and parts[0] == supplier_code:
                    return True
    except FileNotFoundError:
        print("File not found: suppliers.txt")
    return False

# Function to check if a hospital code is valid
def is_hospital_code_valid(hospital_code):
    try:
        with open("hospitals.txt", "r") as hospitals_file:
            for line in hospitals_file:
                parts = line.strip().split(',')
                if len(parts) >= 1 and parts[0] == hospital_code:
                    return True
    except FileNotFoundError:
        print("File not found: hospitals.txt")
    return False

# Function to check if an item code is valid
def is_item_code_valid(item_code):
    try:
        with open("ppe.txt", "r") as ppe_file:
            for line in ppe_file:
                parts = line.strip().split(',')
                if len(parts) >= 3 and parts[0] == item_code:
                    return True
    except FileNotFoundError:
        print("File not found: ppe.txt")
    return False

# Function to check if there is sufficient quantity of an item in stock
def is_quantity_sufficient(item_code, quantity_distributed):
    try:
        with open("ppe.txt", "r") as ppe_file:
            for line in ppe_file:
                parts = line.strip().split(',')
                if len(parts) >= 3 and parts[0] == item_code:
                    quantity_in_stock = int(parts[2])
                    return quantity_in_stock >= quantity_distributed
    except FileNotFoundError:
        print("File not found: ppe.txt")
    return False

# Function to update the inventory with a change in quantity
def update_inventory(item_code, quantity_change):
    # Update the inventory in ppe.txt with the new quantity
    updated_lines = []
    with open("ppe.txt", "r") as ppe_file:
        for line in ppe_file:
            code, supplier_code, quantity_in_stock = line.strip().split(',')
            if code == item_code:
                quantity_in_stock = str(int(quantity_in_stock) + quantity_change)
            updated_lines.append(f"{code},{supplier_code},{quantity_in_stock}\n")

    with open("ppe.txt", "w") as ppe_file:
        ppe_file.writelines(updated_lines)

# Function to record a transaction
def record_transaction(item_code, target_code, quantity, transaction_type):
    # Record the transaction in transactions.txt
    transaction_details = f"{item_code},{target_code},{quantity},{transaction_type},{get_current_datetime()}\n"
    with open("transactions.txt", "a") as transactions_file:
        transactions_file.write(transaction_details)

# Function to get the current date and time in a specific format
def get_current_datetime():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to track the total quantity of all items sorted by item code
def track_total_quantity_sorted_by_item_code():
    items = []

    try:
        with open("ppe.txt", "r") as ppe_file:
            for line in ppe_file:
                try:
                    code, _, quantity = line.strip().split(',')
                    items.append((code, int(quantity)))
                except ValueError:
                    print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print("File not found: ppe.txt")

    items.sort(key=lambda x: x[0])  # Sort by item code
    for item in items:
        print(f"Item Code: {item[0]}, Quantity: {item[1]}")

# Function to track items with low quantities
def track_low_quantity_items(threshold=25):
    try:
        with open("ppe.txt", "r") as ppe_file:
            for line in ppe_file:
                try:
                    code, _, quantity = line.strip().split(',')
                    quantity = int(quantity)
                    if quantity < threshold:
                        print(f"Item Code: {code}, Quantity: {quantity}")
                except ValueError:
                    print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print("File not found: ppe.txt")

# Function to track the quantity of a specific item
def track_quantity_for_item():
    item_code = input("Enter the item code you want to track: ")

    try:
        with open("ppe.txt", "r") as ppe_file:
            for line in ppe_file:
                try:
                    code, _, quantity = line.strip().split(',')
                    if code == item_code:
                        print(f"Item Code: {code}, Quantity: {quantity}")
                        return
                except ValueError:
                    print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print("File not found: ppe.txt")
    print(f"Item with code {item_code}")



# main logic
# receive_items_from_supplier()
# distribute_items_to_hospital()
# create_hospital()
# create_supplier()
# track_total_quantity_sorted_by_item_code()
# track_low_quantity_items()
# track_quantity_for_item()
# track_items_received_in_period()
