"""
cryptography.py
Author: Suhan Gui
Credit: http://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list

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
            divide=len(a_list)/len(b_list)
            bb_list=divide*b_list
            ab_list=zip(a_list,bb_list)
            encrypt=[x+y for x, y in ab_list]
            for x in encrypt:
                print(x,end="")
            print("")
        else:
            ddivide=len(b_list)/len(a_list)
            aa_list=ddivide*a_list
            ab_list=zip(aa_list,b_list)
            encrypt=[x+y for x, y in ab_list]
            for x in encrypt:
                print(x,end="")
            print("\n")
    elif doge=="d":
        POTATO=input("Message: ")
        KEY=input("Key: ")
        A_list=[]
        B_list=[]
        for x in POTATO:
            A_list.append(associations.find(x))
        for x in KEY:
            B_list.append(associations.find(x))
        if len(A_list) > len(B_list):
            DIVIDE=len(A_list)/len(b_list)
            BB_list=b_list*DIVIDE
            AB_list= zip(A_list, BB_list)
            decrypt=[x-y for x, y in AB_list]
            for x in decrypt:
                print(x,end="")
            print("\n")
        else:
            DDIVIDE=len(B_list)/len(A_list)
            BB_list=B_list*DDIVIDE
            AB_list= zip(A_list,BB_list)
            decrypt=[x-y for x, y in AB_list]
            for x in decrypt:
                print(x,end="")
            print("\n")
    else:
        print("Did not understand command, try again.")