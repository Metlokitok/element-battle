# Ideas
Notes for ideas, fixes, features, etc.

## Features
- To be implemented:
   - Game menu
   - User input handling
   - Player vs Player
   - Player vs CPU
   - More Character types
   - Buff/Debuff durations, Magic Points (mp) system, Damage over time (DOT) system
   - Endless Mode
   - Level System for Endless Mode
   - Charge system
   - Damage calculation (for weakness, resistance)

## Self Notes
- Quick Note
    - Buff/Debuff/Dot/Hots to add:
        - Burn (done)
        - Poison
        - Bleed
        - Stun
        - Heal
        - Lifesteal
        - Shield
    - The status effects happens on the player that was applied to, not applies status effects on another player
    - There needs to be a small documentation for how damage works, debuff types, element types, etc
        - Probably in the future updates

## Element Types and their playstyle (Draft)
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