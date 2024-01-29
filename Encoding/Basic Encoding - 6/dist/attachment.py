emojis = [n for n in "🌸🍔🐳🚀🌞🎉🍦🎈🐶🍕🌺🎸⚡️🦋🌼🎁"]
                      
m = open("./Encoding/basic_6/flag.txt", "rb").read().hex()

print(m)

for e, c in zip(emojis, "0123456789abcdef"):
  m = m.replace(c, e)

print(m)