# Q4: Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
numbers = input("Enter a sequence of comma-separated numbers: ")
list_numbers = numbers.split(",")
tuple_numbers = tuple(list_numbers)
print("List:", list_numbers)
print("Tuple:", tuple_numbers)


