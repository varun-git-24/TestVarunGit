def my_decorator(func):
    def wrapper(a,b,c):
        #func(a, b, c)
        print('This is wrapper start')
        if a%2 == 0 and b%2 == 0:
            print(f'{a,b} - Is Even')
        else:
            func(a, b, c)
            print(f'{a,b} - Is odd')

        print('This is wrapper stop')

    return wrapper


@my_decorator
def main_method(a,b,c):
    print('This is main method modified using decorators' , a + b + c)

@my_decorator
def main2_method(a,b,c):
    print('This is second main method' , a + b + c)

main_method(1,3,8)
print('----------------------------------')
#main2_method(2,4,8)