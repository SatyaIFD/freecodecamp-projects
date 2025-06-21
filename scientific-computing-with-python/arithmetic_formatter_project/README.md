# Arithmetic Arranger

This Python script arranges a list of arithmetic problems (addition and subtraction) vertically and side-by-side. It also optionally displays the answers.

This is a solution to the [FreeCodeCamp Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) challenge: **Arithmetic Formatter**.

---

## 📦 Features

- Supports addition (`+`) and subtraction (`-`)
- Validates correct input format and operand limits
- Arranges up to 5 arithmetic problems at once
- Optionally displays answers with a parameter toggle

---

## 🧠 Example

```python
from arithmetic_arranger import arithmetic_arranger

print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], show_answers=True))


Output:

   32      1      9999      523
+   8  - 3801    + 9999    -  49
----  ------    ------    -----
  40   -3800     19998      474
