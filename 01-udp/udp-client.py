# udp_client.py
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12345        # The port used by the server
MESSAGE = b'Hello, UDP Server!'

# 1. Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    
    # 2. Send the message to the server
    #    No 'connect()' is needed for UDP
    s.sendto(MESSAGE, (HOST, PORT))
    print(f"Sent: '{MESSAGE.decode()}'")
    
    # 3. Wait to receive the echo back from the server
    data, server_addr = s.recvfrom(1024)
    
    print(f"Received echo: '{data.decode()}' from {server_addr}")