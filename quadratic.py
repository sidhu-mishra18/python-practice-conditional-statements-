#Write a python program to find all roots of a quadratic equation
import math
a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter the coeffcient of x: "))
c = int(input("Enter the constant: "))

d = b**2-4*a*c
if a == 0:
    print("It is not a quadratic equation")
else:
    if d == 0:
        x =(-b +math.sqrt(d))/(2*a)
        print(f"The roots of the equation are {x} and {x}")
    elif d>0:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b-math.sqrt(d))/(2*a)
        print(f"The roots of the equation are {x1} and {x2}")
    else:
        x1 = (-b + math.sqrt(-d))/(2*a)
        x2 = (-b-math.sqrt(-d))/(2*a)
        print(f"The roots of the equation are {x1} and {x2}")