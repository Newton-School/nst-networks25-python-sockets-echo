# **TCP vs. UDP: Simple Socket Programming Exercises**

Through two short activities, learners will observe the core concepts of "connectionless" vs. "connection-oriented" communication.

## **Prerequisites**

* Python 3.x installed on your system.  
* Access to a command line or terminal.

## **Repository Structure**

```
.  
├── 01-udp  
│   ├── udp-client.py   # A simple UDP client  
│   └── udp-server.py   # A simple UDP server that echoes messages  
└── 02-tcp  
    ├── tcp-client.py   # A simple TCP client  
    └── tcp-server.py   # A simple TCP server that echoes messages
```

## **Activity 1: UDP - The "Fire-and-Forget" Protocol**

**Objective:** To demonstrate that UDP is connectionless. A client can send a datagram without any error, even if the server is not running.

### **Instructions**

1. Open two separate terminal windows and navigate to the 01-udp directory in both.  
2. **Run the Server:** In the first terminal, start the UDP server. It will wait for a message.

```bash
   python3 udp-server.py  
   # Expected output:  
   # UDP Server listening on 127.0.0.1:12345
```

3. **Run the Client:** In the second terminal, run the client. It will send a message and print the echo it receives from the server.

```bash
   python3 udp-client.py  
   # Expected output:  
   # Sent: 'Hello, UDP Server\!'  
   # Received echo: 'Hello, UDP Server\!'
```

   You will also see the server's terminal print that it received and echoed the message.

4. **The Experiment:** Now, stop the server in the first terminal (press Ctrl+C).  

5. Run the client again from the second terminal.

```bash
   python3 udp-client.py  
   # Expected output:  
   # Sent: 'Hello, UDP Server!'  
   # (The script will now hang, waiting for a reply...)
```

### **Observation & Key Takeaway UDP**

Notice that the client script sent the message without any immediate error. It only hangs because it's waiting for a reply that will never arrive.

This demonstrates the "fire-and-forget" nature of UDP. The client's operating system successfully sent the packet to the network, but it has no knowledge of whether an application was listening on the other end.

**UDP is connectionless.**

## **Activity 2: TCP - The Reliable Connection**

**Objective:** To demonstrate that TCP is connection-oriented. A client will fail immediately if it cannot establish a connection with the server.

### **Instructions**

1. Open two separate terminal windows and navigate to the 02-tcp directory in both.  
2. **Run the Server:** In the first terminal, start the TCP server. It will listen for an incoming connection.

```bash
   python tcp-server.py  
   # Expected output:  
   # TCP Server listening on 127.0.0.1:12346
```

3. **Run the Client:** In the second terminal, run the client. It will connect to the server, send a message, and receive an echo.

```bash
   python tcp-client.py  
   # Expected output:  
   # Sent: 'Hello, TCP Server!'  
   # Received echo: 'Hello, TCP Server!'
```

   The server will print that it has been Connected by ('127.0.0.1', ...).  
4. **The Experiment:** Stop the server in the first terminal (Ctrl+C).  
5. Run the client again from the second terminal.

```bash
   python tcp-client.py  
   # Expected output:  
   # Traceback (most recent call last):  
   #   ...  
   # ConnectionRefusedError: \[Errno 61\] Connection refused
```

### **Observation & Key Takeaway TCP**

This demonstrates that **TCP is connection-oriented**. A stable connection must be established before any data transfer can occur.

## **Next Steps**

A great follow-up exercise is to use a packet analyzer like **Wireshark** to capture the traffic from the TCP activity. By filtering for tcp.port \== 12346, learners can visually identify the \[SYN\] \[SYN, ACK\] and \[ACK\] packets that make up the 3-way handshake.
