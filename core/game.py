# This is where the game happens

import sys
from core.model.character import Character
from core.model.character import StatusEffect
from core.model.elements import FireElement
from core.model.elements import element_chart
from core.model import status_effects as status_effect

# Run menu
def run_menu():
    print("\nWelcome to Element Battle!")
    print("1. Start")
    print("2. Exit")    
    
    while (True):
        choice = str(input("Please choose an option: "))
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
    print("1. Player versus Player")
    print("2. Player versus CPU")
    print("3. Endless Mode")
    print("4. Back")
    while (True):
        choice = str(input("\nChoose an option: "))
        if (choice == "1"): 
            print("\nYou have selected Player vs Player")
            pvp_select()
            break
        elif (choice == "2"):
            print("\nYou have selected Player vs CPU")
            pass
        elif (choice == "3"):
            print("\nYou have selected Endless Mode")
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
    
    #initiates pvp
    pvp(player_one, player_two)
    
def pvp(player_one, player_two):
    print("\n=====================")
    print("Player vs Player")
    print(f"{player_one.get_character_name()} vs {player_two.get_character_name()}!")
    print("=====================\n")

    # Game loop
    # Adds another loop for when players wants to rematch
    while (True):
        # resets the player's stats, allowing rematch
        player_one.reset_stats()
        player_two.reset_stats()
        turn = 1
        while (player_one.get_hp() > 0 and player_two.get_hp() > 0):
            
            print(f"===== Turn {turn} =====")

            # --- Player One's Turn ---
            player_one.next_Turn(player_two)
            
            # Check if Player Two is defeated
            if (player_two.get_hp() <= 0):
                print(f"\n{player_two.get_character_name()} has fainted!")
                print(f"{player_one.get_character_name()} Wins!\n")
                break

            # --- Player Two's Turn ---
            player_two.next_Turn(player_one)

            # Check if Player One is defeated
            if (player_one.get_hp() <= 0):
                print(f"\n{player_one.get_character_name()} has fainted!")
                print(f"{player_two.get_character_name()} Wins!\n")
                break
            turn += 1
            print()  # Spacing
            
    # Asks the players to either restart the game or go back to menu
        print("\nContinue?")
        print("\n1. Rematch\n2. Back to menu\n3. Exit")
        
        choice = str(input("\nEnter your choice: "))
        if (choice == "1"):
            continue # Continues through the loop, resetting player stats
        elif (choice == "2"):
            game_mode_select()
            break
        elif (choice == "3"):
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid input!")
      
# Testing: Will remove at a later update
def test():
    player_one = FireElement("player_one_test", 10, "fire")
    player_two = FireElement("player_two_test", 10, "fire")
    pvp(player_one, player_two)

    
    
    
    