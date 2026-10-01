# ⚔️ Level 2: Duel System & Elemental Advantage

## Problem Statement

Implement the core duel mechanics that make fights strategic and exciting. Create a damage calculation system with turn-based combat, critical hits, proper turn order determination, and, new to this level, elemental type advantages.

## Requirements

- **Turn order** determined by Speed stats (faster bender goes first)
- **Elemental Advantage:** each bender's Element makes their attacks stronger or weaker against certain opposing Elements (see below)
- **Enhanced damage calculation:** base damage, modified by elemental advantage and critical hits
- **Critical hits** occur randomly (10% chance for 2x damage)
- **Complete turn-based duel loop** until one bender faints
- **Duel class** to manage the entire combat system

## Input Format

```
Duel initialization:
- bender1: Bender object
- bender2: Bender object

Turn execution:
- current_bender: Bender object
- target_bender: Bender object
- move_choice: integer (0-3) or "auto" for random selection
```

## Output Format

```
Duel start announcement
Turn-by-turn combat log
Elemental advantage notifications
Critical hit notifications
HP updates after each attack
Duel end result with winner
```

## 🌊 The Elemental Wheel

Each bender's Element is one of four: **Water**, **Fire**, **Air**, **Earth**. They form a single cycle:

```
Water beats Fire    (extinguishes it)
Fire beats Air      (burns through it)
Air beats Earth     (erodes it)
Earth beats Water   (absorbs it)
```

When a bender attacks, their **fixed Element** (not the move used) determines the type multiplier against the defender's Element:

| Matchup | Multiplier | Label |
|---|---|---|
| Attacker's Element beats defender's Element | **2.0x** | Super Effective |
| Attacker's Element is beaten by defender's Element | **0.5x** | Weak |
| Anything else, including same element | **1.0x** | Neutral |

**Example:** a Water bender's attacks are always Super Effective against a Fire bender, and always Weak against an Earth bender.

## Enhanced Damage Calculation

```
base_damage = (attacker_attack * move_power) / defender_defense
type_multiplier = 2.0 if attacker's Element beats defender's Element
                   0.5 if attacker's Element is beaten by defender's Element
                   1.0 otherwise
critical_multiplier = 2.0 if critical_hit else 1.0
final_damage = base_damage * type_multiplier * critical_multiplier
final_damage = max(1, round(final_damage))  // Minimum 1 damage, round only once at the end
```

## Turn Order Logic

```
if bender1.speed > bender2.speed:
    first = bender1, second = bender2
elif bender2.speed > bender1.speed:
    first = bender2, second = bender1
else:
    # Speed tie - random selection
    first, second = random.choice([(bender1, bender2), (bender2, bender1)])
```

## Critical Hit Calculation

```
critical_chance = 0.10  // 10% chance
is_critical = random.random() < critical_chance
```

## Example 1: Elemental Advantage Decides the Duel

**Input:**
```
# Create Benders
kael = Bender("Kael", "Fire", 100, 58, 38, 88,
             [("Ember Slash", 40), ("Quick Jab", 30), ("Focus", 0), ("Flame Surge", 70)])

mira = Bender("Mira", "Water", 92, 50, 45, 60,
             [("Water Whip", 35), ("Tide Push", 25), ("Mist Veil", 0), ("Tidal Wave", 60)])

# Start duel
duel = Duel(kael, mira)
duel.start_duel()

# Turn 1: Kael uses Ember Slash (move 0)
# Turn 2: Mira uses Water Whip (move 0), Critical Hit!
```

**Expected Output:**
```
=== DUEL BEGINS! ===
Kael (Fire, HP: 100/100) VS Mira (Water, HP: 92/92)

Turn 1: Kael goes first! (Speed: 88 vs 60)
Kael used Ember Slash!
Not very effective... (Fire is weak against Water)
Mira took 26 damage!
Mira HP: 66/92

Turn 2: Mira strikes back!
Mira used Water Whip!
Super Effective! (Water is strong against Fire)
Critical Hit!
Kael took 184 damage!
Kael HP: 0/100

Kael fainted!
🏆 Mira wins the duel!

Duel Summary:
- Winner: Mira
- Turns: 2
- Critical Hits: 1
- Super Effective Hits: 1
```

## Example 2: Close Battle with Neutral Matchup and Speed Tie

**Input:**
```
# Create Benders with a neutral matchup (Water vs Air) and tied speed
nadia = Bender("Nadia", "Water", 85, 48, 60, 72,
              [("Wave Crash", 35), ("Splash Kick", 25), ("Guard", 0), ("Riptide", 50)])

talon = Bender("Talon", "Air", 90, 52, 55, 72,
              [("Gale Strike", 38), ("Wind Cutter", 28), ("Updraft", 0), ("Cyclone Blast", 48)])

duel = Duel(nadia, talon)
duel.start_duel()
```

**Expected Output:**
```
=== DUEL BEGINS! ===
Nadia (Water, HP: 85/85) VS Talon (Air, HP: 90/90)

Turn 1: Speed tie! Nadia goes first! (Speed: 72 vs 72)
Nadia used Wave Crash!
Talon took 31 damage!
Talon HP: 59/90

Turn 2: Talon strikes back!
Talon used Gale Strike!
Nadia took 33 damage!
Nadia HP: 52/85

Turn 3: Nadia goes first!
Nadia used Riptide!
Talon took 44 damage!
Talon HP: 15/90

Turn 4: Talon strikes back!
Talon used Cyclone Blast!
Nadia took 42 damage!
Nadia HP: 10/85

Turn 5: Nadia goes first!
Nadia used Wave Crash!
Talon took 31 damage!
Talon HP: 0/90

Talon fainted!
🏆 Nadia wins the duel!

Duel Summary:
- Winner: Nadia
- Turns: 5
- Critical Hits: 0
- Super Effective Hits: 0
```
