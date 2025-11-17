import string

def caesar_cipher(input_str):
    ENCRYPT_SHIFT = 3
    DECRYPT_SHIFT = -3

    cipher_str = ""
    plain_str = ""
    
    
    for char in input_str:
        if char in string.ascii_lowercase:
            i = string.ascii_lowercase.index(char)
            new_i = (i + ENCRYPT_SHIFT) % 26
            cipher_str += string.ascii_lowercase[new_i]
            
        elif char in string.ascii_uppercase:
            i = string.ascii_uppercase.index(char)
            new_i = (i + ENCRYPT_SHIFT) % 26
            cipher_str += string.ascii_uppercase[new_i]
            
        else:
                   cipher_str += char

    print(f"Encrypted (Cipher Text) :\t{cipher_str}")

    for char in cipher_str:
        if char in string.ascii_lowercase:
           
            i = string.ascii_lowercase.index(char)
            new_i = (i + DECRYPT_SHIFT + 26) % 26 
            plain_str += string.ascii_lowercase[new_i]
            
        elif char in string.ascii_uppercase:
            i = string.ascii_uppercase.index(char)
            new_i = (i + DECRYPT_SHIFT + 26) % 26
            plain_str += string.ascii_uppercase[new_i]
            
        else:
            plain_str += char

    print(f"Decrypted (Plain Text) :\t{plain_str}")

print("Enter a String :", end="\t")
user_input = input()

caesar_cipher(user_input)
