🟦 Polygon Area Calculator (Rectangle & Square)

This is a simple object-oriented Python project that defines a `Rectangle` class and a `Square` class (as a subclass of `Rectangle`). It allows you to create geometric shapes, compute their properties, visualize them with ASCII art, and even check how many times one shape can fit inside another — all using clean OOP principles! ✨

---

📦 Features

- ✅ Define rectangles and squares with width, height, or side
- 📐 Calculate area, perimeter, and diagonal length
- 🖼 Generate ASCII art pictures of the shapes
- 📏 Count how many times one shape can fit into another
- 🔄 Change dimensions dynamically using setter methods
- 🧬 Inheritance: `Square` extends `Rectangle` and maintains squareness
- 🧾 Informative string representation for easy debugging and display

---

🧠 Object-Oriented Concepts Used

- 🧱 **Encapsulation** – Methods manage access to shape dimensions  
- 🧬 **Inheritance** – `Square` inherits from `Rectangle`  
- 🧩 **Polymorphism** – Methods work across both shape types  
- 🧼 **Method Overriding** – Square redefines width/height setters to maintain equal sides  

---

🧪 Usage Example

```python
# Rectangle example
rect = Rectangle(10, 5)
print(rect.get_area())          # 50
rect.set_height(3)
print(rect.get_perimeter())    # 26
print(rect)                    # Rectangle(width=10, height=3)
print(rect.get_picture())

# Square example
sq = Square(9)
print(sq.get_area())           # 81
sq.set_side(4)
print(sq.get_diagonal())       # 5.656854...
print(sq)                      # Square(side=4)
print(sq.get_picture())

# Fitting shapes
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # 8
