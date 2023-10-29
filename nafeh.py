def create_hospital():
    # Input hospital details
    with open("hospitals.txt", "w") as hospital_file:
      pass
    hospital_code = input("Enter Hospital Code: ")
    hospital_name = input("Enter Hospital Name: ")
    # You can include other relevant details here

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
    # Check if the hospital code is unique by reading existing hospitals from hospitals.txt
    with open("hospitals.txt", "r") as hospital_file:
        for line in hospital_file:
            code, _ = line.strip().split(',')
            if code == hospital_code:
                return False
    return True

# Example usage:
create_hospital()
