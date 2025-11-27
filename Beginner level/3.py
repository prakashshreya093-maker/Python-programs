# Q3: Ask the user for a number.Depending on whether the number is even or odd, print out an appropriate message to the user.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.")
