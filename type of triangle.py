#Write a python program to check whether the triangle is equilateral, isosceles or scalene triangle.

a = int(input("Enter the first side: "))
b = int(input("Enter the second side: "))
c = int(input("Enter the third side: "))
if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
    if a==b and a==c:
        print("It is an equilateral triangle")
    elif a==b!=c or a==c!=b or b==c!=a:
        print("It is an isosceles triagnle")
    elif a!=b and a!=c and b != c:
        print("It is a scalene triangle")
else:
    print("Invalid ")