import socket

def client_chat():
    # Creating a new socket object using IPv4 and TCP protocols
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connecting to the server at localhost on port 65432
    client_socket.connect(('localhost', 65432))
    
    # Receiving a welcome message from the server
    data = client_socket.recv(1024)
    print(data.decode('utf-8'))

    while True:
        # Taking user input and sending it to the server
        msg = input("You: ")
        
        # If the user types "exit", close the connection and exit the loop
        if msg.lower() == "exit":
            break
        
        # Send the user's message to the server
        client_socket.sendall(msg.encode('utf-8'))

        # Receiving a response from the server and printing it
        data = client_socket.recv(1024)
        print(f"Server: {data.decode('utf-8')}")

    # Close the socket connection
    client_socket.close()
    print("Connection closed.")

# Start the client chat
client_chat()
