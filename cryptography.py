"""
cryptography.py
Author: Suhan Gui
Credit: Stack Overflow

Assignment: Cryptography

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"


x = ""
while x != "q":
    doge=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if x=="q":
        print("Goodbye!")
        break
    elif x=="e":
        potato=input("Message: ")
        Key=input("Key: ")
        #print("{0} = {1}\n".format(potato,encrypt))
        #encrypt=
    elif x=="d":
        tomato=input("Message: ")
        key=input("Key: ")
        #print("{0} = {1}\n".format(tomato,decrypt))
        #decrypt=
    else:
        print("Did not understand command, try again.\n")