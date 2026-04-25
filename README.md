# Sudoku Solver using AC-3 and Backtracking

## Developed by Ubaidullah | Constraint Satisfaction Problem (CSP) Project

---

## Overview

This project implements a **Sudoku Solver** using Artificial Intelligence techniques, specifically **Constraint Satisfaction Problem (CSP)** methods.

The solver combines:
- AC-3 (Arc Consistency Algorithm 3)
- Backtracking Search
- Forward Checking
- Minimum Remaining Values (MRV) heuristic

It is designed to efficiently solve Sudoku puzzles of varying difficulty levels by reducing the search space using constraint propagation before applying backtracking.

---

## Problem Type

This project solves Sudoku as a **Constraint Satisfaction Problem (CSP)** where:
- Each cell is a variable
- Domain is numbers 1–9
- Constraints:
  - No repeated number in row
  - No repeated number in column
  - No repeated number in 3×3 subgrid

---

## Algorithms Used

### 1. AC-3 Algorithm (Arc Consistency)

AC-3 enforces consistency between variables by removing inconsistent values from domains.

Purpose:
- Reduces search space before backtracking
- Removes impossible values early

Effect:
- Improves performance significantly
- Helps detect unsolvable puzzles early

---

### 2. Backtracking Search

Backtracking explores possible assignments recursively.

Features:
- Chooses variable with Minimum Remaining Values (MRV)
- Tries possible values one by one
- Backtracks on failure

---

### 3. Forward Checking

After assigning a value:
- Removes that value from neighbors
- Stops early if any domain becomes empty

---

## Key Features

- Solves Sudoku using AI techniques
- Supports multiple difficulty levels:
  - Easy
  - Medium
  - Hard
  - Very Hard
- Automatic puzzle validation
- Performance tracking:
  - Backtracking calls
  - Failures
  - Execution time

---

## How It Works

1. Load Sudoku puzzle
2. Initialize domains for each cell
3. Apply AC-3 to enforce constraints
4. If solvable, start backtracking search
5. Use forward checking during assignment
6. Return solved board or failure

---

## Heuristic Used

### Minimum Remaining Values (MRV)

Selects the cell with the smallest domain first:

- Reduces branching factor
- Improves efficiency

---

## Input Format

Each Sudoku puzzle is represented as 9 strings:

- '0' represents an empty cell
- '1–9' represent fixed values



---

## Output

The program prints:
- Solved Sudoku board
- Number of backtracking calls
- Number of failures
- Execution time in milliseconds

---

## Example Difficulties

The project includes predefined puzzles:

- EASY
- MEDIUM
- HARD
- VERY HARD

---

## How to Run

### 1. Install Python
Make sure Python 3 is installed on your system.

Check version:
``bash
python --version

---

## Technologies Used

- Python
- Data Structures (Sets, Dictionaries, Deque)
- Constraint Satisfaction Problem (CSP) techniques
- Artificial Intelligence Search Algorithms

---

## Learning Outcomes

This project helps understand:

- Constraint Satisfaction Problems
- AC-3 arc consistency algorithm
- Backtracking optimization techniques
- Forward checking in AI
- Heuristic-based search (MRV)

---

## Future Improvements

- GUI-based Sudoku solver
- Step-by-step visualization
- Advanced heuristics (Degree heuristic, LCV)
- Performance comparison with other solvers
- Web-based interactive version

---

## Author

Ubaidullah  
BS Computer Science Student  
Focus: Artificial Intelligence, Algorithms, and Problem Solving
