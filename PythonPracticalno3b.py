from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
private_key = key
public_key = key.public_key()
data_to_encrypt = b'This is a top secret RSA message'

print (f"Original Data: {data_to_encrypt.decode()}")

cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted_data = cipher_rsa.encrypt(data_to_encrypt)
print (f"Encrypted Data looks like this: {encrypted_data}")

decrypt_rsa = PKCS1_OAEP.new(private_key)
decrypted_data = decrypt_rsa.decrypt(encrypted_data)
print (f"Decrypted Data: {decrypted_data.decode()}")

assert data_to_encrypt == decrypted_data
print("Success! The message was encrypted and decrypted correctly.")
