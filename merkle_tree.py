"""Generate a merkle root out of all recorded proxies.

What this module do:
1) Retrieve proxies from a .csv file
2) Generate and return a merkle root

read about merkle_tree here: https://bit.ly/3szuTPO
watch about merkle_tree here: https://bit.ly/3Ng7vyK

"""

import merkletools
import pandas as pd
from csv import reader
from rsa import encrypt

class Voters:
    PROXIES = 'proxies.csv'
    pk = (445, 767)
    zcode = 8304
    
    def get_proofs(self, x=None):
        proofs = []
        if not x:
            for i in range(1, self.__voters_count()+1):
                proof = encrypt(self.pk, self.zcode*i)
                proofs.append(proof)
        else:
            proofs =  [proof in self.__render_proofs(x)]
        return proofs
    

    def __voters_count(self):
        return len(pd.read_csv(self.PROXIES))
    
    
    def __render_proofs(self, fname):
        """Return a list of proofs"""
        
        with open(fname) as file_obj:
            # Skips the heading
            next(file_obj)
            reader_obj = reader(file_obj)
            return [row for row in reader_obj]



def get_leaf(idx, prf_file=None):
    i = idx-1
    try:
        if prf_file:
            return main(prf_file).get_leaf(i)
        else:
            return main().get_leaf(i)
    except Exception as e:
        print(e)
        return False
    
    
1234-34343 == proofs[idx]
proofs = [l1, l2, l3]



def main(prf_file=None):
    global mtools
    mtools = merkletools.MerkleTools()
    proofs = Voters().get_proofs(prf_file)
    mtools.add_leaf(proofs, True)
    mtools.make_tree()
    return mtools
    

if __name__ == '__main__':
    main()
    # print(hashlib.sha256('710-757-0-264'.encode('utf-8')).hexdigest())
