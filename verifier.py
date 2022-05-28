"""A program that verifies if the proof satisfies the claim
of the prover."""


import rsa
import hashlib
from merkle_tree import get_leaf

def verify(vk, x, proof):
    
    decrypted = rsa.decrypt(vk, proof)
    pos = decrypted//x
    x = hashlib.sha256(proof.encode('utf-8')).hexdigest()
    if x == get_leaf(pos):
        return 'Verified voter.'
    else:
        return 'Nonverified'

# verifier's_key: (61, 767)

print(verify((61, 767), 8304, '1-682-682-0-710'))