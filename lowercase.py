#Write a python program to check whether a character is uppercase or lowercase alphabet.

char = input("Enter the alphabet: ")
if 65<=ord(char)<=90:
    print(f"{char} is an Uppercase alphabet")
elif 97<=ord(char)<=122:
    print(f"{char} is a lowercase alphabet")
else:
    print("Enter a valid alphabet")