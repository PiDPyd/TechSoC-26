# 🌱 Level 1 — Genesis of the Grid

[![Difficulty](https://img.shields.io/badge/Difficulty-Beginner-2ea44f?style=flat-square)](#)
[![Concepts](https://img.shields.io/badge/Concepts-2D%20Arrays%20|%20Nested%20Loops%20|%20Conditions%20|%20Functions-0d6efd?style=flat-square)](#)

---

## Background

Conway's Game of Life is a grid simulation where every cell updates each step based on a fixed set of rules applied to its neighbors. You'll build the core engine: read a starting grid, simulate it for a number of steps, and report what happens.

---

## The Four Rules of Conway's Game of Life

In each step (generation), every cell on an $R \times C$ grid looks at its **8 surrounding neighbors** (Moore neighborhood: top-left, top, top-right, left, right, bottom-left, bottom, bottom-right). Cells outside the grid boundaries count as **dead**.

1. **Underpopulation:** Any live cell with **fewer than 2** live neighbors dies.
2. **Survival:** Any live cell with **2 or 3** live neighbors stays alive.
3. **Overpopulation:** Any live cell with **more than 3** live neighbors dies.
4. **Reproduction:** Any dead cell with **exactly 3** live neighbors becomes alive.

> All cells update **simultaneously** — a cell's new state must not affect how its neighbors are evaluated in the same step.

---

## Your Task

Write a program that:

1. Reads the grid dimensions: rows `R` and columns `C`.
2. Reads the number of generations to simulate `G`.
3. Reads `R` lines of `C` characters each — `.` for dead, `#` for alive.
4. Simulates the grid for `G` generations.
5. Prints:
   - **Initial Population:** live cell count at generation 0
   - **Final Population:** live cell count after generation $G$
   - **Peak Population:** the highest live cell count seen from generation $0$ to $G$
   - **Final Grid State:** the grid after $G$ generations

---

## Rules

- Any programming language (Python, C++, C, Java, Rust, JavaScript, etc.)
- Single program file, runs in your terminal
- No GUI, no web app, no framework
- No external simulation libraries

---

## Input Format

```
R C
G
<row 1>
<row 2>
...
<row R>
```

- Line 1: `R` and `C` ($1 \le R, C \le 100$) — rows and columns.
- Line 2: `G` ($0 \le G \le 1000$) — number of generations to simulate.
- Next `R` lines: a string of length `C` containing only `.` and `#`.

---

## Output Format

```
Initial Population: <int>
Final Population: <int>
Peak Population: <int>
Final Grid:
<row 1>
<row 2>
...
<row R>
```

---

## Concepts You'll Use

| Concept | Description |
|---|---|
| 2D Arrays / Matrices | Representing the $R \times C$ grid of cells |
| Nested Loops | Iterating across rows and columns to inspect neighbors |
| Moore Neighborhood | Checking 8 directions $(dr \in \{-1, 0, 1\}, dc \in \{-1, 0, 1\})$ |
| Double Buffering | Keeping a copy of the previous grid to update states simultaneously |
| Boundary Checks | Keeping neighbor coordinates within $[0, R-1]$ and $[0, C-1]$ |
| State Tracking | Tracking initial, peak, and final live cell counts |

---

## Test Cases

<details>
<summary><strong>🧪 Test Case 1 — The Blinker (1 Generation)</strong></summary>
<br>

*A horizontal line of 3 cells rotates to a vertical line.*

**Input:**
```
5 5
1
.....
.###.
.....
.....
.....
```

**Output:**
```
Initial Population: 3
Final Population: 3
Peak Population: 3
Final Grid:
..#..
..#..
..#..
.....
.....
```
</details>

<details>
<summary><strong>🧪 Test Case 2 — The Blinker (2 Generations)</strong></summary>
<br>

*After 2 generations, it oscillates back to its original state.*

**Input:**
```
5 5
2
.....
.###.
.....
.....
.....
```

**Output:**
```
Initial Population: 3
Final Population: 3
Peak Population: 3
Final Grid:
.....
.###.
.....
.....
.....
```
</details>

<details>
<summary><strong>🧪 Test Case 3 — The Block (Still Life, 5 Generations)</strong></summary>
<br>

*A 2x2 square never changes — each cell always has exactly 3 neighbors.*

**Input:**
```
4 4
5
....
.##.
.##.
....
```

**Output:**
```
Initial Population: 4
Final Population: 4
Peak Population: 4
Final Grid:
....
.##.
.##.
....
```
</details>

<details>
<summary><strong>🧪 Test Case 4 — The Glider (4 Generations)</strong></summary>
<br>

*A glider shifts 1 diagonal step every 4 generations.*

**Input:**
```
5 5
4
.#...
..#..
###..
.....
.....
```

**Output:**
```
Initial Population: 5
Final Population: 5
Peak Population: 5
Final Grid:
.....
..#..
...#.
.###.
.....
```
</details>

<details>
<summary><strong>🧪 Test Case 5 — The Toad Oscillator</strong></summary>
<br>

*A 6-cell period-2 oscillator.*

**Input:**
```
6 6
1
......
..###.
.###..
......
......
......
```

**Output:**
```
Initial Population: 6
Final Population: 6
Peak Population: 6
Final Grid:
...#..
.#..#.
.#..#.
..#...
......
......
```
</details>

<details>
<summary><strong>🧪 Test Case 6 — The Beacon Oscillator</strong></summary>
<br>

*Two touching 2x2 blocks oscillate with period 2.*

**Input:**
```
6 6
1
......
.##...
.##...
...##.
...##.
......
```

**Output:**
```
Initial Population: 8
Final Population: 6
Peak Population: 8
Final Grid:
......
.##...
.#....
....#.
...##.
......
```
</details>

<details>
<summary><strong>🧪 Test Case 7 — Underpopulation & Extinction</strong></summary>
<br>

*Isolated cells have 0 neighbors and die.*

**Input:**
```
3 3
1
#..
...
..#
```

**Output:**
```
Initial Population: 2
Final Population: 0
Peak Population: 2
Final Grid:
...
...
...
```
</details>

<details>
<summary><strong>🧪 Test Case 8 — Overpopulation & Birth Surge</strong></summary>
<br>

*A cross pattern triggers births and overpopulation deaths at the same time.*

**Input:**
```
3 3
1
.#.
###
.#.
```

**Output:**
```
Initial Population: 5
Final Population: 8
Peak Population: 8
Final Grid:
###
#.#
###
```
</details>

<details>
<summary><strong>🧪 Test Case 9 — Zero Generations (Edge Case)</strong></summary>
<br>

*When G = 0, the grid stays identical to the initial state.*

**Input:**
```
3 3
0
.##
.#.
...
```

**Output:**
```
Initial Population: 3
Final Population: 3
Peak Population: 3
Final Grid:
.##
.#.
...
```
</details>

<details>
<summary><strong>🧪 Test Case 10 — Bounded Boundary Decay</strong></summary>
<br>

*Border cells have fewer neighbors since out-of-bound cells are dead.*

**Input:**
```
4 4
1
####
....
....
####
```

**Output:**
```
Initial Population: 8
Final Population: 8
Peak Population: 8
Final Grid:
.##.
.##.
.##.
.##.
```
</details>

---

*Once Level 1 works, move on to [Level 2 — The Pattern Watcher](Level_2.md).*
