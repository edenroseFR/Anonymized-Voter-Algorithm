"""Use this module to register a voter.

What this module will do
1) Ask for a voter's ID [NatlID, StudentID, ...].
2) Generate voter's proxy base on step 1.
3) Record the voter's proxy.
4) Give the proxy to the registrant.
"""


import hashlib
from csv import writer
from datetime import datetime
import pandas as pd


def get_voters_proxy(vID):
    x = hashlib.sha256(vID.encode('utf-8')).hexdigest()[:10]
    return x[:3] + '-' + x[3:6] + '-' + x[6:]


def get_number():
    return len(pd.read_csv(PROXIES))


def add_to_db(proxy):
    registration_date = datetime.today().strftime('%m-%d-%Y %H:%M:%S')
    
    with open(PROXIES, 'a', newline='') as db:
        proxy_writer = writer(db)
        proxy_writer.writerow([proxy, registration_date])
        db.close()
    return


def success_msg(proxy):
    print('Registration succesful!')
    
    print('************************', end='\n\n')
    print('**START OF CREDENTIALS**')
    print('Your proxy: ' + proxy)
    print('You are voter number: ' + str(get_number()))
    print('***END OF CREDENTIALS***', end='\n\n')
    
    print('Note: To keep you anonymous, keep your credentials secret.')


def main():
    vID = input('Enter ID: ')
    proxy = get_voters_proxy(vID)
    add_to_db(proxy)
    success_msg(proxy)
    


if __name__ == '__main__':
    PROXIES = 'proxies.csv'
    main()
