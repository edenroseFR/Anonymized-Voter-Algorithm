"""A program that verifies if the claimant is indeed registered in the system"""


import rsa
import hashlib
from merkle_tree import get_leaf

def verify_registration(x, proof, vk=(61, 767)):
    """verify() -> bool
    
    Returns TRUE if the claimant is indeed a registred_voter.
    FALSE, otherwise.
    """
    
    decrypted = rsa.decrypt(vk, proof)
    pos = int(decrypted)//int(x)
    x = hashlib.sha256(proof.encode('utf-8')).hexdigest()
    if x == get_leaf(pos):
        return True
    else:
        return False
    
    
def verify_casting():
    """verify_casting() -> bool/string
    
    Returns TRUE if the claimant already casted a vote.
    Otherwise, check if he really is a registered_voter. 
        If he is, return TRUE. 
            FALSE, otherwise.
    
    ---------------
    TRUE : The claimant already casted a vote.
    FALSE : The claimant is a registred voter but haven't casted his vote.
    'Not a voter' : The claimant is not a registred voter, so automatically, he can't cast a vote.
    """
    
    


# verifier's_key: (61, 767)
if __name__ == '__main__':
    print(verify_registration(x=8304, proof=input("Enter proof: ")))