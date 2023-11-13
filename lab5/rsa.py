msg = "Racovcena Irina"
m = int(''.join(str(ord(char)) for char in msg))
print("Message: Racovcena Irina, message as integer:", m, end="\n\n")

import random
from sympy import isprime

def generate_large_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1

        if isprime(num):
            return num

bits = 1024
prime1 = generate_large_prime(bits)
prime2 = generate_large_prime(bits)

n = prime1 * prime2

phi = (prime1 - 1) * (prime2 - 1)

e = 65537

d = pow(e, -1, phi)

public_key = (n, e)
private_key = (n, d)

print("Prime 1:", prime1)
print("Prime 2:", prime2)
print("n:", n)
print("Euler totient function φ(n) = (p − 1)(q − 1): ", phi)
print("Public Key (n, e):", public_key)
print("Private Key (n, d):", private_key)

c = pow(m, e, n)
print("\nEncrypted message (ciphertext):", c)

m_decrypted = pow(c, d, n)
print("Decrypted message (numeric):", m_decrypted)