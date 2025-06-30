class Category:
    def __init__(self, name):
        # Initialize category with a name and an empty ledger
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        # Add a deposit entry to the ledger
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        # Withdraw funds if available, and record it
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        # Calculate current balance by summing all amounts
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        # Transfer funds to another category if possible
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        # Check if enough balance exists
        return self.get_balance() >= amount

    def __str__(self):
        # Format the ledger output as a string
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]  # Limit description to 23 chars
            amt = f"{entry['amount']:>7.2f}"  # Format amount to 2 decimal places, right-aligned
            items += f"{desc:<23}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Step 1: Calculate total spent per category
    spent = []
    total_spent = 0
    for category in categories:
        category_spent = sum(-entry['amount'] for entry in category.ledger if entry['amount'] < 0)
        spent.append(category_spent)
        total_spent += category_spent

    # Step 2: Calculate each category’s percentage of total spent
    percentages = [(int((amount / total_spent) * 100) // 10) * 10 for amount in spent]

    # Step 3: Start chart with the title
    chart = "Percentage spent by category\n"

    # Step 4: Add percentage rows (100 to 0, step -10)
    for i in range(100, -1, -10):
        row = f"{i:>3}|"
        for percent in percentages:
            row += " o" if percent >= i else "  "
        chart += row + "  \n"  # Two spaces at the end

    # Step 5: Add horizontal separator line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Step 6: Add category names vertically under the bars
    max_len = max(len(category.name) for category in categories)
    padded_names = [category.name.ljust(max_len) for category in categories]

    for i in range(max_len):
        row = "     "  # Indentation for the left margin
        for name in padded_names:
            row += name[i] + "  "
        chart += row.rstrip() + "  \n"  # Strip right and add final 2 spaces

    return chart.rstrip("\n")  # Ensure no trailing newline at the end
