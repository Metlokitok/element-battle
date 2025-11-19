# Game Documentation
- Documentation about how the game works

## Gameplay
- Standard turned based game loop. Players take turns in choosing their moves.
- Has four standard moveset: 
    - Basic Attack
    - Buff/Debuff attack
    - Special Skill one
    - Special Skill two (Ultimate)

## Terminologies
- Hp: Health Points. Game ends when a player character's Hp reaches zero
- Mp: Mana points. Consumed by player skills. Cannot cast a skill if Mp is insufficient
- Atk: Attack points. Determines the amount of damage a player can deal to enemy's Hp. Can be modified via buff/debuff
    - The calculation for the total damage to deal is: 
        - (Base Attack * Multiplier) - Enemy Defense
- Def: Defense points. Reduces the amount of damage received by the player. Can be modified via buff/debuff
- Buff: A status effect that can increase a player's stat. Has a set duration
- Debuff: A status effect that can decrease a player's stat. Has a set duration, and can stack
- DoT: Damage over Time. status effects that deals damage to a player per turn. Has a set duration, and cannot stack

## Element Types
- Fire
    - Strong against grass, weak against water
    - Can reduce enemy attack
    - Every attack has chance of inflicting "Burn" DoT
    - Ultimate deals great damage when target is under burn effect

- Grass
    - Strong against ground, weak against fire
    - Can recover hp each turn
    - Can inflict "Poison" on enemy. Recovers hp when attacking enemy affected by poison
    - Ultimate deals damage and recovers hp

- Ground
    - Strong against electric, weak against Grass
    - Can increase defense that is stackable
    - Can inflict "Bleed" on enemy
    - Ultimate deals great damage depending on the amount of defense stack

- Electric
    - Strong against water, weak against ground
    - Can increase attack
    - Can inflict "Stun" on enemy
    - Ultimate deals great damage. Adds extra damage based on its stacked attack buff and whether the enemy is inflicted with stun effect

- Water
    - Strong against fire, weak against lightning
    - Can gain a shield, and recover hp when shield is active
    - Can reduce enemy attack and defense, and increase its own attack and defense at the same time
    - Ultimate deals damage, deals great damage when enemy is debuffed

## Damage Calculations
### Dealing/Receiving Damage
- The formula for calculating total damage is (Base Attack * Multiplier) - Enemy Defense. The function used for this is calculate_dmg().  
- The total damage will then be passed on to modify_hp() function