# collection of every buffs, debuffs, DoTs etc.

# Burns
def burn(target, value_change):
    target.modify_hp(value_change)
    
# Poisons
def poison(target, value_change):
    target.modify_hp(value_change)    
    
# Reduce attack
def attack_reduction(target, value_change):
    target.modify_attack(value_change)