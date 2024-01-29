# stream

## Author
Moch. Imam Rifai - underzero

## Deskripsi
Recently researchers have found a beautiful stream in a remote village.

According to local residents, there is a legend that says only a chosen person can discover the secrets of the stream. Can you help them to find the secret?

## Attachment
[stream.rar](../dist/stream.rar)

## Tags
- Windows
- NTFS

## Hints
The legend also says that you can see the secrets of the stream through the window

## Points
100

## Solusi
Mengamati dari deskripsi soal dan judul soal yaitu stream dan terdapat rahasia dari stream, maka challenge kemungkinan melibatkan Alternate Data Stream (ADS) pada file system NTFS yang ada pada Windows.
Untuk itu challenge ini bisa diselesaikan menggunakan OS Windows.

Setelah mengekstrak file `stream.rar` terdapat sebuah file `stream.jpg`. 
Untuk melihat adanya ADS bisa menggunakan `Command Prompt` atau `PowerShell`. 
Langkah di bawah ini menunjukkan bagaimana caranya melihat ADS menggunakan `Command Prompt`

```
C:\stream> dir /r
-- output truncated --
26/05/2023  14:11           149.389 stream.jpg
                                347 stream.jpg:secret:$DATA
                                319 stream.jpg:Zone.Identifier:$DATA
               2 File(s)        149.982 bytes
               2 Dir(s)  57.695.985.664 bytes free
```

Dari hasil perintah tersebut terlihat bahwa terdapat ADS dengan nama `secret` untuk melihat konten dari ADS menggunakan perintah berikut ini pada `Command Prompt`

```
C:\stream> more < stream.jpg:secret
cmVzdWx0ID0gIiINCg0KcGxhaW50ZXh0ID0gIn45fWxxS0ROa0p1V3NpYm12fXxXZ2FkYE9JfHx1en5pZG1PLFRJRElPe2R6dWl9dSINCg0KZm9yIGkgaW4gcmFuZ2UoMCwgbGVuKHBsYWludGV4dCkpOg0KICAgIGlmIGkgJSAyID09IDA6DQogICAgICAgIHJlc3VsdCArPSBjaHIob3JkKHBsYWludGV4dFtpXSkgXiAxNikNCiAgICBlbHNlOg0KICAgICAgICByZXN1bHQgKz0gY2hyKG9yZChwbGFpbnRleHRbaV0pIF4gOCkNCg0KcHJpbnQocmVzdWx0KQ==
```

Terdapat sebuah ADS yang diencode menggunakan base64. Hasil decode seperti berikut ini

```python
result = ""

plaintext = "~9}lqKDNkJuWsibmv}|Wgad`OI||uz~idmO,TIDIO{dzui}u"

for i in range(0, len(plaintext)):
    if i % 2 == 0:
        result += chr(ord(plaintext[i]) ^ 16)
    else:
        result += chr(ord(plaintext[i]) ^ 8)

print(result)
```

Isi dari ADS adalah sebuah program Python yang diencode menggunakan base64. Jalankan program Python tersebut maka didapat flag.

Selain menggunakan `Command Prompt` untuk menampilkan ADS, bisa juga menggunakan `PowerShell`. 
Command di bawah ini akan menampilkan semua ADS yang ada pada sistem

```powershell
PS C:\stream> gci -recurse | % { gi $_.FullName -stream * } | where stream -ne `:$Data'              

PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\stream\stream.jpg:secret
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\stream
PSChildName   : stream.jpg:secret
PSDrive       : C
PSProvider    : Microsoft.PowerShell.Core\FileSystem
PSIsContainer : False
FileName      : C:\stream\stream.jpg
Stream        : secret
Length        : 347

PSPath        : Microsoft.PowerShell.Core\FileSystem::C:\stream\stream.jpg:Zone.Identifier
PSParentPath  : Microsoft.PowerShell.Core\FileSystem::C:\stream
PSChildName   : stream.jpg:Zone.Identifier
PSDrive       : C
PSProvider    : Microsoft.PowerShell.Core\FileSystem
PSIsContainer : False
FileName      : C:\stream\stream.jpg
Stream        : Zone.Identifier
Length        : 319
```

Untuk menampilkan konten dari ADS `secret` menggunakan `PowerShell` seperti berikut ini

```powershell
PS C:\stream> Get-Content -path .\stream.jpg -stream secret
cmVzdWx0ID0gIiINCg0KcGxhaW50ZXh0ID0gIn45fWxxS0ROa0p1V3NpYm12fXxXZ2FkYE9JfHx1en5pZG1PLFRJRElPe2R6dWl9dSINCg0KZm9yIGkgaW4gcmFuZ2UoMCwgbGVuKHBsYWludGV4dCkpOg0KICAgIGlmIGkgJSAyID09IDA6DQogICAgICAgIHJlc3VsdCArPSBjaHIob3JkKHBsYWludGV4dFtpXSkgXiAxNikNCiAgICBlbHNlOg0KICAgICAgICByZXN1bHQgKz0gY2hyKG9yZChwbGFpbnRleHRbaV0pIF4gOCkNCg0KcHJpbnQocmVzdWx0KQ==
```

## Flag
### n1mdaCTF{Be_careful_with_Alternate_$DATA_stream}
