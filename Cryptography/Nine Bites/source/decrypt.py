def xor_decrypt(ciphertext, key):
    decrypted = []
    for i in range(len(ciphertext)):
        decrypted.append(chr(ord(ciphertext[i]) ^ ord(key[i % len(key)])))
    return ''.join(decrypted)

ciphertext = "f1okgYH^k<tvneQCs~8wLPVV})^|Ez[{"
known_plaintext = "n1mdaCTF{"
key = []
for i in range(len(known_plaintext)):
    key.append(chr(ord(ciphertext[i]) ^ ord(known_plaintext[i])))

decrypted_flag = xor_decrypt(ciphertext, ''.join(key))
print(decrypted_flag)
