````markdown
🎩 Probability Calculator – FCC Project 🎲

Welcome to the **Probability Calculator**! This is one of the final certification projects for the [freeCodeCamp Scientific Computing with Python](https://www.freecodecamp.org/learn) course. The goal? Estimate the probability of drawing certain balls from a hat using simulation! 🧪

---

📚 Project Overview

You're given a hat filled with colored balls (e.g., red, blue, green). The program should simulate drawing a set number of balls from this hat **without replacement** and calculate how often a specific outcome occurs (like drawing at least 2 red and 1 green). The more simulations you run, the better your estimate gets!

This mimics a **Monte Carlo method** — running experiments over and over to get a reliable approximation of probability.

---

🛠️ What You’ll Learn

* Object-oriented programming with Python 👩‍💻  
* Randomization and simulation techniques 🎰  
* Using `Counter` to track outcomes 🔢  
* Deep copying objects safely with `copy.deepcopy()` 🧪  
* Writing clean, testable code 🧼  

---

📁 Project Files

* **`probability_calc.py`** – Contains the `Hat` class and the `experiment()` function.  
* ✅ The code passes all the test cases required for the certification project.

---

## 🚀 How It Works

```python
hat = Hat(blue=5, red=4, green=2)

# We want to know: What's the probability of drawing at least 1 red and 2 green balls
probability = experiment(
    hat=hat,
    expected_balls={"red": 1, "green": 2},
    num_balls_drawn=4,
    num_experiments=2000
)

print("Estimated Probability:", probability)
````

🔁 The function runs 2000 experiments and returns the probability of drawing **at least 1 red and 2 green** in 4-ball draws.

---

📦 Requirements

✅ Python 3.7+
✅ Modules used:

* `random` 🎲
* `copy` 🧬
* `collections.Counter` 🧮

No external packages required!

---

✅ Project Success Criteria

To successfully complete the FreeCodeCamp project, your solution should:

* Create a `Hat` class with a `draw` method.
* Use the `experiment` function to simulate multiple draws.
* Return the estimated probability.
* Pass all automated tests provided by freeCodeCamp.

---

🧠 Tips for Learners

* Make sure you understand what “drawing without replacement” means.
* Test small cases manually to confirm your logic.
* Try changing the number of experiments and see how your probability estimate changes 📊

---
👨‍💻 Author

Created by **Satyajit Chakraborty**
🔗 [LinkedIn](https://www.linkedin.com/in/satyajitchakraborty91)
📘 [Medium Blog](https://medium.com/@satyajit.chakraborty22)
📸 [Instagram](https://www.instagram.com/satyajit_chakraborty_91)

---

💡 Final Thought

> “The question is not how lucky you are in one draw, but how consistent you are over a thousand.” – Probably a Data Scientist 😉
