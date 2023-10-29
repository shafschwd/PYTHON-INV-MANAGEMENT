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


# Function to track the total quantity of all items sorted by quantity
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
    print(f"Item with code {item_code} not found")


def track_items_received_in_period():
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    with open("transactions.txt", "r") as transactions_file:
        for line in transactions_file:
            item_code, _, quantity, transaction_type, transaction_date = line.strip().split(',')
            if (transaction_type == "Received" and
                start_date <= transaction_date <= end_date):
                print(f"Item Code: {item_code}, Quantity: {quantity}, Date-Time: {transaction_date}")


# Function for user login
def login(user_data):
    while True:
        print("\nLogin System")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        user = authenticate_user(user_data, username, password)
        if user:
            print(f"Welcome, {username} ({user['user_type']})!")

            if user['user_type'] == 'admin':
                admin_menu(user_data)
            else:
                staff_menu(user_data)

            user_continue = input("Do you want to continue (Y/N)? ").strip().lower()
            if user_continue != 'y':
                break
        else:
            print("Invalid username or password. Please try again.")


# Function for admin menu
def admin_menu(user_data):
    while True:
        print("\nUser Management Menu:")
        print("1. Create User")
        print("2. Modify User")
        print("3. Search User")
        print("4. Delete User")
        print("5. Display All Users")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_user(user_data)
        elif choice == "2":
            modify_user(user_data)
        elif choice == "3":
            search_user(user_data)
        elif choice == "4":
            username = input("Enter the username to delete: ")
            delete_user(user_data, username)
        elif choice == "5":
            display_users()
        elif choice == "6":
            print("Returning to the main menu.")
            break
        else:
            print("Invalid choice. Please try again.")


# Function for staff menu
def staff_menu(user_data):
    while True:
        print("\nStaff Menu:")
        print("1. Search User")
        print("2. Display All Users")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            search_user(user_data)
        elif choice == "2":
            display_users()
        elif choice == "3":
            write_user_data(user_data)
            print("Logged out.")
            break
        else:
            print("Invalid choice. Please try again.")


# Function to read user data from the users.txt file
def read_user_data():
    user_data = {}
    with open("users.txt", "r") as file:
        for line in file:
            user_id, username, password, user_type = line.strip().split(',')
            user_data[username] = {
                'user_id': user_id,
                'password': password,
                'user_type': user_type,
            }
    return user_data


# Function to write user data back to the users.txt file
def write_user_data(user_data):
    with open("users.txt", "w") as file:
        for username, details in user_data.items():
            user_id = details['user_id']
            password = details['password']
            user_type = details['user_type']
            file.write(f"{user_id},{username},{password},{user_type}\n")


# Function to authenticate a user
def authenticate_user(user_data, username, password):
    if username in user_data and user_data[username]['password'] == password:
        return user_data[username]
    return None


# Function for admin to create a new user
def create_user(user_data):
    user_id = str(len(user_data) + 1)
    username = input("Enter the new username: ")
    password = input("Enter the new password: ")
    user_type = input("Enter the user type (admin or staff): ")

    if user_type not in ['admin', 'staff']:
        print("Invalid user type. User not created.")
        return

    user_data[username] = {
        'user_id': user_id,
        'password': password,
        'user_type': user_type,
    }
    print("User created successfully!")


# Function for admin to modify a user's details
def modify_user(user_data):
    username = input("Enter the username to modify: ")
    if username in user_data:
        user = user_data[username]
        password = input("Enter the new password (leave blank to keep the current password): ")
        user_type = input("Enter the new user type (admin or staff): ")
        new_username = input("Enter the new username (leave blank to keep the current username): ")

        if user_type not in ['admin', 'staff']:
            print("Invalid user type. User not modified.")
            return

        if password:
            user['password'] = password
        if user_type:
            user['user_type'] = user_type
        if new_username and new_username != username:
            user_data[new_username] = user
            del user_data[username]

        write_user_data(user_data)
        print(f"User details modified successfully.")
    else:
        print("User not found.")


# Function for admin to search for a user
def search_user(user_data):
    username = input("Enter the username to search: ")
    if username in user_data:
        print(f"User ID: {user_data[username]['user_id']}")
        print(f"User Type: {user_data[username]['user_type']}")
    else:
        print("User not found.")


# Function to delete a user
def delete_user(user_data, username):
    if username in user_data:
        del user_data[username]
        write_user_data(user_data)
        print(f"{username} has been deleted.")
    else:
        print("User not found.")


# Function to display all users
def display_users():
    with open("users.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            user_id, username, _, user_type = line.strip().split(',')
            print(f"User ID: {user_id}, Username: {username}, User Type: {user_type}")


'''# User management system
if __name__ == "__main__":
    user_data = read_user_data()
    login(user_data)'''
#distribute_items_to_hospital()
receive_items_from_supplier()

