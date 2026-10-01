# 🔥💧 Level 1: Create Your First Bender

## Introduction to the Elemental Arena Battle Simulator

This challenge involves building an **Elemental Arena** battle simulator. You will start by creating the fundamental building block of the simulator: the `Bender` class.

A duel is a turn-based encounter between two benders. The outcome of the duel depends on the bender's stats, the moves they use, and their elemental affinity.

- **Stats:** Each bender has HP (Health Points), Attack, Defense, and Speed.
- **Element:** Each bender belongs to one of four elements: Water, Fire, Earth, or Air.
- **Moves:** Each bender has a set of four moves with varying power levels.
- **Battle Logic:** The speed of a bender determines who attacks first. The damage dealt by an attack is calculated based on the attacker's Attack stat, the move's power, and the defender's Defense stat.

> **Note:** elemental type does **not** affect damage yet in this level. A bender's Element is simply stored as an attribute for now. The type-advantage system (Water being strong against Fire, for example) is introduced in Level 2.

## Problem Statement

Design and implement a `Bender` class that represents a duel-ready fighter with all essential attributes and basic functionality. This will be the foundation upon which all future battle mechanics will be built.

## Requirements

- **Attributes:** Name, Element, HP (Health Points), Attack, Defense, Speed
- **Moveset:** Array of 4 moves with different power levels
- **Core Methods:** Attack another bender, take damage, check if fainted
- **Constructor:** Initialize a bender with custom stats

## Input Format

```
Bender creation:
- name: string
- element: string ("Water", "Fire", "Earth", or "Air")
- hp: integer (1-200)
- attack: integer (1-100)
- defense: integer (1-100)
- speed: integer (1-100)
- moves: array of 4 move names with power levels

Attack action:
- attacker: Bender object
- defender: Bender object
- move_index: integer (0-3)
```

## Output Format

```
Bender status display
Attack result messages
Fainted status check
```

## Damage Formula (Level 1: Basic Version)

No type advantage yet, that's introduced in Level 2.

```
damage = round((attacker_attack * move_power) / defender_defense)
```

## Example 1: Basic Bender Creation and Attack

**Input:**
```
# Create Kael
kael = Bender("Kael", "Fire", 100, 58, 38, 88,
             [("Ember Slash", 40), ("Quick Jab", 30), ("Focus", 0), ("Flame Surge", 70)])

# Create Mira
mira = Bender("Mira", "Water", 92, 50, 45, 60,
             [("Water Whip", 35), ("Tide Push", 25), ("Mist Veil", 0), ("Tidal Wave", 60)])

# Display initial stats
print(kael.display_stats())
print(mira.display_stats())

# Kael attacks Mira with Ember Slash
kael.attack(mira, 0)
print(mira.display_stats())

# Check if Mira fainted
print(f"Mira fainted: {mira.is_fainted()}")
```

**Expected Output:**
```
Kael (Fire) - HP: 100/100, Attack: 58, Defense: 38, Speed: 88
Moves: Ember Slash (40), Quick Jab (30), Focus (0), Flame Surge (70)

Mira (Water) - HP: 92/92, Attack: 50, Defense: 45, Speed: 60
Moves: Water Whip (35), Tide Push (25), Mist Veil (0), Tidal Wave (60)

Kael used Ember Slash!
Mira took 52 damage!

Mira (Water) - HP: 40/92, Attack: 50, Defense: 45, Speed: 60
Moves: Water Whip (35), Tide Push (25), Mist Veil (0), Tidal Wave (60)

Mira fainted: False
```

## Example 2: Bender Fainting

**Input:**
```
# Create weak Zephyr
zephyr = Bender("Zephyr", "Air", 28, 12, 50, 95,
               [("Gust", 0), ("Wind Slap", 18), ("Tumble", 12), ("Cyclone", 22)])

# Create strong Doran
doran = Bender("Doran", "Earth", 145, 80, 75, 40,
              [("Boulder Throw", 75), ("Rock Fist", 42), ("Tremor", 48), ("Mountain Crush", 85)])

print(zephyr.display_stats())
print(doran.display_stats())

# Doran attacks with Boulder Throw
doran.attack(zephyr, 0)
print(zephyr.display_stats())
print(f"Zephyr fainted: {zephyr.is_fainted()}")
```

**Expected Output:**
```
Zephyr (Air) - HP: 28/28, Attack: 12, Defense: 50, Speed: 95
Moves: Gust (0), Wind Slap (18), Tumble (12), Cyclone (22)

Doran (Earth) - HP: 145/145, Attack: 80, Defense: 75, Speed: 40
Moves: Boulder Throw (75), Rock Fist (42), Tremor (48), Mountain Crush (85)

Doran used Boulder Throw!
Zephyr took 120 damage!

Zephyr (Air) - HP: 0/28, Attack: 12, Defense: 50, Speed: 95
Moves: Gust (0), Wind Slap (18), Tumble (12), Cyclone (22)

Zephyr fainted: True
```
