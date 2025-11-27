# Q20: Python program to print each line of a file in reverse order.
file_name = "reverse_lines.txt"
f_write = open(file_name, 'w')
f_write.write("First line.\nSecond line.")
f_write.close()

try:
    f_read = open(file_name, 'r')
    
    for line in f_read:
        i = 0
        while i < len(line) and (line[i] == ' ' or line[i] == '\n' or line[i] == '\r'):
            i = i + 1
        start = i
        
        j = len(line) - 1
        while j >= 0 and (line[j] == ' ' or line[j] == '\n' or line[j] == '\r'):
            j = j - 1
        end = j
        
        reversed_line = ""
        k = end
        while k >= start:
            reversed_line = reversed_line + line[k]
            k = k - 1
            
        print(reversed_line)
    
    f_read.close()

except:
    print(f"Error: Could not read file.")