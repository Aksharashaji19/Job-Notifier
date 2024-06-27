def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + key) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + key) % 26 + 97)
        else:
            encrypted_char = char

        ciphertext += encrypted_char

    return ciphertext


def special_encrypt(plaintext, key):
    encrypted_text = encrypt(plaintext, key)
    return encrypted_text.replace(' ', '#')

def special_decrypt(plaintext, key):
    encrypted_text = decrypt(plaintext, key)
    return encrypted_text.replace('#', ' ')


def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)


def calculate_frequency(text):
    frequency = {}
    total_chars = len(text)

    for char in text:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1

    frequency_percentage = {char: (count / total_chars) * 100 for char, count in frequency.items()}
    return frequency_percentage


def main():
    plaintext = input("Enter the plaintext: ")
    key = int(input("Enter the encryption key (an integer): "))

    encrypted_text = special_encrypt(plaintext, key)
    print("Encrypted Text:", encrypted_text)




    crypted_text = special_decrypt(encrypted_text, key)
    print("Decrypted Text:", crypted_text)

    plaintext_frequency = calculate_frequency(plaintext.lower())
    print("Frequency Percentage in Plaintext:")
    for char, percentage in plaintext_frequency.items():
        print(f"{char}: {percentage:.2f}%")



main()