from permutation_tables import permute, PC1, PC2

# Table de décalage pour chaque tour om fait soit 1 ou 2 décalage(s)
gestion_dec = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


def left_shift(digits, m):
    """Décalage circulaire à gauche"""
    return digits[m:] + digits[:m]


def generate_subkeys(principle_key):
    """Génère les 16 sous-clés de 48 digits"""
    # Utilisation de la fonction permute importée
    key_pc1 = permute(principle_key, PC1)

    left, right = key_pc1[:28], key_pc1[28:]  # Séparation

    subkeys = []
    for tour_num in range(16):
        shift = gestion_dec[tour_num]
        left = left_shift(left, shift)
        right = left_shift(right, shift)

        # Utilisation de PC2 importé
        subkey = permute(left + right, PC2)
        subkeys.append(subkey)

    return subkeys


# Exemple d'utilisation
if __name__ == "__main__":
    # Clé d'exemple (doit avoir 64 digits)
    principle_key = "0001001100110100010101110111100110011011101111001101111111110001"

    subkeys = generate_subkeys(principle_key)
    for i, key in enumerate(subkeys, 1):
        print(f"Sous-clé {i:2d}: {key}")