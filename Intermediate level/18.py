# Q18: Python program to copy the contents of a file to another file.
source_file = "source.txt"
destination_file = "destination.txt"

f_source_write = open(source_file, 'w')
f_source_write.write("This content will be copied.")
f_source_write.close()

try:
    f_source = open(source_file, 'r')
    content = f_source.read()
    f_source.close()
    
    f_destination = open(destination_file, 'w')
    f_destination.write(content)
    f_destination.close()
    
    print(f"Content successfully copied from {source_file} to {destination_file}.")
        
except:
    print(f"Error: Could not perform file operations.")