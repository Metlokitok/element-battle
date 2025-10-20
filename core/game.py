# This is where the game happens

import sys
from core.model.character import Character
from core.model.elements import FireElement
from core.model.elements import element_chart


# Run menu
def run_menu():
    print("\nWelcome!")
    print("1. Start")
    print("2. Exit")    
    
    while (True):
        choice = str(input("Choose an option: "))
        if (choice == "1"): 
            break
        elif (choice == "2"):
            print("Exiting...")
            sys.exit()
        else:
            print("invalid input!")
    game_mode_select()
    
def game_mode_select():
    print("\nSelect a game mode:")
    print("1. Player versus player")
    print("2. Player versus CPU")
    print("3. Endless mode")
    print("4. Back")
    while (True):
        choice = str(input("Choose an option: "))
        if (choice == "1"): 
            pvp_select()
        elif (choice == "2"):
            pass
        elif (choice == "3"):
            pass
        elif (choice == "4"):
            run_menu()
        else:
            print("invalid input!")


# Player vs player select
def pvp_select():
    while (True):
        # Getting Player name
        player_one_name = str(input(f"\nGreetings, Player One! What is your name? "))
        
        # Player Type selection
        print("\nAvailable Types:")
        for i, type_name in enumerate(element_chart, start=1):
            print(f"{i}. {type_name.title()}")
        print(f"{(i+1)}. Back")
        
        while (True):
            player_one_type = str(input(f"\nType in your Character Element for {player_one_name}: ").lower())
            if player_one_type in element_chart:
                print(f"\nYou are {player_one_name}. You are of the {player_one_type} element!")
                break
            elif (player_one_type == "back"):
                game_mode_select()
            else:
                print("Please select from the options above!")
        break
            
    while (True):
        #Getting Player name
        player_two_name = str(input(f"\nGreetings, Player Two! What is your name? "))
        
        # Player Type selection
        print("\nAvailable Types:")
        for i, type_name in enumerate(element_chart, start=1):
            print(f"{i}. {type_name.title()}")
        print(f"{(i+1)}. Back")
        
        while (True):
            player_two_type = str(input(f"\nType in your Character Element for {player_two_name}: ").lower())
            if player_two_type in element_chart:
                print(f"\nYou are {player_two_name}. You are of the {player_two_type} element!")
                break
            elif (player_one_type == "back"):
                game_mode_select()
            else:
                print("Please select from the options above!")
        break
    
    player_one = FireElement(player_one_name, 10, player_one_type)
    player_two = FireElement(player_two_name, 10, player_two_type)  
    
    pvp(player_one, player_two)
    # Will try to think where I'd put the level system
    
def pvp(player_one, player_two):
    print("\n=====================")
    print("Player vs Player")
    print(f"{player_one.get_character_name()} vs {player_two.get_character_name()}!")
    print("=====================\n")

    # Game loop
    while (player_one.get_hp() > 0 and player_two.get_hp() > 0):
        turn = 1
        print(f"===== Turn {turn} =====")

        # --- Player One's Turn ---
        player_one.display_status()
        player_one.next_Turn(player_two)
        
        # Check if Player Two is defeated
        if (player_two.get_hp() <= 0):
            print(f"\n{player_two.get_character_name()} has fainted!")
            print(f"{player_one.get_character_name()} Wins!\n")
            sys.exit()
            break

        # --- Player Two's Turn ---
        player_two.display_status()
        player_two.next_Turn(player_one)

        # Check if Player One is defeated
        if (player_one.get_hp() <= 0):
            print(f"\n{player_one.get_character_name()} has fainted!")
            print(f"{player_two.get_character_name()} Wins!\n")
            sys.exit()
            break

        turn += 1
        print()  # Spacing

        

def test():
    player_one = FireElement("player_one_test", 10, "fire")
    player_two = FireElement("player_two_test", 10, "fire")
    pvp(player_one, player_two)