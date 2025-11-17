# Element subclasses
# Single file containing multiple subclasses (Element Types). Will split into multiple files if it gets large
# Each subclass will have 4 moves: Basic, Debuffer, and 2 Special Skills

import random
import math
from abc import ABC, abstractmethod
from core.model.character import Character
from core.model.character import StatusEffect
from core.model import status_effects as status_effect

# Element chart for weakness/resistance type for damage calculation (To be implemented)
element_chart = {
    "fire":     {"weak": ["water"], "resist": ["grass"]},
    "grass":    {"weak": ["fire"], "resist": ["ground"]},
    "ground":    {"weak": ["grass"], "resist": ["electric"]},
    "electric": {"weak": ["ground"], "resist": ["water"]},
    "water":   {"weak": ["electric"], "resist": ["fire"]}
}

# Fire Element Character
class FireElement(Character):
    # Basic Attack [Fireball]: Basic attack
    # New effect: has a small chance of inflicting Burn DoT on opponent (10%)
    def basic_attack(self, enemy):
        # Gives a random number between 1-100
        multiplier = 0
        chance = math.floor(random.random()*100)+1
        total_damage = self.calculate_dmg(self.get_attack(), enemy.get_defense(),multiplier)
        
        # restores mp
        self.modify_mp(10)
        
        enemy.modify_hp(total_damage)
        print(f"\n{self.get_character_name()} attacks {enemy.get_character_name()} for {total_damage} damage")
        
        if (chance <= 10):
            enemy.add_status(StatusEffect("Burn", 1, "DOT",status_effect.burn, self.get_attack()))
         
    
    # Status Attack(Debuffer) [Raise Temperature]: Reduce Enemy Attack (Will implement duration in the future)
    # New effect: has a very small chance of inflicting Burn DoT on opponent (2%)
    def status_attack(self, enemy):
        chance = math.floor(random.random()*100)+1
        
        # Checks if player has enough mana
        status_attack_cost = 10
        if (self.get_mp() < status_attack_cost):
            print("\nInsufficient mana!")
            return False
        
        self.modify_mp(-(status_attack_cost))
        print(f"\n{self.get_character_name()} scared {enemy.get_character_name()}, reducing its attack!")
        enemy.add_status(StatusEffect("Attack Down", 3, "DEBUFF",status_effect.attack_reduction, self.get_attack()))
        
        if (chance <= 2):
            enemy.add_status(StatusEffect("Burn", 1, "DOT",status_effect.burn, self.get_attack()))
        
        return True
        
    # Special Attack One [Flameburst]: Deals moderate damage, inflict burn on target     
    def special_attack_one(self, enemy):
        multiplier = 1.5
        special_attack_one_cost = 25
        total_damage = self.calculate_dmg(self.get_attack(), enemy.get_defense(),multiplier)
        if (self.get_mp() < special_attack_one_cost):
            print("\nInsufficient mana!")
            return False
        
        self.modify_mp(-(special_attack_one_cost))
        enemy.modify_hp(total_damage)  
        print(f"\n{self.get_character_name()} burns {enemy.get_character_name()}, dealing {total_damage} damage")
        
        enemy.add_status(StatusEffect("Burn", 3, "DOT", status_effect.burn, self.get_attack()))
        
        return True
        
    # Special Attack Two [Big Fireball]  : Deals great damage. Damage doubles when target is burning  
    def special_attack_two(self, enemy):
        multiplier = 2.5
        special_attack_two_cost = 50
        total_damage = self.calculate_dmg(self.get_attack(), enemy.get_defense(),multiplier)
        if (self.get_mp() < special_attack_two_cost):
            print("\nInsufficient mana!")
            return False
        
        # Increase Multiplier when enemy is burning
        if (any(effect.get_name()=="Burn" for effect in enemy.status_effects)):
            multiplier = 3
            self.modify_mp(-(special_attack_two_cost))
            total_damage = self.calculate_dmg(self.get_attack(), enemy.get_defense(),multiplier)
            enemy.modify_hp(total_damage)
            print(f"\n{self.get_character_name()} hurled a huge fireball at {enemy.get_character_name()}, dealing a massive {total_damage} damage")   
            return True
        
        self.modify_mp(-(special_attack_two_cost))
        enemy.modify_hp(total_damage)
        print(f"\n{self.get_character_name()} hurled a huge fireball at {enemy.get_character_name()}, dealing a massive {total_damage} damage")
        
        # If enemy not burning, add burning status after
        enemy.add_status(StatusEffect("Burn", 3, "DOT", status_effect.burn, self.get_attack()))
        return True
    
    # Display skills
    def display_skills(self):
        print("\n1. [Fireball]: Throws fireball at the enemy, dealing low damage with a low chance of inflicting Burn")
        print("2. [Raise Temperature]: Increase Temperature around the enemy, lowering its attack, with a very low chance of inflicting Burn")
        print("3. [Flameburst]: Launches a barrage of flames at the enemy, dealing moderate damage, and has a chance to inflict Burn")
        print("4. [Big Fireball]: Throws a comically large fireball at the enemy, dealing major damage and inflicts Burn on the enemy")
        
    # This is where players makes their turns
    def next_Turn(self, enemy):
        print(f"\n===== It's {self.get_character_name()}'s Turn! =====")
        self.update_status_effects()
        
        # Ends match if Hp reaches 0
        if (self.get_hp()<=0):
            return
        
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

# Grass Element Character        
class GrassElement(Character):
    
    # Basic Attack [Razor Strike]: Basic attack
    # New effect: Recover hp if opponent is affected by Poison DoT
    def basic_attack(self, enemy):
        multiplier = 0
        total_damage = self.calculate_dmg(self.get_attack(), enemy.get_defense(),multiplier)
        restored_hp = total_damage # 
        # Restores mp
        self.modify_mp(10)
        
        # If enemy is poisoned, recover hp
        if (any(effect.get_name()=="Poison" for effect in enemy.status_effects)):
            enemy.modify_hp(total_damage)
            
            self.modify_hp(-restored_hp) # Must be negative so that it heals in modify_hp()
            
            print(f"\n{self.get_character_name()} attacks {enemy.get_character_name()} for {total_damage} damage")
            print(f"\n{self.get_character_name()} also recovers {restored_hp} hp!")
            return
        
        enemy.modify_hp(self.calculate_dmg(self.get_attack(), enemy.get_defense(),multiplier))
        print(f"\n{self.get_character_name()} attacks {enemy.get_character_name()} for {self.calculate_dmg(self.get_attack(), enemy.get_defense(),multiplier)} damage")
    
    # Status Attack (Self Heal) [Regrow]: Heals itself
    def status_attack(self, enemy):
        restored_hp = self.get_attack()
        
        # Checks if player has enough mana
        status_attack_cost = 10
        if (self.get_mp() < status_attack_cost):
            print("\nInsufficient mana!")
            return False
        
        self.modify_mp(-(status_attack_cost))
        print(f"\n{self.get_character_name()} recovers lost limbs, recovering hp!")
        self.modify_hp(-(restored_hp))
        
        return True
    
    # Special Attack One (Poison Vine): Deals moderate damage, inflict poison on target
    def special_attack_one(self, enemy):
        multiplier = 1.5
        special_attack_one_cost = 25
        total_damage = self.calculate_dmg(self.get_attack(), enemy.get_defense(),multiplier)
        restored_hp = total_damage
        
        if (self.get_mp() < special_attack_one_cost):
            print("\nInsufficient mana!")
            return False
        
        # If enemy is poisoned, heal
        if (any(effect.get_name() == "Poison" for effect in enemy.status_effects)):
            self.modify_mp(-(special_attack_one_cost))
            
            enemy.modify_hp(total_damage)
            self.modify_hp(-restored_hp)  
            
            print(f"\n{self.get_character_name()} poisons {enemy.get_character_name()}, dealing {total_damage} damage")
            print(f"\n{self.get_character_name()} also recovers {restored_hp} hp!")
            
            enemy.add_status(StatusEffect("Poison", 3, "DOT", status_effect.poison, self.get_attack()))
            
            return True
            
        
        self.modify_mp(-(special_attack_one_cost))
        enemy.modify_hp(total_damage)  
        print(f"\n{self.get_character_name()} poisons {enemy.get_character_name()}, dealing {total_damage} damage")
        
        enemy.add_status(StatusEffect("Poison", 3, "DOT", status_effect.poison, self.get_attack()))
        
        return True
    
    # Special Attack Two (Seed Bomb): Deals great damage and inflicts Poison. Recovers moderate amount of hp 
    def special_attack_two(self, enemy):
        multiplier = 2.5
        special_attack_two_cost = 50
        total_damage = self.calculate_dmg(self.get_attack(), enemy.get_defense(),multiplier)
        restored_hp = total_damage
        
        if (self.get_mp() < special_attack_two_cost):
            print("\nInsufficient mana!")
            return False
        
        self.modify_mp(-(special_attack_two_cost))
        enemy.modify_hp(total_damage)
        self.modify_hp(-restored_hp)
        print(f"\n{self.get_character_name()} threw a cluster of exploding seeds at {enemy.get_character_name()}, dealing {total_damage} damage and recovering {restored_hp/2} hp!")
    
        enemy.add_status(StatusEffect("Poison", 3, "DOT", status_effect.poison, self.get_attack()))
    
        return True
    
    def display_skills(self):
        print("\n1. [Razor Strike]: Strikes the enemy with razor vines, dealing low damage. Recovers hp if enemy is poisoned")
        print("2. [Regrow]: Regrows lost limbs, broken bones, and other damages. Recovers hp")
        print("3. [Poison Vine]: Strikes the enemy with poisoned vines, dealing moderate damage, and inflicts Burn")
        print("4. [Big Fireball]: Throws a barrage of exploding seeds at the enemy, dealing great damage, inflicts poison, and recovers hp")
    
    def next_Turn(self, enemy):
        print(f"\n===== It's {self.get_character_name()}'s Turn! =====")
        self.update_status_effects()
        
        # Ends match if Hp reaches 0
        if (self.get_hp()<=0):
            return
        
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
    
# Ground Element Character        
class GroundElement(Character):
    def basic_attack(self, enemy):
        pass
    
    def status_attack(self, enemy):
        pass
    
    def special_attack_one(self, enemy):
        pass
    
    def special_attack_two(self, enemy):
        pass
    
    def display_skills(self):
        pass
    
    def next_Turn(self, enemy):
        pass
    
# Electric Element Character        
class ElectricElement(Character):
    def basic_attack(self, enemy):
        pass
    
    def status_attack(self, enemy):
        pass
    
    def special_attack_one(self, enemy):
        pass
    
    def special_attack_two(self, enemy):
        pass
    
    def display_skills(self):
        pass
    
    def next_Turn(self, enemy):
        pass
    
# Water Element Character        
class WaterElement(Character):
    def basic_attack(self, enemy):
        pass
    
    def status_attack(self, enemy):
        pass
    
    def special_attack_one(self, enemy):
        pass
    
    def special_attack_two(self, enemy):
        pass
    
    def display_skills(self):
        pass
    
    def next_Turn(self, enemy):
        pass
    
# used for constructing player characters at game.py    
element_constructor = {
    "fire": FireElement,
    "grass": GrassElement,
    "ground": GroundElement,
    "electric": ElectricElement,
    "water": WaterElement
}