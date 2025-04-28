from des_text import encrypt_text, decrypt_text

message = "zakariaa el jabiry"
key = "MYKEYDES"

# Chiffrement
chiffre = encrypt_text(message, key)
print("Message chiffré:", chiffre)

# Déchiffrement
clair = decrypt_text(chiffre, key)
print("Message déchiffré:", clair)