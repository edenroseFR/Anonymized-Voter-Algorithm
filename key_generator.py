def gen_key(p, q):
    """gen_key(p,q) -> tuple(tuple1, tuple2)
    
    tuple1 = prover_key
    tuple2 = verifier_key
    
    The keys should only be generated ONCE.
    To keep the voters anonymous, no one should know the value of p and q.
    """
    
    n = p*q
    phi_n = (p-1)*(q-1)
    e = ea_gcd(p, q)
    d = eea_gcd(e, phi_n)

    return ((d, n), (e, n))


def ea_gcd(a, b):
    e = max(a, b)+1
    end = (a-1)*(b-1)
    while e < end:
        phi_n = (a-1)*(b-1)
        max_p = e
        while phi_n != 0:
            max_p, phi_n = phi_n, max_p % phi_n
        if max_p == 1:
            return e
        e += 1


def eea_gcd(a, b):
    d = 3
    while True:
        if (a * d) % b == 1:
            return d
        d += 1
        
        
# primes = 7, 13

if __name__ == '__main__':
    pk,vk = gen_key(59,13)
    
    print("prover's key: " + str(pk))
    print("verifier's_key: " + str(vk))
    
    
# prover's key: (445, 767)
# verifier's_key: (61, 767)