# Q17:Python program to perform read and write operations on a file.
file_name = "sample_file.txt"
content_to_write = "Hello, this is a test line.\nWriting another line now."

f_write = open(file_name, 'w')
f_write.write(content_to_write)
f_write.close()
print(f"Successfully wrote content to {file_name}.")

f_read = open(file_name, 'r')
content = f_read.read()
f_read.close()
print(f"\nContent read from {file_name}:\n{content}")