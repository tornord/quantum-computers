
from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, ec, dsa

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

    else:
        print("Unknown crypto")

    return {
        "subject": cert.subject.rfc4514_string(),
        "issuer": cert.issuer.rfc4514_string(),
        "serial_number": cert.serial_number,
        "not_valid_before": cert.not_valid_before_utc.isoformat(),
        "not_valid_after": cert.not_valid_before_utc.isoformat(),
        "signature_algorithm": cert.signature_algorithm_oid._name,
        "extensions": [ext.__class__.__name__ for ext in cert.extensions],
    }

def decode_crt_file(file_path: str):
    with open(file_path, 'r') as f:
        content = f.read()

    # Split by BEGIN/END markers
    cert_blocks = content.split("-----BEGIN CERTIFICATE-----")
    
    for block in cert_blocks:
        block = block.strip()
        if not block or "-----END CERTIFICATE-----" not in block:
            continue
        
        # Reconstruct PEM format
        pem_cert = "-----BEGIN CERTIFICATE-----\n" + block
        # Load certificate
        cert = x509.load_pem_x509_certificate(pem_cert.encode(), default_backend())
        
        # Display decoded details
        print("=" * 60)
        print(f"Subject: {cert.subject}")
        print(f"Issuer: {cert.issuer}")
        print(f"Serial Number: {cert.serial_number}")
        print(f"Valid From: {cert.not_valid_before}")
        print(f"Valid Until: {cert.not_valid_after}")
        print(f"Signature Algorithm: {cert.signature_algorithm_oid}")
        parse_certificate_text_2(pem_cert)
        print("=" * 60)

# Example usage:
decode_crt_file("./data/ca-certificates.crt")
