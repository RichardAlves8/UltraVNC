from Crypto.Cipher import DES
from binascii import unhexlify

#ultravnc.ini 
hex_password = "75D4CFEE7A1BF08914"

# Remover o "00" do final
ciphertext = unhexlify(hex_password[:-2])

# Chave DES retirado do código fonte da aplicação
key = bytes([0xE8, 0x4A, 0xD6, 0x60, 0xC4, 0x72, 0x1A, 0xE0])

# Inicializa o objeto DES no modo ECB
des = DES.new(key, DES.MODE_ECB)

# Descriptografa
decrypted = des.decrypt(ciphertext)

# Remove padding zero
decrypted_text = decrypted.rstrip(b"\x00").decode("ascii", errors="ignore")
print("Senha descriptografada:", decrypted_text)