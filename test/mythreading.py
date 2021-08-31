from threading import Thread
import time

def hello():
    while True:
        print("hello")
        time.sleep(1)

def goodbye():
    while True:
        print("goodbye")
        time.sleep(1)

thread1 = Thread(target=hello)
thread2 = Thread(target=goodbye)

thread1.start()
thread2.start()

