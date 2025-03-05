# Jake's Escape the Room Game

# Initialize variables
has_key = False  # Tracks if the player has found the key

# Function to describe the room
def describe_room():
    print("\nYou are in a dimly lit room. You see a dusty bookshelf, a locked drawer, and a window.")
    

# Function to check if the player can open the drawer
def open_drawer():
    global has_key
    if has_key:
        print("Congratulations! You've escaped the room!")
        return True
    else:
        print("The drawer is locked.")

# Function to examine the bookshelf
def examine_bookshelf():
    global has_key
    print("The bookshelf is filled with old, leather-bound books. One book seems slightly out of place.")
    #ask the user if to examine the books
    user_input = input("Do you want to examine the book? (yes/no): ").lower()
    if user_input == "yes":
        print("You found a small key!")
    else:
        print("The user didn't examine the bookshelf.")
    has_key = True

# Function to look out the window
def look_out_window():
    print("You see a dark alleyway.")

# Function to handle user input and interactions
def handle_input():
    while True:
        # Describe the room at the start of each loop
        describe_room()

        # Ask the player for their action
        user_input = input("\nWhat do you want to do? (open drawer/examine bookshelf/look out window/): ").lower()

        # Handle different user inputs
        if user_input == "examine bookshelf":
            examine_bookshelf()
        elif user_input == "open drawer":
            if open_drawer():
                break  # Player has escaped, exit the loop
        elif user_input == "look out window":
            look_out_window()
        else:
            print("I don't understand that action.")

# Main function to start the game
def start_game():
    handle_input()

# Start the game
start_game()