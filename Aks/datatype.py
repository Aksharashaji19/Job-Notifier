def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key = key.upper()  # Convert key to uppercase for consistency
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')

            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))

            key_index = (key_index + 1) % len(key)
        else:
            encrypted_char = char

        encrypted_text += encrypted_char

    return encrypted_text


def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key = key.upper()  # Convert key to uppercase for consistency
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')

            if char.islower():
                decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                decrypted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))

            key_index = (key_index + 1) % len(key)
        else:
            decrypted_char = char

        decrypted_text += decrypted_char

    return decrypted_text


# Get user input
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

encrypted_text = vigenere_encrypt(plaintext, key)
print("Encrypted:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted:", decrypted_text)