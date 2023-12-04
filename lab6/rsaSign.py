import random
import hashlib
from sympy import isprime
import math

def generate_large_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << bits - 1) | 1 
        
        if isprime(num):
            return num

def choose_public_exponent(phi_n):
    e = 65537

    while not (1 < e < phi_n and math.gcd(e, phi_n) == 1):
        e = random.randint(2, phi_n - 1)

    return e

hashed_message = '3469f9e6704ea4e5373dbbe60d96eea2291a613ff65a59f348da054ba12a53f7'
hash_bytes = bytes.fromhex(hashed_message)
print("Hashed message:"+ hashed_message + "\n")

bits = 1554
prime1 = generate_large_prime(bits)
prime2 = generate_large_prime(bits)

n = prime1 * prime2
phi_n = (prime1 - 1) * (prime2 - 1)

e = choose_public_exponent(phi_n)

d = pow(e, -1, phi_n)
hashed = int.from_bytes(hash_bytes, byteorder='big')
signature = pow(hashed, d, n)
print("Signature:", signature, "\n")

verification = pow(signature, e, n)

print("Signature is valid:", verification == hashed)
