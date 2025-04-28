from encrypt_DES import feistel_round  # Réutilisation de la même fonction
from permutation_tables import permute, IP, IP_INV
from generate_subkey import generate_subkeys


def des_decrypt(block, key):
    subkeys = generate_subkeys(key)[::-1]
    block = permute(block, IP)
    left, right = block[:32], block[32:]

    for subkey in subkeys:
        left, right = feistel_round(left, right, subkey)

    return permute(right + left, IP_INV)