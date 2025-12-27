#Write a python program to check whether a character is alphabet or not.
char = input("Enter the character: ")
if 65<=ord(char)<=91 or 97<=ord(char)<=122:
    print(f"{char} is an alphabet")
else:
    print(f"{char} is not an alphabet")