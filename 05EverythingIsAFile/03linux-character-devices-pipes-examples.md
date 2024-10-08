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

# Create the named pipe
os.mkfifo("my_pipe")

# In one Python script (writer.py)
f = open("my_pipe", "w")
f.write("Hello from the named pipe!")
f.close()


# In another Python script (reader.py)
import os
f = open("my_pipe", "r")
message = f.read()
print("Received:", message)
f.close()

# Clean up
os.remove("my_pipe")
```

To use this Python example:
1. Run the writer script in another terminal: `python writer.py`
2. Run the reader script in one terminal: `python reader.py`

# Multiple messages Canonical Producer Consumer Pattern
#### Python code

```python  
# writer.py
import os

# Open the named pipe in write mode
f = open("my_pipe", "w")

try:
    while True:
        # Get the message from the user
        message = input("Enter message to send (type 'exit' to quit): ")
        if message == 'exit':
            # Send the "stop" message before exiting
            f.write("stop\n")
            f.flush()  # Ensure the "stop" message is sent immediately
            break
        # Write the message to the pipe
        f.write(message + "\n")
        f.flush()  # Ensure the message is sent immediately
finally:
    f.close()

# reader.py
import os
import time

# Open the named pipe in read mode
f = open("my_pipe", "r")

try:
    while True:
        # Read a message from the pipe
        message = f.readline().strip()  # Read one line at a time
        if message:
            print("Received:", message)
            if message == 'exit':
                print("Exit message received. Stopping the reader.")
                break
        else:
            # If no message is received, wait for a bit before checking again
            time.sleep(1)  # This prevents the loop from running too fast
finally:
    f.close()
```

These examples demonstrate how character devices, pipes, and named pipes in Linux can be interacted with as if they were files, both through shell commands and Python code. This illustrates the "Everything is a File" philosophy in Linux, where even these specialized system features are accessed through a consistent file-like interface.
