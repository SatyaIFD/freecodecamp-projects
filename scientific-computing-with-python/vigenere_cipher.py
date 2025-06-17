# vigenere_cipher.py

text = 'mrttaqrhknsw ih puggrur'
custom_key = 'happycoding'

def vigenere(message, key, direction=1):
    """
    Applies the Vigenère cipher for encryption or decryption.

    Parameters:
        message (str): The input text to encode or decode.
        key (str): The cipher key.
        direction (int): 1 for encryption, -1 for decryption.

    Returns:
        str: The processed message.
    """
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.index(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

def encrypt(message, key):
    """Encrypts the message using the given key."""
    return vigenere(message, key, direction=1)

def decrypt(message, key):
    """Decrypts the message using the given key."""
    return vigenere(message, key, direction=-1)

# Run decryption
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'Decrypted text: {decryption}\n')
