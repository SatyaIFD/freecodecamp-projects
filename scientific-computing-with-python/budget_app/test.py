from budget import Category, create_spend_chart

# Create budget categories
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

# Sample transactions
food.deposit(1000, "initial deposit")
food.withdraw(200.45, "groceries")
food.withdraw(50.15, "restaurant")
food.transfer(100, entertainment)

entertainment.withdraw(50, "movie night")
entertainment.withdraw(30, "concert")

business.deposit(2000, "client deposit")
business.withdraw(300, "software tools")

# Display ledgers
print(food)
print(entertainment)
print(business)

# Display spend chart
print(create_spend_chart([food, entertainment, business]))
