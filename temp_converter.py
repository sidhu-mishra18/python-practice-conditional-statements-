#temperature converter in python
temp = float(input("Enter the temperature: "))
unit = input("Celsius or Fahrenheit? (C/F): ")

if unit == "C":
    temp = temp*9/5 + 32
    unit = "F"
elif unit == "F":
    temp = (temp-32)*5/9
    unit = "C"
else:
    print(f"{unit} is not a valid unit")
print(f"The converted temperature is {round(temp,1)}{unit}")
             