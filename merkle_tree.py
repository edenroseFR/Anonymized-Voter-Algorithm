"""Generate a merkle root out of all recorded proxies.

What this module do:
1) Retrieve proxies from a .csv file
2) Generate and return a merkle root

read about merkle_tree here: https://bit.ly/3szuTPO
watch about merkle_tree here: https://bit.ly/3Ng7vyK

"""

import merkletools
import pandas as pd
from rsa import encrypt

class Voters:
    PROXIES = 'proxies.csv'
    pk = (445, 767)
    zcode = 8304
    
    def get_proofs(self):
        proofs = []
        for i in range(1, self.__count()+1):
            proof = encrypt(self.pk, self.zcode*i)
            proofs.append(proof)

        return proofs
    

    def __count(self):
        return len(pd.read_csv(self.PROXIES))
        


def get_leaf(idx):
    i = idx-1
    try:
        return main().get_leaf(i)
    except:
        return False


def main():
    global mtools
    mtools = merkletools.MerkleTools()
    proofs = Voters().get_proofs()
    mtools.add_leaf(proofs, True)
    mtools.make_tree()
    return mtools
    

if __name__ == '__main__':
    import hashlib
    main()
    # print(hashlib.sha256('710-757-0-264'.encode('utf-8')).hexdigest())
