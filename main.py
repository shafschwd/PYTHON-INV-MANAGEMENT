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
        password = input("Enter the new password: ")
        user_type = input("Enter the new user type (admin or staff): ")

        if user_type not in ['admin', 'staff']:
            print("Invalid user type. User not modified.")
            return

        user_data[username]['password'] = password
        user_data[username]['user_type'] = user_type
        print("User details modified successfully!")
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

# Main program
if __name__ == "__main__":
    user_data = read_user_data()

    while True:
        print("\nLogin System")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        user = authenticate_user(user_data, username, password)
        if user:
            print(f"Welcome, {username} ({user['user_type']})!")

            if user['user_type'] == 'admin':
                while True:
                    print("\nAdmin Menu:")
                    print("1. Create User")
                    print("2. Modify User")
                    print("3. Search User")
                    print("4. Logout")

                    choice = input("Enter your choice: ")

                    if choice == "1":
                        create_user(user_data)
                    elif choice == "2":
                        modify_user(user_data)
                    elif choice == "3":
                        search_user(user_data)
                    elif choice == "4":
                        write_user_data(user_data)
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("You do not have admin privileges.")
                break
        else:
            print("Invalid username or password. Please try again.")
