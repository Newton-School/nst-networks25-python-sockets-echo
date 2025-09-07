# tcp_client.py
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12346        # The port used by the server
MESSAGE = b'Hello, TCP Server!'

# 1. Create a TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    # 2. Connect to the server
    #    This is the step that performs the 3-way handshake.
    #    It will fail if the server is not listening.
    s.connect((HOST, PORT))
    
    # 3. Send the message
    s.sendall(MESSAGE)
    print(f"Sent: '{MESSAGE.decode()}'")
    
    # 4. Wait to receive the echo
    data = s.recv(1024)
    
    print(f"Received echo: '{data.decode()}'")
# The 'with' statement automatically closes the socket.