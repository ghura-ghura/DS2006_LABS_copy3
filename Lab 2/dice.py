import random
import msvcrt

def get_random_integer(end):
    """ Returns a random integer between 1 and end """
    return random.randint(1, end)

# Define the dice sides
SIDES = 20

# Keyboard interrupt keys in ASCII
# Ctl+C = b'\x03'
# Escape = b'\x1b'
KEYBOARD_INTERRUPT_KEYS = [b'\x03', b'\x1b']


def main():
    """ Main function """
    first_roll = True
    if first_roll:
        print(f"Welcome to the game of dice! Press Enter to roll a {SIDES} sided dice!")
        first_roll = False
    
    while (True):
        key = msvcrt.getch()
        
        if key in KEYBOARD_INTERRUPT_KEYS:
            print("Program terminated")
            break


        # Await Enter key before rolling the dice
        if key != b'\r':
            continue

        # Roll the dice
        result = get_random_integer(SIDES)

        # Show the result
        print(f"You rolled a {SIDES} sided dice and got a {result}")

# Only run the main function if the script is run directly
if __name__ == "__main__":
    main()
