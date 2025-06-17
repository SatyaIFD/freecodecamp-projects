# Credit Card Validator (Luhn Algorithm)

This Python script checks whether a credit card number is valid using the **Luhn algorithm**.

## 🔢 How it works:

1. Strips hyphens or spaces from the number.
2. Doubles every second digit from the right.
3. Adds all digits together.
4. If the total is divisible by 10, the card number is valid.

## 🧪 Example

```python
card_number = '4111-1111-4555-1141'
