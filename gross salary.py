'''Write a C program to input basic salary of an employee and calculate its Gross salary according to following:
Basic Salary <= 10000 : HRA = 20%, DA = 80%
Basic Salary <= 20000 : HRA = 25%, DA = 90%
Basic Salary > 20000 : HRA = 30%, DA = 95%'''

basic = float(input("Enter your basic salary: "))
if basic > 20000:
    net = basic + basic*(20/100) + basic*(80/100)
    print(f"Gross salary is {net}")
elif basic > 10000:
    net = basic + basic*(25/100) + basic*(90/100)
    print(f"Gross salary is {net}")
else:
    net = basic + basic*(30/100) + basic*(95/100)
    print(f"Gross salary is {net}")
