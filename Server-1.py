import sys
import  time
import socket


s = socket.socket()
host = socket.gethostname()
print("Server will start on",host)

port = 8080

s.bind((host,port))
print()
print("Server binding with host and port successfully.")
print("Server is waiting for incomming collections.")
s.listen(1)
conn, addr = s.accept()
print(addr,"Host connected to the sever...")

while 1:
    message = input("Enter your message: ")
    message = message.encode()
    conn.send(message)
    print("Message has been sent.")
    incomming_message = conn.recv(1024)
    incomming_message = incomming_message.decode()
    print(incomming_message)


