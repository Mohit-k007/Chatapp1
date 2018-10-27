import socket

s = socket.socket()
host = input(str("Please input the hostname of the server:"))
port = 8080
s.connect((host, port))
print("Connected to the chat server")
while 1:
    incoming_msg = s.recv(1024)
    incoming_msg = incoming_msg.decode()
    print("server:", incoming_msg)
    message = input(str(">>"))
    message = message.encode()
    s.send(message)
    print("Message sent")