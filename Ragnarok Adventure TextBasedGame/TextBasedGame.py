# TextBasedGame.py
# Justin Carlo Florida
# Ragnarok X themed text based adventure game

def show_instructions():
    """Print the game title and available commands."""
    print("======================================")
    print("        Ragnarok Adventure Game       ")
    print("======================================")
    print("Story:")
    print("Baphomet is gathering dark power in Glast Heim.")
    print("Travel through Rune Midgard, collect all items,")
    print("then enter Glast Heim to defeat Baphomet.")
    print()
    print("Commands:")
    print("  go <Direction>   (example: go North)")
    print("  get <Item Name>  (example: get Balmung)")
    print("  exit             (quit the game)")
    print("======================================")
    print()


def show_status(current_room, inventory, rooms):
    """Show the player's current room, inventory, and any item in the room."""
    print("--------------------------------------")
    print("You are in:", current_room)
    print("Inventory:", inventory)

    room_item = rooms[current_room]['item']
    if room_item is not None:
        print("You see:", room_item)
    else:
        print("There is no item in this room.")
    print("--------------------------------------")


def create_rooms():
    """Create and return the rooms dictionary for the Ragnarok map."""
    rooms = {
        'Prontera': {
            'North': 'Geffen',
            'East': 'Payon',
            'West': 'Izlude',
            'South': 'Morroc',
            'item': None
        },
        'Geffen': {
            'South': 'Prontera',
            'item': 'Muspellium'
        },
        'Izlude': {
            'East': 'Prontera',
            'North': 'Byalan Island',
            'item': "Valkyrie's Armor"
        },
        'Byalan Island': {
            'South': 'Izlude',
            'item': 'Balmung'
        },
        'Payon': {
            'West': 'Prontera',
            'South': 'Payon Cave',
            'item': 'Lunatic Heart Necklace'
        },
        'Payon Cave': {
            'North': 'Payon',
            'West': 'Morroc',
            'item': "Murphy's Shoes"
        },
        'Morroc': {
            'North': 'Prontera',
            'East': 'Payon Cave',
            'West': 'Sphinx',
            'item': 'Majestic Goat'
        },
        'Sphinx': {
            'East': 'Morroc',
            'South': 'Glast Heim',
            'item': "Murphy's Cloak"
        },
        'Glast Heim': {
            'North': 'Sphinx',
            # Villain room. There is no collectible item here.
            'item': 'Baphomet'
        }
    }

    return rooms


def main():
    """Main function that runs the full game."""
    rooms = create_rooms()

    # Count how many collectible items exist in the game
    total_items = 0
    for room_name, room_data in rooms.items():
        item = room_data['item']
        # Count only non None items, but ignore the villain in Glast Heim
        if item is not None and room_name != 'Glast Heim':
            total_items += 1

    current_room = 'Prontera'
    inventory = []

    show_instructions()

    # Gameplay loop
    while True:
        show_status(current_room, inventory, rooms)

        command = input("Enter your move: ")
        print()  # blank line for readability

        # Clean and split the command
        command = command.strip()
        if command == "":
            print("You did not enter a command.")
            continue

        # Allow simple "exit"
        if command.lower() == 'exit':
            print("You chose to leave your quest. Thanks for playing.")
            break

        words = command.split()

        # The first word is the verb (go, get, etc.)
        verb = words[0].lower()

        if verb == 'go':
            if len(words) < 2:
                print("Go where? Please enter a direction.")
                continue

            direction = words[1].capitalize()  # North, South, East, West

            # Check if the direction is valid from this room
            if direction in rooms[current_room]:
                next_room = rooms[current_room][direction]
                current_room = next_room

                # Check if player entered the villain room
                if current_room == 'Glast Heim':
                    if len(inventory) == total_items:
                        print("You step into Glast Heim fully prepared.")
                        print("With all your gear gathered, you defeat Baphomet!")
                        print("Congratulations, you collected all items and won the game.")
                    else:
                        print("You enter Glast Heim unprepared...")
                        print("Baphomet overwhelms you with dark power.")
                        print("You did not collect all the items in time.")
                        print("GAME OVER.")
                    break  # game ends after entering Glast Heim
            else:
                print("You cannot go that way from here.")

        elif verb == 'get':
            if len(words) < 2:
                print("Get what? Please enter the name of the item.")
                continue

            # Rebuild the item name from the rest of the words
            typed_item = " ".join(words[1:]).lower()

            room_item = rooms[current_room]['item']

            if room_item is None or current_room == 'Glast Heim':
                print("There is no item you can pick up in this room.")
            else:
                # Compare case insensitive
                if typed_item == room_item.lower():
                    if room_item in inventory:
                        print("You already picked up that item.")
                    else:
                        inventory.append(room_item)
                        rooms[current_room]['item'] = None
                        print("You picked up:", room_item)
                        # Optional: show how many items are collected
                        print("Items collected:", len(inventory), "of", total_items)
                else:
                    print("That item is not in this room.")
                    print("Tip: type the item name exactly as shown.")

        else:
            print("Invalid command.")
            print("Use 'go <Direction>', 'get <Item Name>', or 'exit'.")

    print("Thanks for playing the Ragnarok Adventure Game.")


# Run the game
if __name__ == "__main__":
    main()
