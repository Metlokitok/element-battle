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
        enemy.modify_attack(2)
        print(f"{self.get_character_name()} scared {enemy.get_character_name()}, reducing its attack!")
        
    # Special Attack One [Flameburst]: Deals moderate damage, may inflict burn on target     
    def special_attack_one(self, enemy):
        enemy.modify_hp((self.get_attack()*1.5))  
        print(f"{self.get_character_name()} burns {enemy.get_character_name()}, dealing {(self.get_attack()*1.5)} damage")
        
    # Special Attack Two [Big Fireball]    
    def special_attack_two(self, enemy):
        enemy.modify_hp((self.get_attack()*2.5))
        print(f"\n{self.get_character_name()} hurled a huge fireball at {enemy.get_character_name()}, dealing a massive {(self.get_attack()*2.5)} damage")   
    
    def display_skills(self):
        print("\n1. [Fireball]: Throws fireball at the enemy, dealing low damage")
        print("2. [Raise Temperature]: Increase Temperature around the enemy, lowering its attack")
        print("3. [Flameburst]: Launches a barrage of flames at the enemy, dealing moderate damage, and has a chance to inflict burn")
        print("4. [Big Fireball]: Throws a comically large fireball at the enemy, dealing major damage")
        
    def next_Turn(self, enemy):
        self.display_skills()
        choice = int(input("Choose your option: "))
        if (choice == 1):
            self.basic_attack(enemy)
        elif(choice == 2):
            self.status_attack(enemy)
        elif(choice == 3):
            self.special_attack_one(enemy)
        elif(choice == 4):
            self.special_attack_two(enemy)
