# Basic math for discrete cyclic group elliptic curve
# y^2 = x^3 + ax + b over GF(p)


def mod_inv(x, p):
    # Extended Euclidean Algorithm to find modular inverse
    lm, hm = 1, 0
    low, high = x % p, p
    while low > 1:
        r = high // low
        nm, new = hm - lm * r, high - low * r
        lm, low, hm, high = nm, new, lm, low
    return lm % p


class EllipticCurve:
    def __init__(self, a, b, p, G, n):
        self.a = a
        self.b = b
        self.p = p
        self.G = G
        self.n = n

    def add(self, P, Q):
        if P == (None, None):
            return Q
        if Q == (None, None):
            return P

        x_P, y_P = P
        x_Q, y_Q = Q
        if P != Q:
            if x_P == x_Q:
                return (None, None)
            s = (y_P - y_Q) * mod_inv(x_P - x_Q, self.p) % self.p
        else:
            s = (3 * x_P**2 + self.a) * mod_inv(2 * y_P, self.p) % self.p

        x_R = (s * s - (x_P + x_Q)) % self.p
        y_R = (s * (x_P - x_R) - y_P) % self.p

        return (x_R, y_R)

    def mult(self, k, P):
        R = (None, None)
        A = P

        while k:
            if k & 1:
                R = self.add(R, A) if R else A
            A = self.add(A, A)
            k >>= 1

        return R
