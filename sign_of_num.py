#Write a python program to check whether a number is negative, positive or zero

num = int(input("Enter the number: "))
if num>0:
    print(f"{num} is positive")
elif num<0:
    print(f"{num} is negative")
elif num == 0:
    print(f"{num} is zero")