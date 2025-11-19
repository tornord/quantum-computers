from math import gcd

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from sympy import factorint, nextprime

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a


def mod_inverse(e, phi):
    # Extended Euclidean Algorithm
    def extended_gcd(a, b):
        if b == 0:
            return (1, 0)
        else:
            x1, y1 = extended_gcd(b, a % b)
            x, y = y1, x1 - (a // b) * y1
            return (x, y)

    x, _ = extended_gcd(e, phi)
    return x % phi


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Step 1: Choose primes
q = 5 #nextprime(210)
r = 11 #nextprime(390)
assert is_prime(q) and is_prime(r)

# Step  Compute n and phi(n)
n = q * r
phi = (q - 1) * (r - 1)

# Step 3: Choose e such that 1 < e < phi and gcd(e, phi) = 1


def prime_factors_sympy(n):
    factors = factorint(n)
    return [p for p, exp in factors.items() for _ in range(exp)]


print(prime_factors_sympy(phi))

e = 13
assert gcd(e, phi) == 1
assert pow(e, phi // 2, n) == 1

# Step 4: Compute d (modular inverse of e mod phi)
d = mod_inverse(e, phi)


def find_p(g, N, m=1):
    for i in range(2, N, 2):
        if pow(g, i, N) == m:
            return i
    return -1


# Encrypt and decrypt a message
message = 7
ciphertext = pow(message, e, n)
decrypted = pow(ciphertext, d, n)

print(f"Public key: (e={e}, n={n})")
print(f"Private key: (d={d}, n={n})")
print(f"Original message: {message}")
print(f"Encrypted message: {ciphertext}")
print(f"Descrypted message: {decrypted}")


# Crack the public key
g = 17 #e
p = find_p(g, n, 1)
gp2 = pow(g, p // 2, n)
res = (gcd(gp2 + 1, n), gcd(gp2 - 1, n))
print("q =", res[0], ", r =", res[1])

# Generate RSA key pair (2048 bits)
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
private_numbers = private_key.private_numbers()
print("Private exponent (d):", private_numbers.d)

public_key = private_key.public_key()

# Message to encrypt (e.g., 0 as a byte)
m = 123
message = (m).to_bytes(1, byteorder="big")  # Convert integer 0 to bytes

# Encrypt with OAEP padding
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

# Decrypt
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    ),
)

# Convert decrypted bytes back to integer
decrypted_number = int.from_bytes(plaintext, byteorder="big")

print(f"Original message: {m}")
print(f"Encrypted (hex): {ciphertext.hex()}")
print(f"Decrypted message: {decrypted_number}")
