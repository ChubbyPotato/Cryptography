"""
cryptography.py
Author: Suhan Gui
Credit: Stack Overflow

Assignment: Cryptography

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
#doge=(dict(map(lambda letter:(letter,len(potato)-len(potato.replace(letter,''))),potato)))
#sorted_doge = sorted(doge.items(), key=operator.itemgetter(0))
#converted_doge = list(doge.items())
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
        print("{0}".format(str(encrypt)))
        for x in associations:
            encrypt=
            associations.find(char)
    elif doge=="d":
        tomato=input("Message: ")
        key=input("Key: ")
        print("{0}}".format(str(decrypt)))
        for x in associations:
            decrypt=
            associations.find(char)
    else:
        print("Did not understand command, try again.")