# client.py

import socket

Server_ip = "localhost"
Server_host = 8002
FORMAT = "utf-8"

# Create client socket
CS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CS.connect((Server_ip, Server_host))

# Open and read file
file = open("data/abc.txt", "r")
data = file.read()
file.close()

# Send filename
CS.send("abc.txt".encode(FORMAT))
msg = CS.recv(1024)
print(msg.decode(FORMAT))

# Send file data
CS.send(data.encode(FORMAT))
msg = CS.recv(1024)
print(msg.decode(FORMAT))

# Close socket
CS.close()

print("[*] Client process complete. Connection closed.")
