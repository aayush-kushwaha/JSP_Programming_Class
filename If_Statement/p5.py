'''
5. WAP to check whether the given character is either UpperCase or LowerCase or Numbers.
'''
char = input("Enter a character: ")
if "A" <= char <= "Z":
    print("UpperCase")
elif "a" <= char <= "z":
    print("LowerCase")
elif "0" <= char <= "9":
    print("Number")
else:
    print("Special Character")