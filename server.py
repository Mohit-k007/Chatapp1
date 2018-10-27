import socket

s = socket.socket()
host = socket.gethostname()
print("server will start on host:", host)
port = 8080
s.bind((host, port))
print("")
print("Server done binding to host and port successfully")
print("Server is waiting for incoming connection...")
s.listen(1)
conn, addr = s.accept()
print(addr, "has connected to the server and now online")
while 1:
    message = input(str(">>"))
    message = message.encode()
    conn.send(message)
    print("Message sent")
    incoming_msg = conn.recv(1024)
    incoming_msg = incoming_msg.decode()
    print("client:", incoming_msg)