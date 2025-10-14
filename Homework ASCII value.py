def is_alphabet(char):
    ascii_value = ord(char)
    if (65 <= ascii_value <= 90) or (97 <= ascii_value <= 122):
        return True
    else:
        return False
    
char = input("Enter a character: ")

if is_alphabet(char):
    print(f"{char} is an alphabet.")
else:
    print(f"{char} is not an alphabet.")