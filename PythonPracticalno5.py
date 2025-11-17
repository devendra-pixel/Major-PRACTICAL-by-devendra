def RSHash (data_string):
    a = 378551
    b = 63689
    hash_value = 0
    for char in data_string:
        hash_value = hash_value * a + ord(char)
        a = a * b
    return hash_value

data = "hello world"
hash_result = RSHash(data)
print (f"Original String: {data}")
print (f"RS Hash Value: {hash_result}")

data2 = "world hello"
hash_result2 = RSHash(data2)
print (f"\nOriginal String: {data2}")
print (f"RS Hash Value: {hash_result2}")
