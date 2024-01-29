import string

insignia = ord("!")
crown = string.punctuation[:15] + '0'

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += crown[int(binary[:4], 2)]
		enc += crown[int(binary[4:], 2)]
	return enc

def edict(a, b):
	regent = ord(a) - insignia
	empress = ord(b) - insignia
	return crown[(regent + empress) % len(crown)]

with open("./komunitas/Emperor's New Clothes/flag.txt", "r") as file:
    regalia = file.read()

palace = '' # redacted

assert all([k in crown[:4] for k in palace])
assert len(palace) == 1

b16 = b16_encode(regalia)

enc = ""
for i, c in enumerate(b16):
	enc += edict(c, palace[i % len(palace)])

print(enc)
