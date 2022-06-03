"""A program to be used by a prover.

A prover is someone who wants to prove that he is a voter,
without disclosing his proxy/shadow identity.
"""

import rsa
from hashlib import sha256
import getpass


def generate_proof(pk: tuple, x: int, w: int):
    """Generate a proof that the prover knows a witness ::w,
    and that ::w can be trusted.
    
    ::pk = prover's_key
    ::x = shadow-public [proxy]
    ::w = shadow-private [unique id generated during registration]
    """
    w = rsa.decrypt(pk, w)
    x = sha256(x.encode('utf-8')).hexdigest()[:20]
    proof = hex(int(w)) + '-' + x[:5] + '-' + x[5:10] + '-' + x[10:15] + '-' + x[15:]
    return proof


    
print(generate_proof(
        (445, 767), 
        input('Enter proxy: '), 
        input("Enter voter's number: ")
))


# prover's key: (445, 767)