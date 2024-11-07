# -------------------------------- Class Variable
# class Just:
#     class_variable = 10
#
#     def test(self):
#         pass
#
# obj1 = Just()
# print(obj1.class_variable)
# Just.class_variable = 20
# obj = Just()
# obj.class_variable = 30
# print(obj.class_variable)
#
# next_obj = Just()
# print(next_obj.class_variable)

# ------------------------------------Instance Variable

# class Okay:
#     def __init__(self, instance_var1 , instance_var2):
#         self.instance_var2 = instance_var2
#         self.instance_var1 = instance_var1
#
#     def ok_instance(self):
#         print(self.instance_var1)
#
#     def oks_instance(self):
#         print(self.instance_var2)
#
# my_instance = Okay(90,10)
# my_instance.ok_instance()
# my_instance.oks_instance()
#
# my_instance2 = Okay(80,'HI')
# my_instance2.ok_instance()


############## Local variable
y = 20
global x


def local_var(var_local):
    x = var_local + 2
    return x


print(local_var(10))
