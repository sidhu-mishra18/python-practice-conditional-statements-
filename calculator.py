#calculator with python

operation = input("Enter an operation (+ - * /): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)
else:
    print("Enter a valid operator")
