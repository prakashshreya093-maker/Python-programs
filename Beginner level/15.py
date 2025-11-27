# Q15: Write a function that takes an ordered list of numbers and a number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
def is_in_list(sorted_list, number):
    return number in sorted_list

ordered_list = [1, 3, 5, 7, 9, 11]
num = int(input("Enter a number to check: "))

print(is_in_list(ordered_list, num))
