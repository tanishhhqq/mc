# server.py

import socket

Server_ip = "localhost"
Server_host = 8002
FORMAT = "utf-8"

# Create server socket
SS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SS.bind((Server_ip, Server_host))
SS.listen(5)

print(f"[*] Server listening on {Server_ip}:{Server_host}...")

s1, addr = SS.accept()
print(f"[+] Connection accepted from {addr}")

# Receive file name
file_name = s1.recv(1024).decode(FORMAT)
print(f"[+] File name received: {file_name}")

file = open(file_name, "w")

s1.send("File name received".encode(FORMAT))

# Receive file data
data = s1.recv(1024).decode(FORMAT)
print("[+] File data received")

s1.send("File data received".encode(FORMAT))

# Write data into file and close
file.write(data)
file.close()

# Close sockets
s1.close()
SS.close()

print("[*] Server process complete. Connection closed.")
