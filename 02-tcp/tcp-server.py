# tcp_server.py
import socket

HOST = '127.0.0.1'  # (localhost)
PORT = 12346        # Port to listen on

# 1. Create a TCP socket
#    SOCK_STREAM is for TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    # 2. Bind the socket to the address and port
    s.bind((HOST, PORT))
    
    # 3. Start listening for incoming connections
    s.listen()
    print(f"TCP Server listening on {HOST}:{PORT}")
    
    # 4. Accept a connection (this is a blocking call)
    #    accept() returns a new socket object for the connection
    #    and the address of the client.
    conn, addr = s.accept()
    
    with conn:
        print(f"Connected by {addr}")
        # 5. Receive data from the client and echo it back
        data = conn.recv(1024) # buffer size is 1024 bytes
        print(f"Received message: '{data.decode()}'")
        
        conn.sendall(data)
        print(f"Echoed message back to {addr}")
# The 'with' statement automatically closes the connection and server sockets.