import random

# Create a list of characters for the alphabet
alphabet = list("abcdefghijklmnopqrstuvwxyz")

# Shuffle the alphabet
random.shuffle(alphabet)

# Read the text file
with open("./komunitas/basic crypto 6/flag.txt", "r") as file:
    text = file.read()

# Create a dictionary for character mapping (original to shuffled)
char_mapping = {orig: shuffled for orig, shuffled in zip("abcdefghijklmnopqrstuvwxyz", alphabet)}

# Function to perform the substitution
def substitute(text):
    return ''.join(char_mapping.get(char, char) for char in text)

# Encrypt the text
encrypted_text = substitute(text)

# Write the encrypted text to a new file
with open("./komunitas/basic crypto 6/out.txt", "w") as file:
    file.write(encrypted_text)