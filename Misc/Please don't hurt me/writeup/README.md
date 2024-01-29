# Please don't hurt me

## Description
I don't know how to create CTF challenge, pls don't hurt me.

Flag format: `n1mdaCTF{flag}`

## Attachment
[images.zip](../dist/images.zip)

## Proof of Concept
The idea of this challenge is to convert JPEG image as a base64 data then split the base64 data to smaller chunks.
Each chunks is 256 byte long or it can be less than 256 byte.
QR code will be generated from those chunks.

To solve the challenge you must scan the QR code of the first image and decode the base64 data.
Upon further inspection you would notice that the first image is showing the characteristics of JPEG or JFIF file signature.
You can create a program to scan all of the QR code, decode it using base64, combine all the decoded base64 chunks and save the result as JPEG image.
