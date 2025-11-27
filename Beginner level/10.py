# Q10: Ask the user for a string and print out whether this string is a palindrome or not.
s = input("Enter a string: ")

length = 0
for char in s:
    length = length + 1

reversed_s = ""
i = length - 1
while i >= 0:
    reversed_s = reversed_s + s[i]
    i = i - 1

if s == reversed_s:
    print(f"'{s}' is a Palindrome.")
else:
    print(f"'{s}' is NOT a Palindrome.")