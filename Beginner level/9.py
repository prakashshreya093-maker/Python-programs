A = [1, 2, 2, 3, 4, 5, 5, 6, 7]
B = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common = []

for element in A:
    
    if element in B and element not in common:
        common.append(element)

print("Common elements without duplicates:", common)

