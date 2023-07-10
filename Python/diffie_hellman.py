from secrets import randbelow
from random import randint

def private_key(p):
    return randint(2, p - 1)
    # range = p - 2
    # return 2 + randbelow(range)


def public_key(p, g, private):
    A = g ** private % p
    return A


def secret(p, public, private):
    s = public ** private % p
    return p
