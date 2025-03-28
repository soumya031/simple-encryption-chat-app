# Python Module for Encryption and Decryption by RSA Algorithm

import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_keypair(bits=16):
    """ Generate public and private keys """

    def generate_prime():
        while True:
            num = random.randint(2 ** (bits - 1), 2 ** bits - 1)
            if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
                return num

    p = generate_prime()
    q = generate_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # Standard RSA public exponent
    while gcd(e, phi) != 1:
        e = random.randint(2, phi)

    d = pow(e, -1, phi)
    return ((e, n), (d, n))  # (Public Key, Private Key)


def encrypt(message, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher


def decrypt(ciphertext, private_key):
    d, n = private_key
    message = ''.join(chr(pow(char, d, n)) for char in ciphertext)
    return message
