import os
import sys

# Open a file and get the file descriptor
fd = os.open("sample.txt", os.O_RDWR | os.O_CREAT)

# Write to the file using the file descriptor
os.write(fd, b"Hello, File Descriptors!")

# Move the file pointer to the beginning
os.lseek(fd, 0, os.SEEK_SET)

# Read from the file using the file descriptor
content = os.read(fd, 100)  # Read 100 bytes

# Print the content to stdout
print(f"Read from file (stdout): {content.decode()}")

# Simulate an error message to stderr
print("This is an error message!", file=sys.stderr)

# Prompt the user for input from stdin
user_input = input("Enter something for stdin demonstration: ")

# Print the user input to stdout
print(f"You entered (stdout): {user_input}")

# Close the file descriptor
os.close(fd)
