from feistel import feistel, xor, initial, final


def rounds(l, r, keys):
    for i in range(16):
        l, r = r, xor(l, feistel(r, keys[i]))
    return r + l


def encrypt(block, keys):
    block = initial(block)
    return final(rounds(block[:32], block[32:], keys))