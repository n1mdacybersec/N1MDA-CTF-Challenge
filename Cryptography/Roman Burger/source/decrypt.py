def xor_decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        plaintext += chr(ord(ciphertext[i]) ^ key)
    return plaintext


def caesar_decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.islower():
            shifted_char = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        elif char.isupper():
            shifted_char = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        else:
            shifted_char = char
        plaintext += shifted_char
    return plaintext


encrypted_flag = "r6sloMFJ|m~apf7X62XjErXo2Xmhesz"
caesar_key = 7
xor_key = 7

decrypted_flag = caesar_decrypt(
    xor_decrypt(encrypted_flag, xor_key), caesar_key)

print("Decrypted flag:", decrypted_flag)
