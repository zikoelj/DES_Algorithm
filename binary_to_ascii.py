# 1. Conversion texte-binaire : Q2
def binary_to_text(binary):
    text = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            character = chr(int(byte, 2))
            text += character
    return text