from math import gcd
import subprocess
import re
from typing import Optional
import ssl
import socket

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, ec, dsa
from sympy import nextprime


def fetch_certificates(domain: str, port: int = 443) -> list[str]:
    cmd = ["openssl", "s_client", "-connect", f"{domain}:{port}", "-showcerts"]

    try:
        result = subprocess.run(
            cmd, input="", capture_output=True, text=True, timeout=10
        )
    except subprocess.SubprocessError as e:
        raise RuntimeError(f"Failed to run openssl: {e}")

    output = result.stdout
    certs = re.findall(
        r"-----BEGIN CERTIFICATE-----.*?-----END CERTIFICATE-----", output, re.DOTALL
    )

    return certs


def parse_certificate_text(cert_str: str) -> Optional[str]:
    try:
        result = subprocess.run(
            ["openssl", "x509", "-text", "-noout"],
            input=cert_str,
            capture_output=True,
            text=True,
            timeout=5,
        )

        if result.returncode != 0:
            raise RuntimeError(f"OpenSSL error: {result.stderr.strip()}")

        return result.stdout

    except Exception as e:
        raise RuntimeError(f"Failed to parse certificate: {e}")


def parse_certificate_text_2(cert_str: str) -> dict:
    cert_bytes = cert_str.encode("utf-8")
    cert = x509.load_pem_x509_certificate(cert_bytes, default_backend())
    public_key = cert.public_key()

    print(f"Key size {public_key.key_size}")
    if isinstance(public_key, rsa.RSAPublicKey):
        numbers = public_key.public_numbers()
        print("RSA Public Key")
        print("Modulus (n):", numbers.n)
        print("Exponent (e):", numbers.e)

    elif isinstance(public_key, ec.EllipticCurvePublicKey):
        numbers = public_key.public_numbers()
        curve = public_key.curve.name
        print("Elliptic Curve Public Key")
        print("Curve:", curve)
        print("X:", numbers.x)
        print("Y:", numbers.y)

    elif isinstance(public_key, dsa.DSAPublicKey):
        numbers = public_key.public_numbers()
        print("DSA Public Key")
        print("Y:", numbers.y)
        print("Parameter p:", numbers.parameter_numbers.p)
        print("Parameter q:", numbers.parameter_numbers.q)
        print("Parameter g:", numbers.parameter_numbers.g)

    return {
        "subject": cert.subject.rfc4514_string(),
        "issuer": cert.issuer.rfc4514_string(),
        "serial_number": cert.serial_number,
        "not_valid_before": cert.not_valid_before_utc.isoformat(),
        "not_valid_after": cert.not_valid_before_utc.isoformat(),
        "signature_algorithm": cert.signature_algorithm_oid._name,
        "extensions": [ext.__class__.__name__ for ext in cert.extensions],
    }


def get_peer_certificates(host: str, port: int = 443) -> list[x509.Certificate]:
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)
    conn.connect((host, port))

    der_cert = conn.getpeercert(binary_form=True)
    cert = x509.load_der_x509_certificate(der_cert, default_backend())

    # Note: Python's ssl module does not expose the full chain by default.
    # You only get the leaf certificate here.
    return [cert]


def get_leaf_certificate(host: str, port: int = 443) -> str:
    context = ssl.create_default_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            der_cert = ssock.getpeercert(binary_form=True)
            pem_cert = ssl.DER_cert_to_PEM_cert(der_cert)
            return pem_cert


def get_leaf_certificate_unverified(host: str, port: int = 443) -> str:
    context = ssl._create_unverified_context()
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            der_cert = ssock.getpeercert(binary_form=True)
            return ssl.DER_cert_to_PEM_cert(der_cert)


def generate_toy_rsa_key(bits=16):
    # Generate two small primes
    p = nextprime(2 ** (bits // 2 - 1))
    q = nextprime(p + 1)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e
    e = 3
    while gcd(e, phi) != 1:
        e += 2

    # Compute d
    d = pow(e, -1, phi)

    return {"public_key": (e, n), "private_key": (d, n), "p": p, "q": q}


if __name__ == "__main__":

    # num = 97564666338969382484959738239287093658639323601456735454100666918150406305139
    # hex_value = hex(num)
    # print(hex_value)


    # rsa_keys = generate_toy_rsa_key(bits=16)
    # print(rsa_keys)

    # with open("dev.crt", "rb") as f:
    #     cert_data = f.read()

    # # Parse the certificate
    # cert = x509.load_pem_x509_certificate(cert_data, default_backend())
    # public_key = cert.public_key()

    domain = "svk.se"
    x = get_leaf_certificate_unverified(domain)
    # x = get_peer_certificates(domain)
    # certificates = fetch_certificates(domain)
    p = parse_certificate_text_2(x)
    print(p)
    # for i, cert in enumerate(certificates, 1):
    #     print(f"Certificate {i}:\n{cert}\n")
