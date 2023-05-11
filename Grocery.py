# create an empty grocery list
grocery_list = []


# function to add an item to the grocery list
def add_item(item_name, quantity):
    # add the item and quantity to the grocery list as a tuple
    grocery_list.append((item_name, quantity))
    print(f"{quantity} {item_name} added to the grocery list.")

# function to remove an item from the grocery list
def remove_item(item_name):
    # search for the item in the grocery list
    for item in grocery_list:
        if item[0] == item_name:
            # remove the item if it exists in the grocery list
            grocery_list.remove(item)
            print(f"{item_name} removed from the grocery list.")
            return
    print(f"{item_name} not found in the grocery list.")

# function to view the grocery list
def view_list():
    print("Grocery List:")
    for item in grocery_list:
        print(f"{item[0]}: {item[1]}")

# main loop for the program
while True:
    print("\nWhat would you like to do?")
    print("1. Add item to grocery list")
    print("2. Remove item from grocery list")
    print("3. View grocery list")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        item_name = input("Enter the name of the item: ")
        quantity = int(input("Enter the quantity: "))
        add_item(item_name, quantity)

    elif choice == "2":
        item_name = input("Enter the name of the item to remove: ")
        remove_item(item_name)

    elif choice == "3":
        view_list()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")