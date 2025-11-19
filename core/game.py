# This is where the game happens
import os
import sys
import time
from core.model.elements import element_chart
from core.model.elements import element_constructor
from core.model import status_effects as status_effect

# Set Player Name 
def set_player_name():
    time.sleep(1)
    player_name = str(input(f"\nGreetings, Player! What is your name (Type in your name)? "))
    while (True):
        # Getting Player name
        time.sleep(1)        
        
        # Confirm Player name
        print(f"\nYour name is {player_name}, is that correct? \n1. Yes \n2. No")
        choice = str(input("\nEnter your choice: "))
        
        if (choice == "1"):
            return player_name
        elif (choice == "2"):
            player_name = str(input(f"\nWhat is your name, then? "))
        else:
            print("\nInvalid Input!")
            
# Set Player Type
def set_player_type(player_name):
    time.sleep(1)
    print("\nAvailable Types:")
    for i, type_name in enumerate(element_chart, start=1):
        print(f"{i}. {type_name.title()}")
    print(f"{(i+1)}. Back")
    
    while (True):    
        player_type = str(input(f"\nType in your Character Element for {player_name}: ").lower())
           
        if player_type in element_chart: 
            time.sleep(1)
            # Confirm Player Type           
            print(f"\nYour have selected {player_type}, is that correct? \n1. Yes \n2. No (Choose Again)")
            while (True):
                choice = str(input("\nEnter your choice: "))                       
                if (choice == "1"):
                    return player_type
                elif (choice == "2"):
                    break
                else:
                    print("\nInvalid Input!")

        elif (player_type == "back"):
            game_mode_select()
        else:
            print("Invalid Input!")
            
# Game Menu

# Run menu
def run_menu():
    os.system('cls' if os.name == "nt" else 'clear')
    
    time.sleep(1)
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
    time.sleep(0.5)
    os.system('cls' if os.name == "nt" else 'clear')
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

    # Getting Player name
    
    time.sleep(1)
    
    # Player One
    print("\n===== Player One =====")
    player_one_name = set_player_name()
    player_one_type = set_player_type(player_one_name)
    print(f"\nYou are {player_one_name}. You are of the {player_one_type} element!")
    
    time.sleep(2)
    
    os.system('cls' if os.name == "nt" else 'clear')
    time.sleep(1)
                     
    # Player Two
    print("\n===== Player Two =====")
    player_two_name = set_player_name()
    player_two_type = set_player_type(player_two_name)
    print(f"\nYou are {player_two_name}. You are of the {player_two_type} element!")
    
    # Creates the player characters
    player_one = element_constructor[player_one_type](player_one_name, 10, player_one_type)
    player_two = element_constructor[player_two_type](player_two_name, 10, player_two_type)  
    
    # Clears Terminal for PVP initiation
    time.sleep(2)
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

    
    
    
    