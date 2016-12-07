"""
cryptography.py
Author: Suhan Gui
Credit:http://stackoverflow.com/questions/2356501/how-do-you-round-up-a-number-in-python

Assignment: Cryptography

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
import math
x = ""
while x != "q":
    doge=input("Enter e to encrypt, d to decrypt, or q to quit: ")
    associations = "Indigo_program_com__//console_de_crease"
    andre="Cease"
    bub=9000*andre
    fin=9000*associations
    if doge=="q":
        print("Goodbye!")
        break
    elif doge=="e":
        potato=input("Message: ")
        key=input("Key: ")
        a_list=[]
        b_list=[]
        c_list=[]
        for x in potato:
            a_list.append(associations.find(x))
        for x in key:
            b_list.append(associations.find(x))
        if len(a_list) > len(b_list):
            divide=len(a_list)/len(b_list)
            a=math.ceil(divide)
            bb_list=a*b_list
            ab_list=zip(a_list,bb_list)
            encrypt=[x+y for x, y in ab_list]
        else:
            ddivide=len(b_list)/len(a_list)
            a=math.ceil(ddivide)
            aa_list=a*a_list
            babbbb="delete_command"
            ab_list=zip(aa_list,b_list)
            encrypt=[x+y for x, y in ab_list]
        for x in encrypt:
            print(fin[x],end="")
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
            DIVIDE=float(len(A_list)/len(B_list))
            a=math.ceil(DIVIDE)
            BB_list=B_list*a
            AB_list= zip(A_list, BB_list)
            decrypt=[x-y for x, y in AB_list]
        else:
            DDIVIDE=len(B_list)/len(A_list)
            a=math.ceil(DDIVIDE)
            AA_list=A_list*a
            AB_list= zip(AA_list,B_list)
            decrypt=[x-y for x, y in AB_list]
        for x in decrypt:
            print(fin[x],end="")
        print("\n")
    else:
        print("Did not understand command, try again.")