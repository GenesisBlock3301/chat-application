import sys
import  time
import socket


s = socket.socket()
host = input("Enter your host name: ")
port = 8080
s.connect((host,port))
print("Connect chat server sucessfully.")
while 1:
    incomming_message = s.recv(1024)
    incomming_message = incomming_message.decode()
    print(incomming_message)
    message = input("Enter your message: ")
    message = message.encode()
    s.send(message)
    print("Message has been sent.")

