# 🛣️ Shortest Path Algorithm in Python

This is a practice project completed as part of [freeCodeCamp](https://www.freecodecamp.org/)'s **"Learn Algorithm Design by Building a Shortest Path Algorithm"** course.

The goal of the project is to build a **shortest path algorithm** from scratch using Python and weighted graphs.

---

## 🎯 Learning Objectives

✅ Understand how weighted graphs function  
✅ Design an algorithm to compute shortest paths  
✅ Track minimum distances and actual paths  
✅ Work with Python dictionaries and lists  
✅ Develop core algorithmic problem-solving skills

---

## 🧩 Problem Overview

You're given a graph where nodes are connected by edges with weights.  
The goal is to calculate the **minimum total weight** needed to reach each node from a starting point, and show the actual **path taken**.

---

## 🛠 How It Works

The algorithm:

- Starts at a given node and initializes distances to all others as infinite
- Uses a greedy approach to always visit the next node with the smallest known distance
- Updates both the **distance** and the **path** if a better one is found
- Continues until all nodes have been visited

---

## 🧪 Example Graph

```python
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}

## 🖥 Sample Output

A-F distance: 8
Path: A -> B -> F