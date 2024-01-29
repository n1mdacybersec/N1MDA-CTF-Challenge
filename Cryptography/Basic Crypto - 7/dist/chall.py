import string
from random import randint

chars = string.ascii_letters
for i in range(10):
    chars+=str(i)
    
chars+= '_{}'

print(len(chars))
flag = "redacted"

result = []
for char in flag:
    index = chars.index(char)
    index = index + (randint(1,9) * 67)
    
    result.append(index)
    
print(result)