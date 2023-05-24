# hide

## Deskripsi
im good at hiding

## Hint
why don't you just look inside?

## Message
Diberikan suatu file binary [Binary](challenge/hide)

## Step
Player harus melakukan decrypt terhadap message yang telah ada. Terdapat 2 algoritma yang digunakan yaitu Caesar Cipher dengan Shift/Key 7 dan XOR dengan key 7. Player harus decrypt XOR dengan key 7 terlebih dahulu, lalu melakukan decrypt Caesar Cipher dengan Shift/Key 7 untuk mendapatkan flagnya.

## Resource
Terdapat file [Hide](source/hide.c) untuk menyembunyikan flag ke dalam binary. Untuk generate binary menggunakan command 
```shell
gcc hide.c -o challenge/hide
```

## Flag
### n1mdaCTF{f14gs_h4rdc0d3d_4r3_n0t_s4f3}