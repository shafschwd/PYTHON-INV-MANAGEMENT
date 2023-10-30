# PYTHON-IMS


## To-Do List

### User Management System
- [x] Create a User Management System.
- [x] Users of the program need to have a valid User ID and Password.
- [x] Store all user details in the `users.txt` file.
- [x] User details should include User ID, Password, and UserType (admin or staff).
- [x] Implement validation for User ID and Password.
- [x] Admins should have the ability to create, modify, and search for users.

### Initial Inventory Creation
- [x] Create an Initial Inventory System.
- [x] Store all item details in the `ppe.txt` file.
- [x] Item details should include Item Code, Supplier Code, and Quantity in stock (measured in the number of boxes).
- [x] PPE items should be received, recorded, and distributed in boxes.
- [x] Each item is supplied by exactly one supplier.
- [x] One supplier can supply more than one type of item.
- [x] Implement validation for Supplier Codes.
- [x] Ensure there are a minimum of three hospitals.
- [x] Store hospital details in the `hospitals.txt` file.
- [ ] Inventory creation is a one-time process initialized at the start of the program.
- [x] Allow a maximum of four suppliers.
- [x] Create a `suppliers.txt` file for storing and updating supplier details.

### Searching Functionalities
- [ ] Implement search and print functionalities.
- [ ] Allow users to search for details of item distribution for any particular item.
- [ ] Allow users to search for details of items received from any particular supplier.
- [ ] Create options to filter and display results.

### Hospital and Supplier Creation
#### Supplier Data
- [x] Initialize Supplier Data.
- [x] Write supplier data to a text file.
- [x] Implement editing capabilities for the `supplier.txt` file.

#### Hospital Data
- [x] Initialize Hospital Data.
- [x] Write hospital data to a text file.

## Item Inventory Management
- [x] Implement Item Inventory Management.
- [x] Include item inventory tracking.
- [x] Display available quantity of items stored in ascending order by Item Code.
- [x] Maintain records of all items with a stock quantity of less than 25 boxes.
- [x] Allow tracking of the available quantity of a particular item.
- [x] Implement tracking of items received during a certain period (startDate to endDate).

