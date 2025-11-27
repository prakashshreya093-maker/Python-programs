# Q13: Ask the user for a number and determine whether the number is prime or not.
num_input = input("Enter an integer to check if it's prime: ")
num = int(num_input)

if num <= 1:
    print(f"{num} is not a prime number.")
elif num == 2:
    print(f"{num} is a prime number.")
else:
    is_prime = 1
    i = 2
    while i < num:
        if num % i == 0:
            is_prime = 0
            break
        i = i + 1
    
    if is_prime == 1:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")