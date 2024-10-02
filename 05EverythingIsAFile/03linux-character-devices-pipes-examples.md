# Linux Character Devices, Pipes, and Named Pipes: Commands and Python Code

This document demonstrates the use of character devices, pipes, and named pipes (FIFOs) in Linux, showing both shell commands and equivalent Python code.

## 1. Character Devices

Character devices in Linux are accessed as files, typically in the `/dev` directory. They allow reading or writing one character at a time.

### Example: Reading from the keyboard (stdin)

#### Linux Command:
```bash
cat /dev/stdin
# Type some text and press Ctrl+D to end input
```

#### Python Code:
```python
import sys

print("Type some text (press Ctrl+D to end):")
for line in sys.stdin:
    print("You typed:", line.strip())
```

### Example: Writing to the terminal (stdout)

#### Linux Command:
```bash
echo "Hello, terminal!" > /dev/tty
```

#### Python Code:
```python
import sys

sys.stdout.write("Hello, terminal!\n")
sys.stdout.flush()
```

## 2. Pipes

Pipes allow the output of one process to be used as input to another process.

### Example: Using a pipe to filter output

#### Linux Command:
```bash
ls -l | grep ".txt"
```

#### Python Code:
```python
import subprocess

ls_process = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
grep_process = subprocess.Popen(["grep", ".txt"], stdin=ls_process.stdout, stdout=subprocess.PIPE)
ls_process.stdout.close()

output, _ = grep_process.communicate()
print(output.decode())
```

## 3. Named Pipes (FIFOs)

Named pipes, or FIFOs, are special files that act as a pipe between two processes.

### Creating and Using a Named Pipe

#### Linux Commands:
```bash
# Terminal 1
mkfifo my_pipe
cat > my_pipe

# Terminal 2
cat < my_pipe
```

#### Python Code:
```python
import os
import time

# Create the named pipe
os.mkfifo("my_pipe")

# In one Python script (writer.py)
f = open("my_pipe", "w")
f.write("Hello from the named pipe!")
f.close()

# In another Python script (reader.py)
f = open("my_pipe", "r")
message = f.read()
print("Received:", message)
f.close()

# Clean up
os.remove("my_pipe")
```

To use this Python example:
1. Run the reader script in one terminal: `python reader.py`
2. Run the writer script in another terminal: `python writer.py`


#### Python Code:
```python
import os
import time

# Ensure the pipe doesn't exist
if os.path.exists("my_pipe"):
    os.remove("my_pipe")

# Create the named pipe
os.mkfifo("my_pipe")

# Fork the process
pid = os.fork()

if pid == 0:  # Child process (reader)
    f = open("my_pipe", "r")
    message = f.read()
    print("Child received:", message)
    f.close()
else:  # Parent process (writer)
    time.sleep(1)  # Ensure the child is ready to read
    f = open("my_pipe", "w")
    f.write("Hello from parent!")
    f.close()
    os.waitpid(pid, 0)  # Wait for child to finish

# Clean up
os.remove("my_pipe")
```

These examples demonstrate how character devices, pipes, and named pipes in Linux can be interacted with as if they were files, both through shell commands and Python code. This illustrates the "Everything is a File" philosophy in Linux, where even these specialized system features are accessed through a consistent file-like interface.
