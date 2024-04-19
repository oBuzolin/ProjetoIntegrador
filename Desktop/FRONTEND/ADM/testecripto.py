from cryptography.fernet import Fernet


key = Fernet.generate_key()
cipher_suite = Fernet(key)
# Dados para criptografar
data = b"Seu texto secreto aqui"

# Criptografar os dados
cipher_text = cipher_suite.encrypt(data)
print("Texto Criptografado:", cipher_text)

# Descriptografar os dados
plain_text = cipher_suite.decrypt(cipher_text)
print("Texto Descriptografado:", plain_text.decode())
