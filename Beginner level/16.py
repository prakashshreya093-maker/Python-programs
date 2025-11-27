# Q16: Implement a function that takes input three variables, and returns the largest of the three. Do this without using the Python max() function!
def find_largest(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

print(f"Largest of (10, 5, 15) is: {find_largest(10, 5, 15)}")