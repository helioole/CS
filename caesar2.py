def caesar_cipher(text, key1, key2, mode):
    result = ""
    mod_alphabet = permutation(key1, key2)
    mod_text = text.replace(" ", "").upper()
    
    for char in mod_text:
        if char in mod_alphabet:
            if mode == 1:
                new_index = (mod_alphabet.index(char) + key1) % 26
                print(new_index)
                result += mod_alphabet[new_index]
            elif mode == 2:
                new_index = (mod_alphabet.index(char) - key1) % 26

            new_char = mod_alphabet[new_index]
            result += new_char
        else:
            print("This character is not allowed")
    
    return result

def permutation(key1, key2):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rest_alph = ""
    modified = ""
    key2 = key2.upper()

    if len(key2) < 6:
        return "The key should be a word at least of 7 characters"

    for char in alphabet:
        if char not in key2:
            rest_alph += char

    modified = key2 + rest_alph

    # iterate again to remove duplicates
    seen = ""
    final = ""
    for char in modified:
        if char not in seen:
            final += char
            seen += char

    # apply shift
    key1 = key1 % len(final)
    return final[key1:] + final[:key1]

def main():
    while True:
        print("Caesar Cipher with Permutations")
        print("1. Encrypt")
        print("2. Decrypt")
        choice = input("Enter your choice: ")
        message = input("Enter the message: ")
        key1 = int(input("Enter the key (1-25): "))
        key2 = str(input("Enter the key word: "))

        if 1 >= key1 or key1>= 25:
            print("Invalid key. Key must be between 1 and 25.")
        else:
            if choice == '1':
                ciphertext = caesar_cipher(message, key1, key2, 1)
                modified_alphabet = permutation(key1, key2)
                print("Modified alphabet:", modified_alphabet)
                print("Encrypted message:", ciphertext)

            elif choice == '2':
                decrypted_message = caesar_cipher(message, key1, key2, 2)
                modified_alphabet = permutation(key1, key2)
                print("Modified alphabet:", modified_alphabet)
                print("Decrypted message:", decrypted_message)

            else:
                print("Invalid choice. Please enter 1, 2.")

if __name__ == "__main__":
    main()