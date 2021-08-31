import socket

c = ('localhost' , 1818)

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

client.connect(c)

while True:
    data = client.recv(1024)
    if data == None:
        quit()
    print(data.decode())
