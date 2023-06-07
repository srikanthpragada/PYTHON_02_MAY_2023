import threading
from threading import Thread

print(threading.current_thread())


def print_numbers():
    for i in range(1, 11):
        print(f'Child : {i}')


ct = Thread(target=print_numbers)
ct.start()

for i in range(1, 11):
    print(f'Main : {i}')
