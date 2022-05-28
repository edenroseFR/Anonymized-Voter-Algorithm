"""Generate a merkle root out of all recorded proxies.

What this module do:
1) Retrieve proxies from a .csv file
2) Generate and return a merkle root

read about merkle_tree here: https://bit.ly/3szuTPO
watch about merkle_tree here: https://bit.ly/3Ng7vyK

"""

import merkletools
import csv


class Voters:
    PROXIES = 'proxies.csv'
    
    def get_all(self):
        return self.__all_proxies()
    
    def __all_proxies(self):
        with open(self.PROXIES) as proxies:
            # skips the heading
            next(proxies)
            
            proxy_reader = csv.reader(proxies)
            all_proxy = [row[0] for row in proxy_reader]
            return all_proxy



def main()-> None:
    voters = Voters().get_all()
    mtools.add_leaf(voters, True)
    mtools.make_tree()
    print(mtools.get_merkle_root())
    


if __name__ == '__main__':
    mtools = merkletools.MerkleTools()
    main()
