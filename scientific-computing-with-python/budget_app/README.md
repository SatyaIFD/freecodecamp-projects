💰 Budget App

A Python-based budgeting tool that allows you to track spending across categories and visualize expenses in a clean, text-based chart.

Built as part of the **freeCodeCamp Scientific Computing with Python** certification project.

---

📦 Features

- 📂 Create budget categories (e.g. Food, Entertainment, Business)
- 💵 Deposit and withdraw funds with optional descriptions
- 🔁 Transfer funds between categories
- 📊 Generate a vertical **spend chart** by category
- ✅ Passes all 24 unit tests from the freeCodeCamp Budget App project

---

🚀 Quick Example

```python
from budget import Category, create_spend_chart

food = Category("Food")
food.deposit(900, "deposit")
food.withdraw(105.55, "groceries")

entertainment = Category("Entertainment")
entertainment.deposit(500)
entertainment.withdraw(33.40)

food.transfer(30, entertainment)

print(food)
print(entertainment)

print(create_spend_chart([food, entertainment]))

---

🖨️ Sample Output

*************Food*************
deposit                 900.00
groceries              -105.55
Transfer to Entertainment -30.00
Total: 764.45

**********Entertainment**********
Initial deposit         500.00
-33.40                 -33.40
Transfer from Food       30.00
Total: 496.60

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60|    o     
 50|    o     
 40| o  o     
 30| o  o     
 20| o  o     
 10| o  o     
  0| o  o     
    ----------
     F  E  B  
     o  n  u  
     o  t  s  
     d  e  i  
        r  n  
        t  e  
        a  s  
        i     
        n     
        m     
        e     
        n     
        t     

