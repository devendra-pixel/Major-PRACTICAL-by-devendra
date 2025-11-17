from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'my_secret_key_16' # exactly 16 bytes
data_to_encrypt = b'Hello from modern AES!'

cipher = AES.new(key, AES.MODE_CBC)
iv = cipher.iv
encrypted_data = cipher.encrypt(pad(data_to_encrypt, AES.block_size))

print (f"Original Data: {data_to_encrypt.decode()}")
print (f"Encrypted Data looks like this: {encrypted_data}")

decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_data = unpad(decrypt_cipher.decrypt(encrypted_data), AES.block_size)

print (f"Decrypted Data: {decrypted_data.decode()}")
