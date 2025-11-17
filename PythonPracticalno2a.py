import pyDes

key = b"mysecret"
data_to_encrypt = b"Hello from DES!"
cipher = pyDes.des(key, padmode = pyDes.PAD_PKCS5)

encrypted_data = cipher.encrypt(data_to_encrypt)
print (f"Original Data: {data_to_encrypt.decode()}")
print (f"Encrypted Data Looks like this: {encrypted_data}")

decrypted_data = cipher.decrypt(encrypted_data)
print (f"Decrypted Data: {decrypted_data.decode()}")
