# Q7: Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] and write a program that prints out all the elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

less_than_5 = []
for element in a:
    if element < 5:
        less_than_5 = less_than_5 + [element]
print(f"Elements less than 5 (New List): {less_than_5}")

x_input = input("Enter a number to filter the list by: ")
x = int(x_input)
smaller_than_x = []
for element in a:
    if element < x:
        smaller_than_x = smaller_than_x + [element]
print(f"Elements smaller than {x}: {smaller_than_x}")