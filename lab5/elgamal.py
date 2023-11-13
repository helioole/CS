import random

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return result

def generate_keys(p, g):
    private_key = random.randint(1, p - 1)

    public_key = pow(g, private_key, p)

    return private_key, public_key

def elgamal_encrypt(message, p, g, public_key):
    k = random.randint(1, p - 2)

    C1 = pow(g, k, p)
    C2 = (message * pow(public_key, k, p)) % p

    return C1, C2

def elgamal_decrypt(C1, C2, p, private_key):
    s = pow(C1, private_key, p)

    s_inv = pow(s, -1, p)

    decrypted_message = (C2 * s_inv) % p

    return decrypted_message

p = 323170060713110073001535134778251633624880571334890751745884341392698068341362100027920563626401646854585563579353308169288829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696961297438562417412362372251973464026918557977679768023014625397933058015226858730761197532436467475855460715043896844940366130495768128542959588576514223145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696961297438562490632338072839127039
g = 2

private_key, public_key = generate_keys(p, g)

message = 8297991111189910111097327311410511097
C1, C2 = elgamal_encrypt(message, p, g, public_key)
decrypted_message = elgamal_decrypt(C1, C2, p, private_key)

print(f"Original Message: {message}")
print("Public key:", public_key)
print("Private key:", private_key)
print(f"Encrypted Message (C1, C2): ({C1}, {C2})")
print(f"Decrypted Message: {decrypted_message}")
