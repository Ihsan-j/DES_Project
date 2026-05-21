from utils import permute

PC1 = [
57,49,41,33,25,17,9,
1,58,50,42,34,26,18,
10,2,59,51,43,35,27,
19,11,3,60,52,44,36,
63,55,47,39,31,23,15,
7,62,54,46,38,30,22,
14,6,61,53,45,37,29,
21,13,5,28,20,12,4
]

PC2 = [
14,17,11,24,1,5,
3,28,15,6,21,10,
23,19,12,4,26,8,
16,7,27,20,13,2,
41,52,31,37,47,55,
30,40,51,45,33,48,
44,49,39,56,34,53,
46,42,50,36,29,32
]

SHIFT = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]


def shift_left(bits, n):
    """Left shift a bit string by n positions"""
    return bits[n:] + bits[:n]


def generate_round_keys(key):
    # Key must be 64 bits
    if len(key) != 64:
        raise ValueError(f"Key must be 64 bits, got {len(key)}")
    
    # Apply PC1 permutation (64 bits -> 56 bits)
    key = permute(key, PC1)
    
    # Split into C and D halves (28 bits each)
    c = key[:28]
    d = key[28:]
    
    round_keys = []
    
    # Generate 16 round keys
    for i in range(16):
        # Left shift C and D
        c = shift_left(c, SHIFT[i])
        d = shift_left(d, SHIFT[i])
        
        # Combine and apply PC2 permutation (56 bits -> 48 bits)
        combined = c + d
        round_key = permute(combined, PC2)
        round_keys.append(round_key)
    
    return round_keys