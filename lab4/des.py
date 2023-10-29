INITIAL_PERMUTATION = [
    57, 49, 41, 33, 25, 17, 9, 
    1, 58, 50, 42, 34, 26, 18, 
    10, 2, 59, 51, 43, 35, 27,
    19, 11, 3, 60, 52, 44, 36, 
    63, 55, 47, 39, 31, 23, 15, 
    7, 62, 54, 46, 38, 30, 22, 
    14, 6, 61, 53, 45, 37, 29, 
    21, 13, 5, 28, 20, 12, 4
]

def generate_k_plus(key):
    if len(key) != 8:
        raise ValueError("The key must be 8 characters long.")

    binary_key = ''.join(format(ord(char), '08b') for char in key)
    k_plus = [binary_key[i - 1] for i in INITIAL_PERMUTATION]

    return k_plus

def print_k_plus(data, title):
    print(title + " as a table:")
    for i in range(0, len(data), 7):
        row = data[i:i + 7]
        print(' '.join(row))

def print_k(data, title):
    print(title + " as a table:")
    for i in range(0, len(data), 8):
        row = data[i:i + 8]
        print(' '.join(row))

key = input("Enter the keyword: ")
k_plus = generate_k_plus(key)

print_k(''.join(format(ord(char), '08b') for char in key), "K for the key '{}'".format(key))
print_k_plus(k_plus, "K+ for the key '{}'".format(key))
print("K+ for the key '{}' as a binary string:".format(key))
print(''.join(k_plus))