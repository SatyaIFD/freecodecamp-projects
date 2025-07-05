🧠 Equation Solver — freeCodeCamp Practice Project

Welcome! This is a Python project for practicing object-oriented programming as part of the **freeCodeCamp** curriculum. It focuses on building a solver for **linear** and **quadratic equations**.

---

📌 What You'll Learn

✅ Abstract base classes  
✅ Inheritance and polymorphism  
✅ String formatting with f-strings  
✅ Match/case (Python 3.10+)  
✅ Input validation  
✅ Clean and aligned CLI output

---

## ✨ Features

- 🔁 Supports **Linear** (e.g., `2x + 3 = 0`) and **Quadratic** (e.g., `x² + 2x + 1 = 0`) equations
- 📈 Outputs:
  - Solutions (real roots only)
  - Details like slope, intercept, vertex, concavity
- 🎯 Centered and right-aligned formatting using f-strings
- 📚 Great for visualizing math in Python!

---

🧪 Example Usage

```python
from equations import LinearEquation, QuadraticEquation, solver

# Linear equation: 2x + 3 = 0
eq1 = LinearEquation(2, 3)
print(solver(eq1))

# Quadratic equation: x² + 2x + 1 = 0
eq2 = QuadraticEquation(1, 2, 1)
print(solver(eq2))

---

📤 Example Output

➕ Linear Equation

----Linear Equation-----

       2x +3 = 0        

-------Solutions--------

       x = -1.500       

--------Details---------

slope =           2.000
y-intercept =     3.000


➗ Quadratic Equation

---Quadratic Equation---

    x**2 +2x +1 = 0     

-------Solutions--------

       x = -1.000       

--------Details---------

concavity =      upwards
min =    (-1.000, 0.000)
