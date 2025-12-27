#Write a python program to input any alphabet and check whether it is vowel or consonant.

char = input("Enter the alphabet: ")
if char.lower() in ['a','e','i','o','u']:
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")