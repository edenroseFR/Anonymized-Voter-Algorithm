import sys
import csv
import getpass
from utilities import proof_is_valid


def display_message(state=None):
    footnote = "If you think that this is a mistake, please approach John Doe."
    
    if state == 'success':
        print(f"""
              Result for proxy: {v_proxy}
              Your vote for {vote} is successfully recorded.
              
              {footnote}
        """)
    elif state == 'failed':
        print("""
              Sorry, you are not eligible to vote. Our system could not recognize you.
              {footnote}
        """)
    elif state == 'already_voted':
        print(f"""
              You already casted your vote.
              {footnote}
        """)
    elif state == 'unrecognized_proxy':
        print(f"""
              Sorry, the proxy {v_proxy} doesn't exist in the system.
              {footnote}
        """)
        
    return None


def record_vote():
    with open('votes.csv', 'a', newline='\n') as db:
        vote_writer = csv.writer(db)
        vote_writer.writerow([v_proxy, vote])
        db.close()
    return None

    
def v_proxy_exist(p):
    """v_proxy_exist() -> bool
    
    Check if proxy ::p exist in proxies.csv
    """
    
    with open('proxies.csv') as file_obj:
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            if row[0] == p:
                return True
        return False
    

def show_candidates():
    """show_candidates() -> None
    
    Display candidates to choose from.
    """
    print('''
          Choose your color:
            > Yellow
            > Blue
            > Red
    ''')
    return


def no_vote_record():
    """no_vote_record() -> bool
    
    Open 'votes.csv' and check whether proof ::p is already in it.
    If ::p is already in the 'votes.csv', it means that he already casted his vote.
    This function assume that proof ::p is already verified.
    
    Returns TRUE if the voter's proxy proof ::p is already in the 'votes.csv''.
    FALSE, otherwise.
    
    PARAMETERS
    ------------------
    ::p : voter's proof of registration
    
    """

    with open('votes.csv') as file_obj:
        reader_obj = csv.reader(file_obj)
        for row in reader_obj:
            if row[0] == v_proxy:
                return False
        return True


def cast_vote():
    global v_proxy
    global vote 
    
    v_proxy = getpass.getpass("Enter proxy: ")
    if v_proxy_exist(v_proxy):
        if no_vote_record():
            show_candidates()
            vote = input("Your vote: ")
            return vote
        else:
            display_message('already_voted')
            sys.exit()
    else:
        display_message('unrecognized_proxy')
        sys.exit()


def verified_voter():
    z = input("Enter zip code: ")
    v_proof = input("Enter a proof that you are a registered voter: ")
    print("Verifying...")
    if proof_is_valid(z, v_proof):
        print("Proof verified.")
        return True
    else:
        return False


def main():
    if verified_voter():
        cast_vote()
        record_vote()
        display_message('success')
    else:
        display_message('failed')
        sys.exit()



if __name__ == '__main__':
    main()
    