# Import necessary modules
import csv

# Function to read user data from the users.txt file
def read_user_data():
    user_data = []
    with open("users.txt", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            user_data.append(row)
    return user_data

# Function to authenticate a user
def authenticate_user(username, password):
    user_data = read_user_data()
    for user in user_data:
        if user[1] == username and user[2] == password:
            return user
    return None

# Main login system
def login_system():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        user = authenticate_user(username, password)
        if user:
            user_id, username, _, user_type = user
            print(f"Welcome, {username} ({user_type})!")
            return user_id, user_type
        else:
            print("Invalid username or password. Please try again.")

# Main inventory management system
def inventory_management(user_id, user_type):
    if user_type == "admin":
        print("You are logged in as an admin.")
        # Add admin-specific functionality here
    elif user_type == "staff":
        print("You are logged in as a staff member.")
        # Add staff-specific functionality here

# Main program
if __name__ == "__main__":
    print("Inventory Management System")
    user_id, user_type = login_system()
    inventory_management(user_id, user_type)
