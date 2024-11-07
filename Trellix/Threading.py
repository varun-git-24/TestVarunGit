import threading
import os


def my_thread1(a, b):
    print('This is my first process : ', a + b,
          f' > THe process ID is {os.getpid()} and current thread is {threading.current_thread().name}')


def my_thread2(a, b):
    print('This is my second process : ', a * b,
          f' > THe process ID is {os.getpid()} and current thread is {format(threading.current_thread().name)}')


def main_func():
    print(os.getpid())


t1 = threading.Thread(target=my_thread1, args=[8,0], name='T1-----')
t2 = threading.Thread(target=my_thread2, args=[10, 10], name='T2-----')

t1.start()
t2.start()

t1.join()
t2.join()

main_func()


l = [[1,2,3] ,5 ,7]
x = [1,2,3]
h = isinstance(x,tuple)
print(h)
