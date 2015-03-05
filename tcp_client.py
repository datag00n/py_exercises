import socket

target_host = "localhost"
target_port = 9998

#create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
client.connect((target_host,target_port))

#send some data
#HTTP
#client.send("\nGET / HTTP/1.1\r\nHost: datagoon.com\r\n\r\n")
client.send("SYN")

#receive some data
response = client.recv(4096)

print response
