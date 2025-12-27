#weight converter in python

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight*2.205
    unit = "Lbs"
elif unit == "L":
    weight = weight/2.205
    unti = "Kgs"
else:
    print(f"{unit} is not valid")
print(f"Your converted weight is {round(weight,1)}{unit}")