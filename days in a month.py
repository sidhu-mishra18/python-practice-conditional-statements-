#Write a python program to input month number and print number of days in that month.

month = int(input("Enter the month number: "))
if month in [1,3,5,7,8,10,12]:
    print(f"Month number {month} has 31 days")
elif month in [4,6,9,11]:
    print(f"Month number {month} has 30 days")
elif month == 2:
    print(f"Month number {month} has 28 days")
else:
    print("Enter a valid month number")