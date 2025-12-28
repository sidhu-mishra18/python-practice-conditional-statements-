#Write a python program to calculate profit or loss.

cp = float(input("Enter the cost price: "))
sp = float(input("Enter the selling price: "))

if sp>cp:
    print(f"It is a profit of ${round(sp-cp,1)}")
elif cp>sp:
    print(f"It is a loss of ${round(cp-sp,1)}")
else:
    print("There is no profit or loss")