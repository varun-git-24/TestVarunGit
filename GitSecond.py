import time

i = 0
while i < 10:
    print(i)
    time.sleep(1)
    print('Written in Remote Repo')
    i = i + 1

print('This is written after creating slave branch')