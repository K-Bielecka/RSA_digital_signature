from math import gcd
from hashlib import sha512


def is_prime(n, k):
    """
    The function implements the Miller-Rabin primality test.

    Input:
    n - the number to be tested
    k - number of tests to be performed

    Output: a boolean value
    """
    pass


def generate_prime_number():
    """
    Generates large prime numbers.

    Output: p - a large prime number.
    """
    pass


def extended_euclides(a, b):
    """
    Computes greatest common divisor and the coefficients of Bézout's identity.

    Input: a, b - integers of which greatest common divisor is calculated.

    Output: gcd  - greatest common divisor
            x, y - the coefficients of Bézout's identity.
    """
    pass


def generate_keys():
    """
    Generates RSA public and private keys.

    Output: (n, e) - public key
                 d - private key.
    """
    pass


def generate_signature(m, d):
    """
    The function generates an RSA digital signature.

    Input:
    m - message
    d - private key of sender

    Output:
    a digital signature s

    """
    pass


def verify(n, e, s):
    """
    The function generates verifies the received signature using public key.

    Input:
    (n,e) - public key of sender
    s - digital signature

    Output:
    a boolean value

    """
    pass
