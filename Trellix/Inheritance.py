##########Single inheritance ####################
# class Parent:
#     def parent(self):
#         print('I am parent')
#
#
# class Child(Parent):
#     def child(self):
#         print('I am child')
#
#
# obj = Child()
# obj.parent()
# obj.child()


################ Multiple Inheritance ##############
# class Parent1:
#     def parent1(self):
#         print('I am parent1')
#
# class Parent2:
#     def parent2(self):
#         print('I am parent2')
#
# class Child(Parent1,Parent2):
#     def child(self):
#         print('I am child')
#
#
# obj = Child()
# obj.parent1()
# obj.parent2()
# obj.child()


############################# Multilevel Inheritance ##################################
# class Parent1:
#     def parent1(self):
#         print('I am parent1')
#
# class Parent2(Parent1):
#     def parent2(self):
#         print('I am parent2')
#
# class Child(Parent2):
#     def child(self):
#         print('I am child')
#
#
# obj = Child()
# obj.parent1()
# obj.parent2()
# obj.child()
#
# obj2 = Parent2()
# obj.parent1()
# obj2.parent2()

################################ Heirarchical ##################

# class Parent1:
#     def parent1(self):
#         print('I am parent1')
#
# class Child1(Parent1):
#     def child1(self):
#         print('I am child1')
#
# class Child2(Parent1):
#     def child2(self):
#         print('I am child2')
#
# obj = Child2()
# obj.child2()
#
# obj2 = Child1()
# obj2.parent1()

########################### Hybrid ################################

class Parent1:
    def parent1(self):
        print('I am parent1')

class Child1(Parent1):
    def child1(self):
        print('I am child1')

class Child:
    def child(self):
        print('I am just child , no inheritance')

class Child2(Parent1,Child):
    def child2(self):
        print('I am child2')

obj1 = Child2()
obj1.parent1()
obj1.child()
obj1.child2()

obj2 = Child1()
obj2.parent1()