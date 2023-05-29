# hide

## Author
Arasy Dafa Sulistya Kurniawan - omegathrone

## Deskripsi
im good at hiding

## Hint
why don't you just look inside?

## Message
Diberikan suatu file binary [Binary](challenge/hide)

## Step
Player harus mencari flag yang berada dalam file binary tersebut. Dapat digunakan command `strings` untuk melihat isi daripada file binary tersebut dan terdapat dua part flag yang mana jika digabungkan menghasilkan flag secara utuh.

## Resource
Terdapat file [Hide](source/hide.c) untuk menyembunyikan flag ke dalam binary. Untuk generate binary menggunakan command 
```shell
gcc hide.c -o challenge/hide
```

## Flag
### n1mdaCTF{f14gs_h4rdc0d3d_4r3_n0t_s4f3}