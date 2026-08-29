# 🔲 Problem Statement 1: Conway's Game of Life

Welcome to **Problem Statement 1**! In this challenge, you'll implement and analyze **Conway's Game of Life**, one of the most well-known examples of a **cellular automaton** in computer science.

Devised by mathematician **John Horton Conway** in 1970, the Game of Life is a grid-based simulation where every cell updates on each step according to a fixed set of rules based on its neighbors. No further input is given after the starting grid — the rules alone determine everything that follows. Despite how simple the rules are, the patterns that emerge from them can be surprisingly complex and hard to predict just by looking at the starting state.

This problem statement is split into **three progressive levels**:

---

### 📍 The Levels

| Level | Title | Difficulty | Core Focus |
|---|---|---|---|
| [**🌱 Level 1**](Level_1.md) | **Genesis of the Grid** | Beginner | 2D Grids, 8-Neighbor Moore Counting, Conway's 4 Rules, Bounded Grid Evolution |
| [**🔍 Level 2**](Level_2.md) | **The Pattern Watcher** | Intermediate | Toroidal (Wrap-around) Topologies, Cycle Detection, Center of Mass & Bounding Box |
| [**⏱️ Level 3**](Level_3.md) | **Real-Time Evolution** | Beginner to Intermediate | Timed Loops, Screen Clearing, Real-Time Terminal Playback |

---

## 📜 The Four Rules of Life

Every cell on a two-dimensional grid is either **Alive** (`#` or `1`) or **Dead** (`.` or `0`). In each step (generation), every cell checks its **8 immediate neighbors** (horizontally, vertically, and diagonally):

1. **Underpopulation:** Any live cell with **fewer than 2** live neighbors dies.
2. **Survival:** Any live cell with **2 or 3** live neighbors stays alive.
3. **Overpopulation:** Any live cell with **more than 3** live neighbors dies.
4. **Reproduction:** Any dead cell with **exactly 3** live neighbors becomes alive.

> All updates happen **simultaneously** — a cell's new state must not affect how its neighbors are evaluated in the same step.

---

## 🌟 Common Patterns

```
   Still Life (Block)         Oscillator (Blinker)          Glider
        ##                         ...                       .#.
        ##                         ###                       ..#
                                   ...                        ###
     (stays the same)            (period 2)                (moves diagonally)
```

---

## 🚀 How to Begin

1. Start with [**Level 1 — Genesis of the Grid**](Level_1.md) to implement the core simulation engine.
2. Once Level 1 works correctly, move on to [**Level 2**](Level_2.md) and [**Level 3**](Level_3.md).
3. You may use any programming language (Python, C++, Java, Rust, JavaScript, etc.).
