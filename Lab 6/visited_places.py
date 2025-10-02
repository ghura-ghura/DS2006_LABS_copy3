import os
import time
import sys

def clear_console():
    """ Clears the terminal for Windows and Linux systems """
    os.system('cls' if os.name == 'nt' else 'clear')

def file_exists(file_name):
    return os.path.exists(file_name)

def write_to_file(file_name, content, remove = False, replace = False):
    if isinstance(content, list):
        content_str = "\n".join(content)
    else:
        content_str = str(content)

    mode = "w" if not file_exists(file_name) or replace else "r" if remove else "a"

    with open(file_name, mode, encoding="utf-8") as file:
        if remove:
            file_content = file.read()
            new_content = file_content.replace(content_str, "")
            file.seek(0)
            file.write(new_content)
            file.truncate()
        else:
            file.write("\n" + content_str if not replace else content_str)
    
menu_width = 59

menu_header = """
******************************************************************
********************* My Travel List *****************************
******************************************************************
*                                                                *
* Please choose one of the following options:                    *
*                                                                *
"""

view_visited_cities_header = """
******************************************************************
********************* My Travel List *****************************
******************************************************************
*                                                                *
* Visited cities:                                                *
*                                                                *
"""

menu_options = [
    "Add a new city to the list of visited cities",
    "View your list of visited cities",
    "Sort the list of visited cities",
    "Shows the number of visited cities",
    "Remove a given city from the list of visited cities",
    "Remove all cities from the list of visited cities",
    "Save the list of visited cities to a file"
]

options = "\n".join([f"*({i+1}) {option} {(menu_width - len(option)) * ' '}*" for i, option in enumerate(menu_options)])

menu = menu_header + options + "\n" + (menu_width + 7) * "*"

file_name = "visited_cities.txt"
visited_cities = [] if not file_exists(file_name) else [city.strip() for city in open(file_name, "r").readlines() if city.strip()]

def game(menu, file_name, visited_cities):
    clear_console()
    print(menu)


    choice = str(input("Enter your choice: "))

    match choice:
        case "1":
            city = str(input("Enter the city you want to add: "))
            
            if len(city) > 0:
                visited_cities.append(city)
                print(f"{city} added to the list")
                time.sleep(0.5)
            else:
                print("City name cannot be empty")
                time.sleep(0.5)
        case "2":
            clear_console()
            if visited_cities:
                visited_cities_str = "\n".join([f"*({i+1}) {city} {(menu_width - len(city)) * ' '}*" for i, city in enumerate(visited_cities)])
                visited_cities_menu = view_visited_cities_header + visited_cities_str + "\n" + (menu_width + 7) * "*"
                print(visited_cities_menu)
            else:
                print("No cities in your list yet!")
            input("\nPress Enter to continue...")
        case "3":
            if visited_cities:
                visited_cities.sort()
                print("Visited cities sorted alphabetically")
            else:
                print("No cities to sort!")
            time.sleep(0.5)
        case "4":
            print(f"You have visited {len(visited_cities)} cities")
            time.sleep(1)
        case "5":
            if visited_cities:
                city = str(input("Enter the city you want to remove: "))
                
                if len(city) > 0:
                    if city in visited_cities:
                        visited_cities.remove(city)
                        print(f"{city} removed from the list")
                    else:
                        print(f"{city} is not in the list")
                else:
                    print("City name cannot be empty")
            else:
                print("No cities in your list to remove!")
            time.sleep(0.5)
        case "6":
            if visited_cities:
                should_clear = str(input("Are you sure you want to remove all cities? (y/n): "))
                
                if should_clear.lower() == "y" or should_clear == "":
                    visited_cities.clear()
                    print("All cities removed from the list")
                else:
                    print("Operation cancelled")
            else:
                print("No cities in your list to remove!")
            time.sleep(0.5)
        case "7": 
            write_to_file(file_name, visited_cities, remove=False, replace=True)
            if visited_cities:
                print(f"List of {len(visited_cities)} cities saved to {file_name}")
            else:
                print(f"Empty list saved to {file_name} (file cleared)")
            time.sleep(0.5)
        case _:
            sys.exit()
    game(menu, file_name, visited_cities)     

if __name__ == "__main__":
    game(menu, file_name, visited_cities)