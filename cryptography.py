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
        Key=input("Key: ")
        print("{0}".format(int(decrypt)))
        for x in potato:
            b=str(associations.find(a))
            a="d"
    elif doge=="d":
        tomato=input("Message: ")
        key=input("Key: ")
        print("{0}".format(int(decrypt)))
        for x in tomato:
            decrypt=(B)
            B=associations.find(A)
            #A=
    else:
        print("Did not understand command, try again.")