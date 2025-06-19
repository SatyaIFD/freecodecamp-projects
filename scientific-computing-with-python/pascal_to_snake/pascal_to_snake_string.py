def convert_to_snake_case(pascal_or_camel_cased_string):
    # Convert uppercase letters to lowercase and prepend an underscore
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    # Join characters and remove leading underscore, if present
    return ''.join(snake_cased_char_list).lstrip('_')

def main():
    print(convert_to_snake_case('IAmAPascalCasedString'))

main()
