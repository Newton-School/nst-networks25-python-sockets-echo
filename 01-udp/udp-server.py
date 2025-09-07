# udp_server.py
import socket

HOST = '127.0.0.1'  # (localhost)
PORT = 12345        # Port to listen on (any port greater than 1024 not used on your computer)

# 1. Create a UDP socket
#    AF_INET is for IPv4
#    SOCK_DGRAM is for UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    
    # 2. Bind the socket to the address and port
    s.bind((HOST, PORT))
    print(f"UDP Server listening on {HOST}:{PORT}")
    
    # 3. Wait for a message (this is a blocking call)
    #    recvfrom returns the data and the address of the client that sent it
    data, addr = s.recvfrom(1024) # buffer size is 1024 bytes
    
    print(f"Received message: '{data.decode()}' from {addr}")
    
    # 4. Echo the message back to the client
    s.sendto(data, addr)
    print(f"Echoed message back to {addr}")