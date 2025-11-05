# Character Class
# Will serve as the blueprint for subclasses

from abc import ABC, abstractmethod

# Character Superclass
class Character(ABC):
    # Constructor, self defines this class
    def __init__(self, name, level, element_type):
        self.__name = name
        self.__level = level
        self.__type = element_type.lower()

        self.__max_hp = 10*level
        self.__hp = self.__max_hp
        
        self.__max_mp = 5*level
        self.__mp = self.__max_mp
        
        # To be implemented
        self.shield = 0
        
        self.__base_attack = 2*level
        self.__attack = self.__base_attack
        
        self.__base_defense = level
        self.__defense = self.__base_defense
        
        self.status_effects = []
          
    # Returns character name
    def get_character_name(self):
        return self.__name
    
    # Returns character level
    def get_character_level(self):
        return self.__level   
    
    # Returns character type
    def get_character_type(self):
        return self.__type
    
    # Returns character max hp
    def get_max_hp(self):
        return self.__max_hp
    
    # Returns character hp
    def get_hp(self):
        return self.__hp 
    
    # Returns character max mp
    def get_max_mp(self):
        return self.__max_mp
    
    # Returns character mp
    def get_mp(self):
        return self.__mp
    
    # Returns character attack
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
    
    #### Stat modifiers

    # Resets hp stat (for rematch/level up/etc.)
    def reset_stats(self):
        self.__hp = self.__max_hp
        self.__mp = self.__max_mp
        self.__attack = self.__base_attack
        self.__defense = self.__base_defense
        self.status_effects = []

    # Modify hp stat (for taking damage/recovering health)
    def modify_hp(self, damage):
        self.__hp -= damage
        if (self.__hp <= 0):
            self.__hp = 0
            
        if (self.__hp >= self.__max_hp):
            self.__hp = self.__max_hp
            
    # Modify mp stat (for skill usage)
    def modify_mp(self, value):
        self.__mp += value
        
        # Prevents mp overload
        if (self.__mp > self.__max_mp):
            self.__mp = self.__max_mp
        elif (self.__mp < 0):
            self.__mp = 0
        
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
            
     # Add New Status to the character
    def add_status(self, effect):
        
        # Prevents DoT stacking
        for active_effect in self.status_effects:
             if (active_effect.get_name()==effect.get_name() and effect.get_effect_type() == "DOT"):
                 active_effect.set_duration(effect.get_duration())
                 print(f"\n{self.get_character_name()} is now affected by {effect.get_name()} for {effect.get_duration()} turns!")
                 return
        
        # Note: you are adding an object as a parameter here (see class StatusEffect)
        self.status_effects.append(effect)
        print(f"\n{self.get_character_name()} is now affected by {effect.get_name()} for {effect.get_duration()} turns!")
        
    # Apply status effects and update status duration or remove status if duration <= 0    
    def update_status_effects(self):
        # list used for looping expired status
        expired = []
        for effect in self.status_effects:           
            #"BUFF", "DEBUFF", "DOT"
            if (effect.get_effect_type() == "BUFF"):
                effect.apply(self)
            elif (effect.get_effect_type() == "DEBUFF"):
                effect.apply(self)
            elif (effect.get_effect_type() == "DOT"):
                print(f"\n{self.get_character_name()} gets hurt from {effect.get_name()}, receiving {effect.dots_value} damage!")
                effect.apply_dot(self)
                
            if (effect.get_duration() == 0):
                expired.append(effect)    
            
        # Removes status that are added in expired list        
        for e in expired:
            # prevents dot status effects from reverting
            if (e.get_effect_type() == "BUFF" or e.get_effect_type() == "DEBUFF"):
                e.revert_status(self)
            self.status_effects.remove(e)
            print(f"{self.get_character_name()} is no longer affected by {e.get_name()}.")
        
    # Display character status
    def display_status(self):
        print(f"\nName: {self.get_character_name()}")
        print(f"HP: {self.get_hp()}/{self.get_max_hp()}")
        print(f"MP: {self.get_mp()}/{self.get_max_mp()}")
        
        print(f"Attack: {self.get_attack()}")
        print(f"Defense: {self.get_defense()}")
        print(f"Level: {self.get_level()}")
        print(f"Type: {self.get_type()}")
        
        # Display active status
        if self.status_effects: 
            print("Active effects:", ", ".join(f"{e.get_name()} ({e.get_duration()})" for e in self.status_effects)) 
        else: 
            print("No active effects.")    
        
    # Damage calculation: To be used before modifying HP
    # Calculation is (Base Attack * Multiplier) - Enemy Defense
    def calculate_dmg(self, base_attack, enemy_defense, multiplier):
        # if no multiplier (for basic attack)
        if (multiplier == 0):
            return base_attack - enemy_defense
        # return with multiplier
        return (base_attack * multiplier) - enemy_defense
         
    #### Character's Skillsets (Abstraction)        
    # Basic Attack: Low dmg, gains mp
    @abstractmethod
    def basic_attack(self, enemy):
        pass   
        
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
    
    # Defines how players make a turn
    @abstractmethod
    def next_Turn(self, enemy):
        pass
    
# Classes that inflicts status effects. To see how different status affects players, see status_effects.py 
class StatusEffect:
    def __init__(self, name, duration, effect_type ,effect_function, value_change):
        self.__name = name
        self.__duration = duration
        
        # It has 3 effect types: "BUFF", "DEBUFF", "DOT" 
        self.__effect_type = effect_type
        self.effect_function = effect_function
        
        # For Buff/Debuff calculation (based on player stat)
        self.stats_value = value_change * 0.2
        
        # For DoT damage calculation (based on enemy attack)
        self.dots_value = value_change * 0.5
        
        # For determining whether the effect has been applied
        self.is_applied = False
    
    def get_name(self): 
        return self.__name
    
    def get_duration(self):
        return self.__duration
    
    def get_effect_type(self):
        return self.__effect_type
    
    # If player inflicts the same DoT, only refreshes its duration
    def set_duration(self, duration):
        self.__duration = duration
        
    # Apply Buff/Debuff
    def apply(self, target):
        if (not self.is_applied):
            self.effect_function(target, self.stats_value)
            self.is_applied = True
        self.__duration -= 1
        
    def revert_status(self, target):
        self.effect_function(target, -self.stats_value)    
        
    # Apply DoTs
    def apply_dot(self, target):
        self.effect_function(target, self.dots_value)
        self.__duration -= 1
        
