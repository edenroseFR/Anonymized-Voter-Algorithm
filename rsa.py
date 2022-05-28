def encrypt(k, n):
    i, N = k
    def expmod(base, exp, n):
        bin_exp = bin(exp)[2:][::-1]
        val = 1
        for idx in range(len(bin_exp)):
            if idx > 0:
                base **= 2
            if bin_exp[idx] == '1':
                val = val*base % n
        return str(val)

    encrypted = [expmod(int(c), i, N) for c in list(str(n))]
    return '-'.join(encrypted)



