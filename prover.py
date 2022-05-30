"""A program to be used by a prover.

A prover is someone who wants to prove that they know the secret,
without disclosing the very secret.
"""

import rsa


def generate_proof(pk: tuple, x: int, w: int):
    """Generate a proof that the prover knows a witness ::w
    and that ::w can be trusted.
    
    ::pk = prover's_key
    ::x = some public key [zip code]
    ::w = private_witness [the id generated during registration] / provided during registration
    """
    
    m = int(w)*int(x)
    proof = rsa.encrypt(pk, m)
    return proof


    
print(generate_proof((445, 767), input('Enter zip code: '), input("Enter voter's number: ")))

# prover's key: (445, 767)