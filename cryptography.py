"""
cryptography.py
Author: Suhan Gui
Credit: Stack Overflow

Assignment: Cryptography

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

doge=input("Enter e to encrypt, d to decrypt, or q to quit: ")

for x in doge:
    if doge=="q":
        print("Goodbye!")
        elif doge=="e":
            putin=input("Message: ")
            print("Key: Lorem ipsum")
           # print(encrypt)
            elif doge=="d":
                obama=input("Message: ")
                print("Key: Lorem ipsum")
                #print(encrypt)
                else:
                    print("Did not understand command, try again.")