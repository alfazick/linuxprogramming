
import os
import socket
import time

# Step 1: Working with Regular Files
# Create regular files and write data to them
with open('file1.txt', 'w') as f:
    f.write("Hello, this is a regular file.\n")
    
# Step 2: Working with Directories
# Create a directory and organize files within it
os.mkdir('example_dir')
os.rename('file1.txt', 'example_dir/file1.txt')

# Step 3: Working with Symbolic Links (Symlinks)
# Create a symbolic link to a file
os.symlink('file1.txt', 'example_dir/symlink_to_file1.txt')

# Step 4: Working with FIFO (Named Pipes)
# Create a named pipe and write data to it in a separate process
os.mkfifo('example_fifo')
def fifo_writer():
    with open('example_fifo', 'w') as f:
        f.write("Hello from the FIFO writer!")
    
from threading import Thread
writer_thread = Thread(target=fifo_writer)
writer_thread.start()

# Open the named pipe and read data from it
with open('example_fifo', 'r') as f:
    print(f.read())  # Output: Hello from the FIFO writer!

# Clean up FIFO file
os.remove('example_fifo')

# Step 5: Working with Sockets
# Open a socket for inter-process communication
def socket_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 65432))
    server_socket.listen()
    conn, addr = server_socket.accept()
    with conn:
        conn.sendall(b'Hello from the socket server!')
    
server_thread = Thread(target=socket_server)
server_thread.start()

# Allow the server to start listening before the client attempts to connect
time.sleep(0.1)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 65432))
data = client_socket.recv(1024)
print(data.decode('utf-8'))  # Output: Hello from the socket server!

# Cleanup: close socket and remove created files and directories
client_socket.close()
# os.remove('example_dir/symlink_to_file1.txt')
# os.remove('example_dir/file1.txt')
# os.rmdir('example_dir')