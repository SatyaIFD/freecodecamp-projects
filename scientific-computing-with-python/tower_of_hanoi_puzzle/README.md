# 🏗️ Tower of Hanoi - Recursive Python Solution

This is a classic **recursive implementation** of the Tower of Hanoi problem using plain Python lists as rods (`A`, `B`, `C`). It’s perfect for understanding recursion, stack behavior, and solving algorithmic challenges.

---

## 📁 Repository Purpose

This practice project is part of [freeCodeCamp](https://www.freecodecamp.org/) coding exercises and is intended to help you:

- Understand how recursion works step-by-step
- Solve the Tower of Hanoi algorithmically
- Visualize how data structures like stacks are used

---

## 🧠 Problem Statement

Move `n` disks from the source rod to the target rod using an auxiliary rod, **obeying these rules**:

1. Only one disk can be moved at a time.
2. No disk can be placed on top of a smaller disk.
3. Only the top disk of any rod may be moved.

---

## ▶️ How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/YOUR-USERNAME/tower-of-hanoi
   cd tower-of-hanoi

---

🧩 Example Output (for 3 disks)
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
...
