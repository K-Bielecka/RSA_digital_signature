from math import gcd
from hashlib import sha512
from random import randrange


def is_prime(n: int, k: int) -> bool:
    """
    The function implements the Miller-Rabin primality test.

    Input:
    n - the number to be tested
    k - number of tests to be performed

    Output: a boolean value
    """

    # trivial cases: 0-2 and even numbers
    if n == 2:
        return True
    elif n <= 1 or n % 2 == 0:
        return False

    # writing n as 2^r * d + 1 with d odd
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    # perform k number of tests
    for _ in range(k):
        a = randrange(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def generate_prime_number() -> int:
    """
    Generates large prime numbers.

    Output: p - a large prime number.
    """

    p = 0

    # choose randomly a large number until prime is obtained
    while not is_prime(p, 180):
        p = randrange(1000, 3000)

    return p


def extended_euclidean(a: int, b: int) -> (int, int, int):
    """
    Computes greatest common divisor and the coefficients of Bézout's identity.

    Input: a, b - non-negative integers satisfying a >= b.

    Output: gcd  - greatest common divisor
            x, y - the coefficients of Bézout's identity.
    """

    if b == 0:
        return (a, 1, 0)

    x1, x2, y1, y2 = 0, 1, 1, 0
    while b > 0:
        q, r = divmod(a, b)
        x = x2 - q * x1
        y = y2 - q * y1

        a, b, x2, x1, y2, y1 = b, r, x1, x, y1, y

    gcd, x, y = a, x2, y2
    return (gcd, x, y)


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
