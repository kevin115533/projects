"""
Program: Caesar Cipher Decrypter
Author: Kevin Tran

The purpose of this program is to decrypt a message

1. Get message and distance inputs
2. Loop to convert all characters according to ASCII values plus distance
3. Print the resulting message
"""

message = input("Enter the message you would like to decrypt: ")
distance = int(input("Enter a distance value: "))
dMessage = ""

for ch in message:
    ordValue = ord(ch)
    eValue = ordValue - distance
    dMessage += chr(eValue)
print(dMessage)
