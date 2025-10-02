import random
import msvcrt

def get_random_integer(end):
    """
    Roll a dice with a given number of sides.
    Returns:
        int: a random number between 1 and the number of given sides
    """
    return random.randint(1, end)

def roll_d4():
    """ Roll a 4 sided dice """
    return get_random_integer(4)

def roll_d6():
    """ Roll a 6 sided dice """
    return get_random_integer(6)

def roll_d8():
    """ Roll a 8 sided dice """
    return get_random_integer(8)

def roll_d12():
    """ Roll a 12 sided dice """
    return get_random_integer(12)

def roll_d20():
    """ Roll a 20 sided dice """
    return get_random_integer(20)

def roll_d100():
    """ Roll a 100 sided dice """
    return get_random_integer(100)

SIDES = 20

# Keyboard interrupt keys
# Ctl+C = b'\x03'
# Escape = b'\x1b'
KEYBOARD_INTERRUPT_KEYS = [b'\x03', b'\x1b']

if __name__ == "__main__":
    while (True):
        key = msvcrt.getch()
        
        if key in KEYBOARD_INTERRUPT_KEYS:
            print("Program terminated")
            break

        if key != b'\r': # Wait for the user to press Enter
            continue
        
        res = get_random_integer(SIDES)

        # Show the rolled number
        print(f"You rolled a {SIDES} sided dice and got a {res}")
   
