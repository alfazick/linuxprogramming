import socket
from threading import Thread

def handle_client(conn, addr):
    while True:
        # Receiving a message from the client
        data = conn.recv(1024)
        if not data:
            break

        print(f"Received message from {addr}: {data.decode('utf-8')}")
        
        # Sending a response to the client
        conn.sendall(b'Received your message!')
    
    conn.close()
    print(f"Connection with {addr} closed.")

def socket_server():
    # Creating a new socket object using IPv4 and TCP protocols
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Setting the SO_REUSEADDR option to allow the socket to be reused immediately
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Binding the socket to localhost on port 65432
    server_socket.bind(('localhost', 65432))
    
    # Starting to listen for connections
    server_socket.listen()
    print("Server is listening...")

    while True:
        # Accepting a new connection
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        # Sending a welcome message to the client
        conn.sendall(b'Hello from the socket server!')

        # Creating a new thread to handle the client
        client_thread = Thread(target=handle_client, args=(conn, addr))
        client_thread.start()

# Start the socket server
socket_server()
