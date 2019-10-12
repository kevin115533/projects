"""
Program: Caesar Cipher
Author: Kevin Tran

The purpose of this program is to encrypt a message

1. Get message and distance inputs
2. Loop to convert all characters according to ASCII values plus distance
3. Print the resulting message
"""

message = input("Enter the message you would like to encrypt: ")
distance = int(input("Enter a distance value: "))
eMessage = ""

for ch in message:
    ordValue = ord(ch)
    eValue = ordValue + distance
    eMessage += chr(eValue)
print(eMessage)


