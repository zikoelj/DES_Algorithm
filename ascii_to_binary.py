# 1. Conversion texte-binaire : Q1
def text_to_binary(text):
    binary = ''
    for character in text:
        binary_character = bin(ord(character))[2:].zfill(8)
        binary += binary_character
    return binary