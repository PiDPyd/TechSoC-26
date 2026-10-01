# 🏆 Level 3: Advanced Arena Features

## Problem Statement

Create an intelligent duel system with computer-controlled opponents, status effects, battle statistics tracking, and tournament mode for multiple benders.

## Requirements

- **Smart Computer Player:** AI chooses moves based on elemental advantage, effectiveness, and remaining HP
- **Status Effects:** Burn, Frozen, or Buried, each affecting multiple turns
- **Battle Statistics:** Track wins, losses, and battle history
- **Tournament Mode:** Multiple benders face off in elimination rounds
- **Advanced Duel Mechanics:** Status effect interactions and strategic AI

## Input Format

```
Tournament setup:
- participants: list of Bender objects (must be power of 2: 4, 8, 16, etc.)
- tournament_name: string

AI Duel:
- player_bender: Bender object
- computer_bender: Bender object
- difficulty: string ("easy", "medium", "hard")

Status effects:
- effect_type: string ("burn", "frozen", "buried")
- duration: integer (turns remaining)
```

## Output Format

```
Tournament bracket display
Round-by-round results
AI decision explanations
Status effect notifications
Comprehensive battle statistics
Tournament winner announcement
```

## 🤖 AI Decision Logic

```
def choose_move(self, opponent):
    if self.hp < 30% and has_healing_move():
        return healing_move
    elif opponent.hp > 70% and has_status_move():
        return status_move
    elif opponent.hp < 25%:
        return strongest_move
    else:
        return most_effective_move   # accounts for elemental advantage against opponent's Element
```

## 🔥❄️ Status Effects System

| Effect | Mechanic |
|---|---|
| **Burn** | Deals 10% max HP damage each turn for 4 turns |
| **Frozen** | 50% chance to skip turn for 3 turns |
| **Buried** | Cannot move for 2-4 turns (random duration) |

## 🥇 Tournament Structure

- Must have 2^n participants (4, 8, 16, etc.)
- Single elimination bracket
- Winners advance, losers are eliminated
- HP carries over between rounds (no full heal between matches)
- Final champion crowned
- Complete statistics tracking

## Example 1: AI Duel with a Status Effect

**Input:**
```
# Create Benders
sable = Bender("Sable", "Air", 95, 60, 58, 85,
              [("Arctic Gust", 0, "frozen"), ("Wind Blade", 52), ("Tailwind", 0), ("Cyclone Fang", 58)])

boran = Bender("Boran", "Earth", 110, 68, 62, 50,
              [("Rockslide", 55), ("Quicksand Trap", 0, "buried"), ("Stone Wall", 0), ("Seismic Slam", 70)])

# Start AI duel (computer controls Boran)
ai_duel = AIDuel(sable, boran, difficulty="hard")
ai_duel.start_duel()
```

**Expected Output:**
```
=== AI DUEL BEGINS! ===
Sable (Air, HP: 95/95) VS Boran (Earth, HP: 110/110) [COMPUTER]

Turn 1: Sable goes first! (Speed: 85 vs 50)
Sable used Wind Blade!
Super Effective! (Air is strong against Earth)
Boran took 101 damage!
Boran HP: 9/110

Turn 2: Boran strikes!
🤖 AI Analysis: HP critical, inflicting a status effect before going down
Boran used Quicksand Trap!
Sable is now buried! (3 turns remaining)

Turn 3: Sable is buried and cannot move!
Buried duration: 2 turns remaining

Turn 4: Boran strikes!
🤖 AI Analysis: Enemy immobilized, strike now!
Boran used Seismic Slam!
Not very effective... (Earth is weak against Air)
Sable took 41 damage!
Sable HP: 54/95

Turn 5: Sable is buried and cannot move!
Buried duration: 1 turn remaining

Turn 6: Boran strikes!
🤖 AI Analysis: Finish while immobilized
Boran used Rockslide!
Not very effective... (Earth is weak against Air)
Sable took 32 damage!
Sable HP: 22/95

Turn 7: Sable breaks free from being buried!
Sable used Cyclone Fang!
Super Effective! (Air is strong against Earth)
Boran took 112 damage!
Boran HP: 0/110

Boran fainted!
🏆 Sable wins the duel!

Duel Summary:
- Winner: Sable
- Turns: 7
- Status Effects Used: 1
- AI Difficulty: Hard
- Critical Hits: 0
- Super Effective Hits: 2
- Resisted Hits: 2
```

## Example 2: 4-Bender Tournament

**Input:**
```
# Create tournament participants
participants = [
    Bender("Ignis", "Fire", 120, 82, 70, 95, [("Inferno Slash", 60), ("Flame Dash", 38), ("Ember Guard", 0), ("Volcanic Burst", 80)]),
    Bender("Kestra", "Water", 128, 78, 85, 68, [("Tidal Crush", 65), ("Ice Shard", 45), ("Mist Shield", 0), ("Maelstrom", 85)]),
    Bender("Terrak", "Earth", 135, 88, 90, 45, [("Stone Avalanche", 70), ("Quake Punch", 48), ("Bulwark", 0), ("Mountain's Wrath", 88)]),
    Bender("Squall", "Air", 105, 65, 55, 100, [("Thunder Gale", 58), ("Razor Wind", 35), ("Updraft", 0, "frozen"), ("Tempest Strike", 72)])
]

tournament = Tournament(participants, "Elemental Arena Championship")
tournament.start_tournament()
```

**Expected Output:**
```
🏆 ELEMENTAL ARENA CHAMPIONSHIP 🏆
Participants: 4 Benders

=== TOURNAMENT BRACKET ===
Semifinal 1: Ignis vs Kestra
Semifinal 2: Terrak vs Squall

=== SEMIFINAL 1 ===
Ignis (Fire, HP: 120/120) VS Kestra (Water, HP: 128/128)

Turn 1: Ignis goes first! (Speed: 95 vs 68)
Ignis used Volcanic Burst!
Not very effective... (Fire is weak against Water)
Kestra took 39 damage!
Kestra HP: 89/128

Turn 2: Kestra strikes back!
Kestra used Maelstrom!
Super Effective! (Water is strong against Fire)
Critical Hit!
Ignis took 379 damage!
Ignis HP: 0/120

Ignis fainted!
Kestra advances to the finals!

=== SEMIFINAL 2 ===
Terrak (Earth, HP: 135/135) VS Squall (Air, HP: 105/105)

Turn 1: Squall goes first! (Speed: 100 vs 45)
Squall used Updraft!
Terrak is now frozen! (3 turns remaining)

Turn 2: Terrak breaks through the cold and strikes!
Terrak used Quake Punch!
Not very effective... (Earth is weak against Air)
Squall took 38 damage!
Squall HP: 67/105

Turn 3: Squall strikes!
Squall used Tempest Strike!
Super Effective! (Air is strong against Earth)
Terrak took 104 damage!
Terrak HP: 31/135

Turn 4: Terrak is frozen and cannot move!
Frozen duration: 1 turn remaining

Turn 5: Squall strikes!
Squall used Thunder Gale!
Super Effective! (Air is strong against Earth)
Terrak took 84 damage!
Terrak HP: 0/135

Terrak fainted!
Squall advances to the finals!

=== CHAMPIONSHIP FINAL ===
Kestra (HP: 89/128) VS Squall (HP: 67/105)

Turn 1: Squall goes first! (Speed: 100 vs 68)
Squall used Tempest Strike!
Kestra took 55 damage!
Kestra HP: 34/128

Turn 2: Kestra strikes back!
Kestra used Maelstrom!
Squall took 121 damage!
Squall HP: 0/105

Squall fainted!
🏆 KESTRA WINS THE ELEMENTAL ARENA CHAMPIONSHIP! 🏆

=== TOURNAMENT STATISTICS ===
Champion: Kestra
Total Battles: 3
Total Turns: 9
Critical Hits: 1
Status Effects: 1
Super Effective Hits: 3

Final Standings:
1st: Kestra
2nd: Squall
3rd: Ignis & Terrak (tied)
```
