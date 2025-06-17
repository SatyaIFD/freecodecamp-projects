def verify_card_number(card_number):
    """
    Verifies a card number using the Luhn algorithm.
    Returns True if valid, False otherwise.
    """
    card_number_reversed = card_number[::-1]
    sum_of_odd_digits = sum(int(d) for d in card_number_reversed[::2])

    sum_of_even_digits = 0
    for d in card_number_reversed[1::2]:
        doubled = int(d) * 2
        if doubled >= 10:
            doubled = (doubled // 10) + (doubled % 10)
        sum_of_even_digits += doubled

    total = sum_of_odd_digits + sum_of_even_digits
    print(total)
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1141'
    # Remove spaces and hyphens
    cleaned_number = card_number.translate(str.maketrans('', '', '- '))
    
    if verify_card_number(cleaned_number):
        print('VALID!')
    else:
        print('INVALID!')

if __name__ == '__main__':
    main()
