import re
import secrets
import string

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Generates a secure random password meeting specific character constraints.

    Parameters:
    - length (int): Total length of the password (default 16)
    - nums (int): Minimum number of digits required in the password
    - special_chars (int): Minimum number of special characters required
    - uppercase (int): Minimum number of uppercase letters required
    - lowercase (int): Minimum number of lowercase letters required

    Returns:
    - str: A randomly generated password that meets all the constraints
    """

    # Define character sets
    letters = string.ascii_letters            # a-z + A-Z
    digits = string.digits                    # 0-9
    symbols = string.punctuation              # Special characters like !@#$%^&*

    # Combine all characters into a pool for random selection
    all_characters = letters + digits + symbols

    while True:
        password = ''.join(secrets.choice(all_characters) for _ in range(length))

        # Define constraints to validate the password
        constraints = [
            (nums, r'\d'),                     # Digits
            (special_chars, fr'[{symbols}]'),  # Special characters
            (uppercase, r'[A-Z]'),             # Uppercase letters
            (lowercase, r'[a-z]')              # Lowercase letters
        ]

        # Check if password meets all constraints using regex
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break  # Valid password generated

    return password

if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)
