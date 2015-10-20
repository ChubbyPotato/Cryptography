"""
cryptography.py
Author: Suhan Gui
Credit: http://stackoverflow.com/questions/1720421/join-two-lists-in-python

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
        a_list=[]
        b_list=[]
        for x in potato:
            a_list.append(associations.find(x))
        for x in key:
            b_list.append(associations.find(x))
        if len(a_list) > len(b_list):
            
        else:
            
        encrypt=[x+y for x, y in zip(A_list, B_list)]
    elif doge=="d":
        POTATO=input("Message: ")
        KEY=input("Key: ")
        A_list=[]
        B_list=[]
        for x in POTATO:
            A_list.append(associations.find(x))
        for x in KEY:
            B_list.append(associations.find(x))
        if len(a_list) > len(b_list):
            
        else:
            
        decrypt=[x-y for x, y in zip(A_list, B_list)]
    else:
        print("Did not understand command, try again.")