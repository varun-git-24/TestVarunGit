
def try_catch_except(a ,b):
    try:
        y = a/ b
        print(y)
    except ZeroDivisionError:
        print('Ur input should not be 0')



print(try_catch_except(2, 2))

x = lambda x, y: x + y
print(x(2, 3))
