class Python:
    c_v = 10

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def test(self):
        self.b = 20
        return self.a + self.b

    def add(self):
        return self.a + self.b

    def mul(self,c):
        self.c = c
        return self.b * self.c

    def div(self):
        return self.b % Python.c_v

    @staticmethod
    def this_is_static(x,y): ##Always inside the class
        return x*y



ob1 = Python(2,6)
print(ob1.b)
print(ob1.test())
print(ob1.b)
print(ob1.add())

#
ob2 = Python(8,2)
print(ob2.b)
# print(ob2.add())
# print(ob2.test())

# print(ob2.mul(2))
# ob2.b = 22
# print(ob2.mul(2))
#
#
# print(ob2.div())
#
#
# print(Python.this_is_static(7,y=


# x = 10
# y = x #y = 10
# s = x+y-x
#
#
# print(id(x))
# print(id(y))
# print(id(s))

x = 'a'
y = x.join(['x1', 'x2','8'])
print(y)



# def arguments(**x):
#     for k,v in x.items():
#         print(f'This is key = {k} , THis is val = {v}')
#
#     return [val+10 for key , val in x.items()]
#
# print(arguments(x=10 , y=20, z=30))


x = [1,2,3,4,5]
def demo(i):
    for item in i :
        if item == 7:
            print('Yes')
            break
    return 'NO'

demo(x)



x = None
x = f'Hi'
print()