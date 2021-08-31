from time import sleep
from threading import Thread
import socket


s = ('localhost' , 1818)

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server.bind(s)

server.listen(5)

con , addr = server.accept()


def send_data():
    while True:
        data_send = input('>> ')
        con.send(data_send.encode())
        sleep(5)


def recv_data():
    while True:
        data_recv = con.recv(1024)
        print(data_recv.decode())
        sleep(5)
    
    
send_data_threading = Thread(target=send_data)
recv_data_threading = Thread(target=recv_data)


send_data_threading.start()
recv_data_threading.start()