from tkinter import *
from win32api import GetSystemMetrics
from time import sleep


def get_entry_data():
    data = get_text.get()
    lbl = Label(root, text=data, bg='blue', fg='white', borderwidth=2, relief='ridge')
    lbl.pack(fill=X, side=TOP)
    get_text.delete(0, END)


root = Tk()

root.iconbitmap('icon/file_tga.ico')

root.title('py-messenger')

root.geometry(f'400x{GetSystemMetrics(0)-800}')

root.resizable(False, False)


lbl = Label(root, text='Hello . Wellcome to py messenger', bg='blue', fg='white', borderwidth=2, relief='ridge')
lbl.pack(fill=X, side=TOP)

btn = Button(root, text='Click', command=get_entry_data)
btn.pack(fill=X, side=BOTTOM)

get_text = Entry(root)
get_text.pack(fill=X, side=BOTTOM)


root.mainloop()