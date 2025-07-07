Projectile Trajectory Calculator 🏹🧮

Welcome to the **Projectile Trajectory Calculator** project! This little Python program models the flight of a projectile launched at an angle, computing and visualizing its path using physics principles. Perfect for physics lovers, coders, or anyone curious about motion! 🎉

---

🚀 What Does It Do?

* **Calculates projectile flight details** like speed, height, launch angle, and horizontal displacement.
* **Generates a table of coordinates** representing the (x, y) position of the projectile at every step.
* **Builds a visual trajectory graph** right in the terminal, showing the path of the projectile using symbols.
* Adds helpful **x and y axes ticks** to make the graph easy to read.
* Wraps everything neatly inside easy-to-use **Python classes** and a utility function.

---

⚙️ How Does It Work?

1. **Projectile Class**:

   * Takes initial speed, launch height, and angle.
   * Uses physics formulas to calculate displacement and y-coordinates over time.
   * Returns all the coordinates of the projectile’s flight.

2. **Graph Class**:

   * Takes the list of coordinates and rounds them for graphing.
   * Builds a matrix representing the graph with spaces and projectile symbols.
   * Adds axes to make it visually clear where the projectile flies.
   * Converts the matrix into a nice multiline string for terminal display.

3. **Utility Function (`projectile_helper`)**:

   * Takes user inputs for speed, height, and angle.
   * Prints out the projectile details, the coordinate table, and the trajectory graph.

---

🧑‍💻 How To Run

1. Clone or download the repo.
2. Run the Python file (e.g., `python projectile.py`).
3. You’ll see detailed output including:

   * Projectile info
   * Coordinates table
   * Visual trajectory graph

You can modify the parameters by changing the arguments in the `projectile_helper()` call.

---

🎯 Example Output

```
Projectile details:
speed: 10 m/s
height: 3 m
angle: 45°
displacement: 12.6 m

  x      y
  0   3.00
  1   3.90
  2   4.61
  ...

⊣     ∙       
⊣  ∙∙∙ ∙∙∙    
⊣ ∙       ∙   
⊣∙         ∙  
⊣           ∙ 
⊣            ∙
⊣             
 TTTTTTTTTTTTT
```

---

📚 Concepts Covered

* Python OOP (classes, properties, setters)
* Physics formulas for projectile motion
* Working with lists of tuples and matrices
* String formatting and terminal output
* Coordinate transformations (graph inversion)

---

## 🙏 Acknowledgments

This project is a practice challenge from **FreeCodeCamp** — big thanks to their amazing curriculum for inspiring this build! 💙

---

🚀 Want to Contribute?

Feel free to open an issue or submit a pull request if you want to improve the code, add features, or fix bugs! Every contribution counts! 🤝

---

Thanks for checking this out! If you find this helpful, don’t forget to ⭐ the repo! 🌟

---

**Happy coding and shooting projectiles! 🎉🔭**



