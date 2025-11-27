# Q5: Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

sum = num1 + num2 + num3

if num1 == num2 == num3:
    sum = sum * 3

# Display the result
print("The result is:", sum)
