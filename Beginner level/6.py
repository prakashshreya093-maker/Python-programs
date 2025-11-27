# Q6: Write a Python program to test whether a passed letter is a vowel or not.
letter = input("Enter a letter: ").lower()  

if letter in ('a', 'e', 'i', 'o', 'u'):
    print(f"The letter '{letter}' is a vowel.")
else:
    print(f"The letter '{letter}' is not a vowel.")

