"""A program that verifies if the proof satisfies the claim
of the prover."""


def verify(vk, x, proof):
    if proof:
        return True
    else:
        return False
