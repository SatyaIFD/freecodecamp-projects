🕒 Time Calculator

This is a solution to the **Time Calculator** project from the [freeCodeCamp Scientific Computing with Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

The goal is to build a function that performs time arithmetic using a 12-hour clock format and optionally accounts for the day of the week.

---

📘 Project Description

The `add_time()` function takes a start time, a duration, and an optional weekday, and returns the new time after adding the duration. It handles:

- Conversion between 12-hour and 24-hour time formats
- Time overflow across days
- Optional calculation of the new weekday
- Formatting the output in a user-friendly 12-hour format

---

🧠 Skills Demonstrated

- String manipulation
- Time arithmetic
- Control flow and conditionals
- Working with lists and modular arithmetic
- Optional function arguments

---

🧪 Function Specification

```python
add_time(start_time, duration, start_day=None)

---

✅ Example Usage

add_time("3:00 PM", "3:10")
# Returns: "6:10 PM"

add_time("11:30 AM", "2:32", "Monday")
# Returns: "2:02 PM, Monday"

add_time("10:10 PM", "3:30")
# Returns: "1:40 AM (next day)"

add_time("11:43 PM", "24:20", "tuesday")
# Returns: "12:03 AM, Thursday (2 days later)"

