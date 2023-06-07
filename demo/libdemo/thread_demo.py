import threading
from threading import Thread

print(threading.current_thread())


class ChildThread(Thread):
    def run(self):
        for i in range(1, 11):
            print(f'Child : {i}')


ct = ChildThread()
ct.start()

for i in range(1, 11):
    print(f'Main : {i}')
