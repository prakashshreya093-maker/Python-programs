# Q14: Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
a = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_list = []
for item in a:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)

