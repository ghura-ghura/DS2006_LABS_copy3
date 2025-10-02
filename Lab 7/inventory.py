import sys
import os
import time

def clear_console():
    """ Clears the terminal for Windows and Linux systems """
    os.system('cls' if os.name == 'nt' else 'clear')

#Keep track of inventory:
inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 20
}

inventory.update({"pear": 10})
inventory.update({"pineapple": 5})

menu_width = 59

menu_header = """
******************************************************************
********************* My Inventory *****************************
******************************************************************
*                                                                *
* Please choose one of the following options:                    *
*                                                                *
"""

menu_options = [
    "Add a new item to the inventory",
    "Remove an item from the inventory",
    "View the inventory",
    "View item quantity",
    "Exit"
]

options = "\n".join([f"*({i+1}) {option} {(menu_width - len(option)) * ' '}*" for i, option in enumerate(menu_options)])

menu = menu_header + options + "\n" + (menu_width + 7) * "*"

def game():
    clear_console()
    print(menu)

    choice = str(input("Enter your choice: "))

    match choice:
        case "1":
            item = str(input("Enter the item you want to add: "))
            if len(item) > 0:
                if item not in inventory:
                    quantity = int(input("Enter the quantity of the item: "))
                    inventory.update({item: quantity})
                    print(f"{item} added to the inventory")
                    time.sleep(1)
                else:
                    print("Item already exists")
                    time.sleep(1)
            else:
                print("Item name cannot be empty")
                time.sleep(1)
        case "2":
            item = str(input("Enter the item you want to remove: "))
            if len(item) > 0:
                if item in inventory:
                    inventory.pop(item)
                    print(f"{item} removed from the inventory")
                    time.sleep(1)
                else:
                    print("Item does not exist")
                    time.sleep(1)
            else:
                print("Item name cannot be empty")
                time.sleep(1)
        case "3":
            print(inventory)
            print("\nPress Enter to continue...")
            input()
        case "4":
            item = str(input("Enter the item you want to view the quantity of: "))
            if len(item) > 0:
                if item in inventory:
                    print(f"{item} has {inventory[item]} items")
                    time.sleep(1)
                else:
                    print("Item does not exist")
                    time.sleep(1)
            else:
                print("Item name cannot be empty")
                time.sleep(1)
        case _: # Handles invalid choices + case 5 (Exit)
            sys.exit()
    game()

if __name__ == "__main__":
    game()