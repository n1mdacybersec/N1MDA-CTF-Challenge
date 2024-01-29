# Nine Bites

## Author
Dhuma Aziza Altarin - rchmdnt

## Deskripsi
Diane sent me the flag, but its encrypted!
I heard them yell something about nine bites...but I don’t understand what they mean!

The ciphertext: `f1okgYH^k<tvneQCs~8wLPVV})^|Ez[{`

Can you decrypt the flag?

## Step
Player harus melakukan decrypt terhadap ciphertext yang telah ada. Di deskripsi telah tersirat `nine bites` yang artinya adalah `nine bytes`, berarti flag diencode menggunakan XOR. Tetapi kita tidak diberitahu keynya apa, setelah ditelaah keynya adalah 9 byte pertama dari flag, yaitu `n1mdaCTF{`. Yang mana key tersebut harus dilakukan XOR dengan 9 bit hex kembali. Setelah itu dilakukan XOR kembali antara ciphertext dengan key tersebut, dan didapatkan flagnya.

## Resource
Terdapat file [Decrypt](../source/decrypt.py) untuk fungsi decrypt. Run file tersebut menggunakan command di bawah ini untuk mendapatkan flagnya.
``` shell
# Run decrypt.py
python decrypt.py # Untuk Windows
python3 decrypt.py # Untuk Linux
```

Bisa juga player menggunakan Cyberchef untuk melakukan decode.

## Flag
### n1mdaCTF{4ttacK_kn0wN_PLa1NtExT}