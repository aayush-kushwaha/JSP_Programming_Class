'''
4. WAP to check whether the given number is divisible by 3 and 5 or not. If number is divisible\
    by 3, print the cube of that number. If it is divisible by 5, print the power 5 of that\
    number. If it is divisible by both 3 and 5, add 3 and 5 to that number and print the output.
'''
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(num + 3 + 5)
elif num % 3 == 0:
    print(num ** 3)
elif num % 5 == 0:
    print(num ** 5)
