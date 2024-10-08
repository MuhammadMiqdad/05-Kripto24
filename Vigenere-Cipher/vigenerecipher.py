# NAMA  : Muhammad Miqdad A.J
# NPM   : 140810220005
# KELAS : A

# Vigenère Cipher Encryption
def vigenere_encrypt(plaintext, key):
    key = key.upper()
    result = []
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            if char.isupper():
                result.append(chr((ord(char) - 65 + shift) % 26 + 65))
            else:
                result.append(chr((ord(char) - 97 + shift) % 26 + 97))
            key_index += 1
        else:
            result.append(char)
    
    return ''.join(result)

# Vigenère Cipher Decryption
def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    result = []
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            if char.isupper():
                result.append(chr((ord(char) - 65 - shift + 26) % 26 + 65))
            else:
                result.append(chr((ord(char) - 97 - shift + 26) % 26 + 97))
            key_index += 1
        else:
            result.append(char)
    
    return ''.join(result)

# Function to encrypt a file using Vigenère Cipher
def encrypt_file_vigenere(input_file, output_file, key):
    with open(input_file, 'r') as file:
        data = file.read()
    encrypted_data = vigenere_encrypt(data, key)
    with open(output_file, 'w') as file:
        file.write(encrypted_data)
    print(f"File '{input_file}' encrypted successfully to '{output_file}'.")

# Function to decrypt a file using Vigenère Cipher
def decrypt_file_vigenere(input_file, output_file, key):
    with open(input_file, 'r') as file:
        data = file.read()
    decrypted_data = vigenere_decrypt(data, key)
    with open(output_file, 'w') as file:
        file.write(decrypted_data)
    print(f"File '{input_file}' decrypted successfully to '{output_file}'.")

# Main menu for Vigenère Cipher
def menu_vigenere():
    while True:
        print("\nVigenère Cipher Menu")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Encrypt file")
        print("4. Decrypt file")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            text = input("Enter text to encrypt: ")
            key = input("Enter key: ")
            encrypted_text = vigenere_encrypt(text, key)
            print(f"Encrypted Text: {encrypted_text}")
        
        elif choice == '2':
            cipher = input("Enter text to decrypt: ")
            key = input("Enter key: ")
            decrypted_text = vigenere_decrypt(cipher, key)
            print(f"Decrypted Text: {decrypted_text}")
        
        elif choice == '3':
            input_file = input("Enter the input file path to encrypt: ")
            output_file = input("Enter the output file path: ")
            key = input("Enter key: ")
            encrypt_file_vigenere(input_file, output_file, key)

        elif choice == '4':
            input_file = input("Enter the input file path to decrypt: ")
            output_file = input("Enter the output file path: ")
            key = input("Enter key: ")
            decrypt_file_vigenere(input_file, output_file, key)

        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the Vigenère Cipher menu
if __name__ == "__main__":
    menu_vigenere()
