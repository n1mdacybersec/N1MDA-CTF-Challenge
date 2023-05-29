# Roman Burger

## Author
Arasy Dafa Sulistya Kurniawan - omegathrone

## Deskripsi
7 roman people buy 7 exclusive original burger

## Hint
don't forget your key

## Message
r6sloMFJ|m~apf7X62XjErXo2Xmhesz

## Step
Player harus melakukan decrypt terhadap message yang telah ada. Terdapat 2 algoritma yang digunakan yaitu Caesar Cipher dengan Shift/Key 7 dan XOR dengan key 7. Player harus decrypt XOR dengan key 7 terlebih dahulu, lalu melakukan decrypt Caesar Cipher dengan Shift/Key 7 untuk mendapatkan flagnya.

## Resource
Terdapat file [Decrypt](source/decrypt.py) untuk fungsi decrypt flag dan [Encrypt](source/encrypt.py) untuk fungsi encrypt flag. Run file tersebut menggunakan command
``` shell
# Run decrypt.py
python decrypt.py # Untuk Windows
python3 decrypt.py # Untuk Linux

# Run encrypt.py
python encrypt.py # Untuk Windows
python3 encrypt.py # Untuk Linux
```

Bisa juga player menggunakan Cyberchef untuk melakukan decode.

## Flag
### n1mdaCTF{crypt0_15_fUn_a5_chum}