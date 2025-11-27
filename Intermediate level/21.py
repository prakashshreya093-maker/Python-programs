# Q21: Python program to compute the number of characters, words and lines in a file.
file_name = "stats.txt"
f_write = open(file_name, 'w')
f_write.write("This is line one.\nThis is line two.")
f_write.close()

char_count = 0
word_count = 0
line_count = 0

try:
    f_read = open(file_name, 'r')
    
    for line in f_read:
        line_count = line_count + 1
        char_count = char_count + len(line)

        in_word = 0
        for char in line:
            if char == ' ' or char == '\n' or char == '\r':
                in_word = 0
            else:
                if in_word == 0:
                    word_count = word_count + 1
                in_word = 1
    
    f_read.close()
    
    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {char_count}")

except:
    print(f"Error: Could not read file.")