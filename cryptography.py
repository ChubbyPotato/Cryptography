"""
cryptography.py
Author: Suhan Gui
Credit: Stack Overflow

Assignment: Cryptography

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""

x = ""
while x != "q":
    doge=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
    if doge=="q":
        print("Goodbye!")
        break
    elif doge=="e":
        potato=input("Message: ")
        key=input("Key: ")
        print(encrypt)
        for x in potato:
            associations.find(x)
        for x in key:
            associations.find(x)
    elif doge=="d":
        POTATO=input("Message: ")
        KEY=input("Key: ")
        print(decrypt)
        for x in POTATO:
            associations.find(x)
        for x in KEY:
            associations.find(x)
    else:
        print("Did not understand command, try again.")