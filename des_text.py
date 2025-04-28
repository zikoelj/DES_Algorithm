from text_processing import prepare_message, process_ciphertext
from encrypt_DES import des_encrypt
from decrypt_DES import des_decrypt
from ascii_to_binary import text_to_binary
from binary_to_ascii import binary_to_text


def encrypt_text(plaintext, key_text):
    """Chiffrement DES silencieux"""
    key_bin = text_to_binary(key_text.ljust(8)[:8])
    blocks = prepare_message(plaintext)
    cipher_blocks = [des_encrypt(block, key_bin) for block in blocks]
    return binary_to_text(''.join(cipher_blocks))


def decrypt_text(ciphertext, key_text):
    """Déchiffrement DES silencieux"""
    key_bin = text_to_binary(key_text.ljust(8)[:8])
    binary = text_to_binary(ciphertext)
    blocks = [binary[i:i + 64] for i in range(0, len(binary), 64)]
    plain_blocks = [des_decrypt(block, key_bin) for block in blocks]
    return process_ciphertext(''.join(plain_blocks))


# Exemple d'utilisation
if __name__ == "__main__":
    message = "Message secret important!"
    key = "Clef1234"

    # Chiffrement
    encrypted = encrypt_text(message, key)
    print("Message chiffré (brut):", encrypted)

    # Déchiffrement
    decrypted = decrypt_text(encrypted, key)
    print("Message déchiffré:", decrypted)