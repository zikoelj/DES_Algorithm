from ascii_to_binary import text_to_binary
from binary_to_ascii import binary_to_text

def pad_text(text, block_size=8):
    """Padding PKCS#7 pour un alignement sur 64 bits"""
    pad_len = block_size - (len(text) % block_size)
    return text + chr(pad_len) * pad_len

def unpad_text(text):
    """Suppression du padding PKCS#7"""
    pad_len = ord(text[-1])
    return text[:-pad_len] if pad_len <= len(text) else text

def prepare_message(text):
    """Convertit un texte en blocs binaires de 64 bits"""
    padded = pad_text(text)
    binary = text_to_binary(padded)
    return [binary[i:i+64] for i in range(0, len(binary), 64)]

def process_ciphertext(binary):
    """Convertit le binaire en texte avec suppression du padding"""
    text = binary_to_text(binary)
    return unpad_text(text)