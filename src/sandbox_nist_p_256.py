import os

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from ecdsa.curves import NIST256p

# https://neuromancer.sk/std/nist/P-256
# https://neuromancer.sk/std/secg/secp256r1

# Key generation for Alice and Bob
alice_private_key = ec.generate_private_key(ec.SECP256R1())
bob_private_key = ec.generate_private_key(ec.SECP256R1())

alice_public_key = alice_private_key.public_key()
bob_public_key = bob_private_key.public_key()

# Shared secret derivation
alice_shared_key = alice_private_key.exchange(ec.ECDH(), bob_public_key)
bob_shared_key = bob_private_key.exchange(ec.ECDH(), alice_public_key)

public_numbers = alice_public_key.public_numbers()
curve = public_numbers.curve
print("Curve name:", curve.name)


alice_public_bytes = alice_public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
print(alice_public_bytes.decode('utf-8'))


curve = NIST256p.curve
generator = NIST256p.generator

print("Field modulus (p):", curve.p())
print("Curve coefficient a:", curve.a())
print("Curve coefficient b:", curve.b())
print("Base point G (x):", generator.x())
print("Base point G (y):", generator.y())
print("n", NIST256p.order)


# Get the generator point G
G = NIST256p.generator

# Calculate 2 * G
double_G = G + G

print("2G x:", double_G.x())
print("2G y:", double_G.y())
# 56515219790691171413109057904011688695424810155802929973526481321309856242040, 3377031843712258259223711451491452598088675519751548567112458094635497583569


def derive_key(shared_secret):
    return HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"ecdh demo",
    ).derive(shared_secret)


# Symmetric key derivation
derived_key = derive_key(alice_shared_key)

# Encryption
plaintext = b"Hello from Alice!"
iv = os.urandom(12)

encryptor = Cipher(
    algorithms.AES(derived_key),
    modes.GCM(iv),
).encryptor()

ciphertext = encryptor.update(plaintext) + encryptor.finalize()
tag = encryptor.tag

# Decryption
decryptor = Cipher(
    algorithms.AES(derived_key),
    modes.GCM(iv, tag),
).decryptor()

decrypted = decryptor.update(ciphertext) + decryptor.finalize()

print("Ciphertext:", ciphertext.hex())
print("IV:", iv.hex())
print("Tag:", tag.hex())
print("Decrypted:", str(decrypted))
