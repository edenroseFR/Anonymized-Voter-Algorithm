import verifier


def proof_is_valid(proof):
    if verifier.verify_registration(proof):
        return True
    else:
        return False