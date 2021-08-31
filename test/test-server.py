import socket

s = ('localhost' , 1818)

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server.bind(s)

server.listen(2)

con , addr = server.accept()

while True:
    send_data = input('>> ')
    con.send(send_data.encode())
