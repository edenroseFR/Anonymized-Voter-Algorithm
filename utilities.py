import verifier


def proof_is_valid(zipcode, proof):
    if verifier.verify_registration(zipcode, proof):
        return True
    else:
        return False