

# Examples of Commands Using the Python Script

## Introduction

To deeply understand Pipes and Redirection, we need to go through a code demonstration first. We'll use the following Python script (`file_descriptor.py`) as our example:

```python
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
```

Assuming our Python script is saved as `file_descriptor.py`, here are some examples of commands that demonstrate pipes and redirection using this script:

## 1. Basic Execution

```bash
python file_descriptor.py
```
This will run the script normally, writing to sample.txt and interacting with stdout, stderr, and stdin as coded.

## 2. Redirecting stdout to a File

```bash
python file_descriptor.py > output.txt
```
This will redirect the stdout of the script to output.txt. The file will contain the "Read from file" message and the echoed user input, but not the error message (which goes to stderr).

## 3. Redirecting stderr to a File

```bash
python file_descriptor.py 2> error.txt
```
This will redirect the stderr of the script to error.txt. The file will contain only the error message.

## 4. Redirecting Both stdout and stderr to Different Files

```bash
python file_descriptor.py > output.txt 2> error.txt
```
This separates the standard output and error streams into two different files.

## 5. Redirecting Both stdout and stderr to the Same File

```bash
python file_descriptor.py > all_output.txt 2>&1
```
This redirects both stdout and stderr to all_output.txt. The `2>&1` syntax means "redirect stderr to wherever stdout is currently pointing".

## 6. Using Input Redirection

```bash
echo "Predefined input" | python file_descriptor.py
```
This pipes the output of the echo command as input to our Python script, automatically answering the input prompt.

## 7. Combining Input and Output Redirection

```bash
echo "Predefined input" | python file_descriptor.py > output.txt 2> error.txt
```
This command provides input to the script via a pipe, redirects stdout to output.txt, and stderr to error.txt.

## 8. Using the Script in a Pipeline

```bash
python file_descriptor.py | grep "stdout"
```
This runs the script and pipes its output to grep, which will only display lines containing "stdout".

## 9. Redirecting to /dev/null

```bash
python file_descriptor.py > /dev/null 2>&1
```
This discards all output (both stdout and stderr) by redirecting it to /dev/null.

## 10. Using tee for Output and Logging

```bash
python file_descriptor.py | tee output.txt
```
This runs the script, displaying its output on the screen and also saving it to output.txt.

These examples demonstrate various ways to use pipes and redirection with the given Python script, illustrating the concepts discussed in the previous explanation.
