"""A program that verifies if the claimant is indeed registered in the system"""


import hashlib
from merkle_tree import get_leaf
from ast import literal_eval

def verify_registration(proof):
    """verify() -> bool
    
    Returns TRUE if the claimant is indeed a registred_voter.
    FALSE, otherwise.
    """


    l_proof = proof.split('-')
    proof = [l_proof[i] for i in range(1,len(l_proof))]
    proof = ''.join(proof)
    pos = literal_eval(l_proof[0])
    x = hashlib.sha256(proof.encode('utf-8')).hexdigest()
    r = get_leaf(pos)
    
    if x == r:
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
    print(verify_registration(proof=input("Enter proof: ")))
    
