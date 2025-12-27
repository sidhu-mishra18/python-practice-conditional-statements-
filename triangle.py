#Write a python program to input angles of a triangle and check whether triangle is valid or not

a = int(input("Enter the first angle: "))
b = int(input("Enter the second angle: "))
c = int(input("Enter the third angle: "))

if a+b+c == 180 and a>0 and b>0 and c>0:
    print("The three angles form a triangle")
else:
    print("The three angles do not form a triangle")