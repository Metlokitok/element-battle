# Element subclasses
# Single file containing multiple subclasses (Element Types). Will split into multiple files if it gets large
# Each subclass will have 4 moves: Basic, Debuffer, and 2 Special Skills

from abc import ABC, abstractmethod
from core.model.character import Character

# Element chart for weakness/resistance type for damage calculation (To be implemented)
element_chart = {
    "fire":     {"weak": ["water"], "resist": ["grass"]},
    "grass":    {"weak": ["fire"], "resist": ["ground"]},
    "ground":    {"weak": ["grass"], "resist": ["electric"]},
    "electric": {"weak": ["ground"], "resist": ["water"]},
    "water":   {"weak": ["electric"], "resist": ["fire"]}
}



# Fire Element Character
# First subclass that inherits from Character main class
# Uses Fire type attacks. Debuffs Enemy Attack
# Strong against Grass-types, weak against Water-types
class FireElement(Character):

    # Inherits Basic Attack from Character main class
    
    # Basic Attack [Fireball]: Basic attack
    
    # Status Attack(Debuffer) [Raise Temperature]: Reduce Enemy Attack (Will implement duration in the future)
    def status_attack(self, enemy):
        # Checks if player has enough mana
        status_attack_cost = 10
        if (self.get_mp() < status_attack_cost):
            print("\nInsufficient mana!")
            return False
        
        self.modify_mp(-(status_attack_cost))
        enemy.modify_attack(2)
        print(f"\n{self.get_character_name()} scared {enemy.get_character_name()}, reducing its attack!")
        return True
        
    # Special Attack One [Flameburst]: Deals moderate damage, may inflict burn on target     
    def special_attack_one(self, enemy):
        special_attack_one_cost = 25
        if (self.get_mp() < special_attack_one_cost):
            print("\nInsufficient mana!")
            return False
        
        self.modify_mp(-(special_attack_one_cost))
        enemy.modify_hp(self.calculate_dmg(self.get_attack(), enemy.get_defense(), 1.5))  
        print(f"\n{self.get_character_name()} burns {enemy.get_character_name()}, dealing {self.calculate_dmg(self.get_attack(), enemy.get_defense(), 1.5)} damage")
        return True
        
    # Special Attack Two [Big Fireball]    
    def special_attack_two(self, enemy):
        special_attack_two_cost = 50
        if (self.get_mp() < special_attack_two_cost):
            print("\nInsufficient mana!")
            return False
        
        self.modify_mp(-(special_attack_two_cost))
        enemy.modify_hp(self.calculate_dmg(self.get_attack(), enemy.get_defense(), 2.5))
        print(f"\n{self.get_character_name()} hurled a huge fireball at {enemy.get_character_name()}, dealing a massive {self.calculate_dmg(self.get_attack(), enemy.get_defense(), 2.5)} damage")   
        return True
    
    # Display skills
    def display_skills(self):
        print("\n1. [Fireball]: Throws fireball at the enemy, dealing low damage")
        print("2. [Raise Temperature]: Increase Temperature around the enemy, lowering its attack")
        print("3. [Flameburst]: Launches a barrage of flames at the enemy, dealing moderate damage, and has a chance to inflict burn")
        print("4. [Big Fireball]: Throws a comically large fireball at the enemy, dealing major damage")
        
    # This is where players makes their turns
    def next_Turn(self, enemy):
        print(f"\n===== It's {self.get_character_name()}'s Turn! =====")
        self.display_status()
        self.display_skills()
        while (True):
            choice = str(input("\nChoose your option: "))
            if (choice == "1"):
                self.basic_attack(enemy)
                break
            elif(choice == "2"):
                turn_success = self.status_attack(enemy) # should return True/False
                if (turn_success):
                    break
            elif(choice == "3"):
                turn_success = self.special_attack_one(enemy)
                if (turn_success):
                    break
            elif(choice == "4"):
                turn_success = self.special_attack_two(enemy)
                if (turn_success):
                    break
            else:
                print("\nInvalid input!")
        print(f"\n===== {self.get_character_name()}'s Turn Ended! =====")
        
