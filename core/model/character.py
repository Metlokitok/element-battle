# Character Class
# Will serve as the blueprint for subclasses

from abc import ABC, abstractmethod

class Character(ABC):
    # Constructor, self defines this class
    def __init__(self, name, level, element_type):
        self.__name = name
        self.__level = level
        self.__type = element_type.lower()
        self.__hp = 10*level
        self.__attack = 1*level
        self.__defense = 1+level
    
    # Returns character name
    def get_character_name(self):
        return self.__name
    
    # Returns character level
    def get_character_level(self):
        return self.__level   
    
    # Returns character type
    def get_character_type(self):
        return self.__type
    
    # Returns character attack
    def get_hp(self):
        return self.__hp 
    
    # Returns character hp
    def get_attack(self):
        return self.__attack
    
    # Returns character defense
    def get_defense(self):
        return self.__defense
    
    # Returns character level
    def get_level(self):
        return self.__level
    
    # Returns character type
    def get_type(self):
        return self.__type

    # Modify hp stat (for taking damage)
    def modify_hp(self, damage):
        self.__hp -= damage
        if (self.__hp <= 0):
            self.__hp = 0

    # Modify attack stat (for debuff)
    def modify_attack(self, attack_debuff):
        self.__attack -= attack_debuff
        if (self.__attack <= 0):
            print("Attack cannot go any lower!")
            self.__attack = 0
        
    # Modify defense stat (for debuff)
    def modify_defense(self, defense_debuff):
        self.__defense -= defense_debuff
        if (self.__defense <= 0):
            print("Defense cannot go any lower!")
            self.__defense = 0
        
    # Display character status
    def display_status(self):
        print(f"\nName: {self.get_character_name()}")
        print(f"HP: {self.get_hp()}")
        print(f"Level: {self.get_level()}")
        print(f"Type: {self.get_type()}")    
        
    # Character's Skillsets (Abstraction)    
        
    # Basic Attack: Low dmg, cost 0 mp
    def basic_attack(self, enemy):
        enemy.modify_hp((self.get_attack()))
        print(f"{self.get_character_name()} attacks {enemy.get_character_name()} for {self.get_attack()} damage")   
        
    # Buff/Debuff Attack: Inflict Status effects (atk reduction(fire), def reduction(grass), atk increase(water/electric), def increase(ground))
    @abstractmethod
    def status_attack(self, enemy):
        pass
    
    # Special Attack 1: Moderate dmg, inflicts Damage over time (to be implemented)
    @abstractmethod
    def special_attack_one(self, enemy):
        pass
        
    # Special Attack 2: High dmg, high mp cost
    @abstractmethod
    def special_attack_two(self, enemy):
        pass    
        
    # Display character skills
    @abstractmethod
    def display_skills(self):
        pass # to be implemented by the subclass    
    
    @abstractmethod
    def next_Turn(self, enemy):
        pass
    
    