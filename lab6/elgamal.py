import hashlib
import random
import math

hashed_message = '3469f9e6704ea4e5373dbbe60d96eea2291a613ff65a59f348da054ba12a53f7'
hash_bytes = bytes.fromhex(hashed_message)
print("Hashed message:", hashed_message, "\n")

p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
g = 2

a = random.randint(1, p - 2)

b = pow(g, a, p)

while True:
    k = random.randint(1, p - 2)
    gcd_value = math.gcd(k, p - 1)
    hashed = int.from_bytes(hash_bytes, byteorder='big')  # Convert to integer

    if gcd_value == 1:
        r = pow(g, k, p)
        s = (pow(k, -1, p - 1) * (hashed - a * r)) % (p - 1)
        signature = (r, s)
        print("Signature:", signature, "\n")

        received_signature = signature
        r_received, s_received = received_signature

        v1 = (pow(b, r_received, p) * pow(r_received, s_received, p)) % p
        v2 = pow(g, hashed, p)  # Use the hashed integer
        verification = (v1 == v2)

        print("Signature Verification:", verification)
        break
