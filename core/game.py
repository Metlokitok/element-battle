# This is where the game happens
import os
import sys
import time
from core.model.elements import element_chart
from core.model.elements import element_constructor
from core.model import status_effects as status_effect

# Run menu
def run_menu():
    print("\nWelcome to Element Battle!")
    time.sleep(1)
    print("\n1. Start")
    print("2. Exit")    
    
    while (True):
        choice = str(input("Please choose an option: "))
        if (choice == "1"): 
            break
        elif (choice == "2"):
            print("Exiting...")
            time.sleep(1)
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
        time.sleep(1)
        choice = str(input("\nChoose an option: "))
        if (choice == "1"): 
            print("\nYou have selected Player vs Player")
            time.sleep(1)
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
    # clears terminal
    os.system('cls' if os.name == "nt" else 'clear')
    
    time.sleep(1)
    print("===== Player vs Player =====")
    while (True):
        # Getting Player name
        time.sleep(1)
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
            
    time.sleep(1)
    
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
            if player_two_type in element_constructor:
                print(f"\nYou are {player_two_name}. You are of the {player_two_type} element!")
                break
            elif (player_one_type == "back"):
                game_mode_select()
            else:
                print("Please select from the options above!")
        break
    
    # Creates the player characters
    player_one = element_constructor[player_one_type](player_one_name, 10, player_one_type)
    player_two = element_constructor[player_two_type](player_two_name, 10, player_two_type)  
    
    # Clears Terminal for PVP initiation
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    #initiates pvp
    pvp(player_one, player_two)
    
def pvp(player_one, player_two):
    
    time.sleep(1)
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
            time.sleep(1)
            print(f"===== Turn {turn} =====")
            
            # --- Player One's Turn ---
            time.sleep(1)
            player_one.next_Turn(player_two)
            
            # Check if Player One is defeated via DoT
            if (player_one.get_hp() <= 0):
                time.sleep(1)
                print(f"\n{player_one.get_character_name()} has fainted!")
                print(f"{player_two.get_character_name()} Wins!\n")
                break
            
            # Check if Player Two is defeated
            if (player_two.get_hp() <= 0):
                time.sleep(1)
                print(f"\n{player_two.get_character_name()} has fainted!")
                print(f"{player_one.get_character_name()} Wins!\n")
                break

            # --- Player Two's Turn ---
            time.sleep(1)
            player_two.next_Turn(player_one)

            # Check if Player One is defeated
            if (player_one.get_hp() <= 0):
                time.sleep(1)
                print(f"\n{player_one.get_character_name()} has fainted!")
                print(f"{player_two.get_character_name()} Wins!\n")
                break
            
            # Check if Player Two is defeated via DoT
            if (player_two.get_hp() <= 0):
                time.sleep(1)
                print(f"\n{player_two.get_character_name()} has fainted!")
                print(f"{player_one.get_character_name()} Wins!\n")
                break
            
            # Increment Turn Number
            turn += 1
            
            time.sleep(2)
            
            # Clears Terminal for readability
            os.system('cls' if os.name == 'nt' else 'clear')
            
            # print()  # Spacing (Remove if not needed)
                   
    # Asks the players to either restart the game or go back to menu
        time.sleep(1)
        print("\nContinue?")
        print("\n1. Rematch\n2. Back to menu\n3. Exit")
        
        while (True):
            choice = str(input("\nEnter your choice: "))
            if (choice == "1"):
                time.sleep(1)
                break # Continues through the loop, resetting player stats
            elif (choice == "2"):
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
                time.sleep(1)
                game_mode_select()
                break
            elif (choice == "3"):
                print("Exiting...")
                time.sleep(1)
                sys.exit()
            else:
                print("Invalid input!")
      
# Testing: Will remove at a later update
def test():
    player_one = element_constructor["fire"]("Player One", 10, "fire")
    player_two = element_constructor["fire"]("Player Two", 10, "fire")
    pvp(player_one, player_two)

    
    
    
    