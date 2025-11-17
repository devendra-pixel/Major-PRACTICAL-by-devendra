import hashlib

data = "Hello, this is a test string"
md5_hash_object = hashlib.md5(data.encode())
hex_digest = md5_hash_object.hexdigest()

print (f"Original String : {data}")
print (f"MD5 Hash: {hex_digest}")
