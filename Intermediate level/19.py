# Q19: Python program to count frequency of characters in a given file.
file_name = "char_count.txt"
f_write = open(file_name, 'w')
f_write.write("AaBbCdeEff")
f_write.close()

char_counts = {}

def to_lower(char):
    if 'A' <= char <= 'Z':
        return chr(ord(char) + 32)
    return char

try:
    f_read = open(file_name, 'r')
    content = f_read.read()
    f_read.close()
    
    for char in content:
        if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
            char_key = to_lower(char)
            if char_key in char_counts:
                char_counts[char_key] = char_counts[char_key] + 1
            else:
                char_counts[char_key] = 1
    
    print(f"Character frequency: {char_counts}")

except:
    print(f"Error: Could not read file.")