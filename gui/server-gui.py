from time import sleep
from tkinter import *
from threading import Thread
import socket
from win32api import GetSystemMetrics

s = ('localhost', 1818)
server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(s)
server.listen(5)
con , addr = server.accept()


def send_data():
    data_send = message.get()
    if data_send != '':
        con.send(data_send.encode())
        label = Label(frame, text=data_send, bg='red', fg='white', borderwidth=2, relief='ridge')
        label.pack(fill=X, side=TOP)
        message.delete(0, END)


def recv_data():
    while True:
        data_recv = con.recv(1024)
        if data_recv != '':
            label = Label(frame, text=data_recv, bg='blue', fg='white', borderwidth=2, relief='ridge')
            label.pack(fill=X, side=TOP)


def quit_chat():
    con.close()
    root.destroy()
    quit()


def update_scroll():
    while True:
        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scrollbar.set)
        sleep(2)


root = Tk()

canvas = Canvas(root)
scrollbar = Scrollbar(root, orient='vertical', command=canvas.yview)
frame = Frame(root)

root.iconbitmap('icon/file_tga.ico')
root.title('Chat server')
root.geometry(f'400x{GetSystemMetrics(1)-200}')
root.resizable(False, False)

quit_btn = Button(root, text='quit', command=quit_chat)
send_btn = Button(root, text='send', command=send_data)
message = Entry(root)

quit_btn.pack(fill=X, side=BOTTOM)
send_btn.pack(fill=X, side=BOTTOM)
message.pack(fill=X, side=BOTTOM)

canvas.pack(fill=BOTH, side=LEFT, expand=True)
scrollbar.pack(fill=Y, side=RIGHT)
canvas.create_window(0, 0, window=frame, anchor='nw')
canvas.update_idletasks()


update_scroll_thread = Thread(target=update_scroll)
get_recv_data = Thread(target=recv_data)
update_scroll_thread.start()
get_recv_data.start()


root.mainloop()