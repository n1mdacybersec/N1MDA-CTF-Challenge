import random


def caesar_encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.islower():
            shifted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif char.isupper():
            shifted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            shifted_char = char
        ciphertext += shifted_char
    return ciphertext


def xor_encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        ciphertext += chr(ord(plaintext[i]) ^ key)
    return ciphertext


flag = "n1mdaCTF{crypt0_15_fUn_a5_chum}"
caesar_key = 7
xor_key = 7

encrypted_flag = xor_encrypt(caesar_encrypt(flag, caesar_key), xor_key)

print("Encrypted flag:", encrypted_flag)
