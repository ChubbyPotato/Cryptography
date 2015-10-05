"""
cryptography.py
Author: Suhan Gui
Credit: 

Assignment: Cryptography

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

doge=input("Enter e to encrypt, d to decrypt, or q to quit: ")

for x in doge:
    if x=="q":
        print("Goodbye!")
        break
    elif x=="e":
        potato=input("Message: ")
        input("Key: ")
        #print(encrypt"="coded)
        #encrypt=
    elif x=="d":
        tomato=input("Message: ")
        input("Key: ")
        #print(decrypt"="decoded)
        #decrypt=
    else:
        print("Did not understand command, try again.")
    doge=input("Enter e to encrypt, d to decrypt, or q to quit: ")