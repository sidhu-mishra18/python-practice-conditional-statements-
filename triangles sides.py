#Write a python program to input all sides of a triangle and check whether triangle is valid or not.

a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))

if a>0 and b>0 and c>0 and a+b>c and a+c>b and c+b>a:
    print("The three sides form a triangle")
else:
    print("The three sides do not form a triangle")