# Q24: Write a Regular Expression to represent all 10 digit mobile numbers. Rules: 1. Every number should contain exactly 10 digits. 2. The first digit should be 7 or 8 or 9. Write a Python Program to check whether the given number is valid mobile number or not.
def is_digit(char):
    if '0' <= char <= '9':
        return 1
    return 0

def validate_mobile_number(number):
    if len(number) != 10:
        return False
    
    if not (number[0] == '7' or number[0] == '8' or number[0] == '9'):
        return False
        
    i = 1
    while i < 10:
        if is_digit(number[i]) == 0:
            return False
        i = i + 1
        
    return True

mobile_num = input("Enter a 10-digit mobile number: ")

if validate_mobile_number(mobile_num):
    print(f"'{mobile_num}' is a VALID mobile number.")
else:
    print(f"'{mobile_num}' is NOT a valid mobile number according to the rules.")