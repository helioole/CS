def caesar_cipher(text, key, mode):
    result = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    modified = text.replace(" ", "").upper()
    
    for char in modified:
        if char in alphabet:
            if mode == 1:
                result += alphabet[(alphabet.index(char) + key) % 26]
            elif mode == 2:
                result += alphabet[(alphabet.index(char) - key) % 26]
        else:
            return "Cipher accepts only English letters"
    
    return result

def main():
    while True:
        print("Caesar Cipher")
        print("1. Encrypt")
        print("2. Decrypt")
        
        choice = input("Enter your choice: ")
        message = input("Enter the message: ")
        key = int(input("Enter the key (1-25): "))

        if 1 > key or key> 25:
            print("Invalid key. Key must be between 1 and 25.")
        else:
            if choice == '1':
                    ciphertext = caesar_cipher(message, key, 1)
                    print("Encrypted message:", ciphertext)

            elif choice == '2':
                    decrypted_message = caesar_cipher(message, key, 2)
                    print("Decrypted message:", decrypted_message)

            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()