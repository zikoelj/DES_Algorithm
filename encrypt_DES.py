from permutation_tables import permute, IP, IP_INV, E, P
from S_Boxes import S_BOXES
from generate_subkey import generate_subkeys


def feistel_round(left, right, subkey):
    expanded = permute(right, E)
    xored = bin(int(expanded, 2) ^ int(subkey, 2))[2:].zfill(48)
    sbox_out = ''.join(
        format(S_BOXES[i][int(xored[i * 6] + xored[i * 6 + 5], 2)][int(xored[i * 6 + 1:i * 6 + 5], 2)], '04b')
        for i in range(8)
    )
    p_out = permute(sbox_out, P)
    new_right = bin(int(left, 2) ^ int(p_out, 2))[2:].zfill(32)
    return right, new_right


def des_encrypt(block, key):
    subkeys = generate_subkeys(key)
    block = permute(block, IP)
    left, right = block[:32], block[32:]

    for subkey in subkeys:
        left, right = feistel_round(left, right, subkey)

    return permute(right + left, IP_INV)