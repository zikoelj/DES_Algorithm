# 2. Initialisation des blocs : Q1 & Q2
from ascii_to_binary import text_to_binary
def process_text_in_64bit_blocks(text):
    # Conversion texte vers binaire
    binary = text_to_binary(text)

    # Ajout du padding bit-oriented
    original_length = len(binary)
    print(original_length)
    if original_length % 64 != 0:
        padding_needed = 64 - (original_length % 64)
        binary += '1' + '0' * (padding_needed - 1)  # Padding ISO/IEC 7816-4

    # Découpage et affichage
    print(f"Taille totale après padding : {len(binary)} bits\n")

    for i in range(0, len(binary), 64):
        block = binary[i:i + 64]
        print(f"Bloc {i // 64}: {block} ({len(block)} bits)")


# Test avec le même exemple
plain_text = "HelloWorld1234!"
process_text_in_64bit_blocks(plain_text)
