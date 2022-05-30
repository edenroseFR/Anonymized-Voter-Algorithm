"""Use this module to register a voter.

What this module will do
1) Ask for a voter's ID [NatlID, StudentID, ...].
2) Generate voter's proxy base on step 1.
3) Record the voter's proxy.
4) Give the proxy to the registrant.

OUTPUT -> voter's_proxy , witness
"""


import hashlib
from csv import writer
from datetime import datetime, date
import pandas as pd
from rsa import encrypt


def get_voters_proxy(vID):
    x = hashlib.sha256(vID.encode('utf-8')).hexdigest()[:10]
    return x[:3] + '-' + x[3:6] + '-' + x[6:]


"""
password123 ==hash===> 234dSEawdwe

234dSEawdwe ==> password12

"""


def get_number():
    pk =  (445, 767)
    
    v_num = len(pd.read_csv(PROXIES))
    return v_num


def record_vID(vID):
    reg_year = date.today().year
    
    with open('registered_IDs.csv', 'a', newline='') as db:
        vID_writer = writer(db)
        vID_writer.writerow([vID, reg_year])
        db.close()
    return
    

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


def valid(vID):
    return True

def main():
    vID = input('Enter ID: ')
    if valid(vID): # TODO
        proxy = get_voters_proxy(vID)
        add_to_db(proxy)
        record_vID(vID)
        success_msg(proxy)
    else:
        print("""
              
        """)
    


if __name__ == '__main__':
    PROXIES = 'proxies.csv'
    main()
