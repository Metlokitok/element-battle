# Journal:
Personal Journal, so you can see my descent to madness

## 10-13-2025
- Coded the Main class for the character objects in the game, and implemented its first character type (fire)
- Player vs Computer basics showcased
    - To be implemented:
        - Game menu
        - User input handling
        - Player vs Player
        - Player vs CPU
        - More Character types
        - Buff/Debuff durations, Magic Points (mp) system, Damage over time (DOT) system
        - Endless Mode
        - Level System for Endless Mode

## 10-20-2025
- Forgor this project exists
    - Created a separate journal file for documentation
    - Encapsulated the player stats(attack, hp, etc.)
    - Created a working Player vs Player game mode
        - Currently limited to fire types, other types to be implemented
        - No other game modes yet, will implement on later releases

## 10-21-2025
- Features:
    - Allows players in pvp to restart or go back to menu
    - Added max and base stats (HP, MP, Attack, Defense). Used for resetting, rematches, level up(to be implemented), etc.
    - Added a proper damage calculation system. weakness/resistance to be implemented!
- Bug fixes:
    - Fixed issue where you are prompted to make an option instead of exiting the game
    - Fixed rematch issues
    - Fixed error during player turn wherein it crashes when making invalid inputs

## 10-22-2025
- Features:
    - Mana system added. Players will now have to be mindful of their mana usage
- Changes
    - Terminal outputs. Added proper spacing and some fancy terminal prints
- Bug fixes:
    - Fixed issue where players are prompted to attack more than once whenever they chose skills that has insufficient mana cost

## 10-27-2025
- Took a break, forgor this exist
- Features:
    - Buff, debuff, and damage over time (DoT) planned
- Issues:
    - Debuff not properly called yet
    - Debuff not being applied
    - Updated code to be pushed once new features is ready to be implemented

## 11-01-2025
- I keep forgetting
- Fixes (Somewhat)
    - DoTs are properly being implemented, however they are part of another feature (chanced based) which is to be implemented as well
- Issues: 
    - The status debuff is still not being applied properly. Issues include:
        - debuffs of the same type keeps stacking (Might be implemented in the future)
        - changes on player stats not going back to original stat even after the debuff duration ended
    - Again, updated code to be pushed once new features are ready to be implemented

## 11-02-2025
- Finally
- Features: 
    - Buffs, Debuffs, Damage-over-time (DoTs) now implemented!
- Bug Fixes:
    - Fixed issue where player stats does not go back to its original value
- (New) Coming up next:
    - Chanced based DoT
    - Code and Documentation cleanup
    - README update

## 11-03-2025
- Features:
    - Fire type small update: every attack has chance of inflicting "Burn" DoT 
- Fixes:
    - Fixed some code typography
    - Fixed issue where DoT status effects returns hp after its duration
    - Fixed issue where game doesn't end when the DoT reduce hp to 0
    - Fixed issue where game restarts when entering invalid inputs
- Coming up next:
    - More code cleanup
    - Damage scaling adjustments
    - README
    - New element types