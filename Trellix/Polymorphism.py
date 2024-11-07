# Method over-riding
# class Car:
#     def __init__(self, country):
#         self.country = country
#
#     def quality(self):
#         print('This is a car')
#
#
# class Mercedes(Car):
#
#     def quality(self):
#         print(f'The Most Luxurious of {self.country} ')
#
#
# class Buggatti(Car):
#     def quality(self):
#         print('The fastest')
#
#
# class Audi(Car):
#     def quality(self):
#         print('The most good looking')
#
#
# car_obj_m = Mercedes('German')
# car_obj_m.quality()

# Duck_Typig----No need of super class or inheritance
class Buggatti:
    def quality(self):
        print('The fastest')
        return ""


class Audi:
    def quality(self):
        print('The most good looking')
        return ""

def duck_function(car):    #car is like object of buggatti or Audi class
    print(car.quality())


bugatti = Buggatti()
audi = Audi()

duck_function(audi)  ### === bugatti.quality()


#overloading ------ Not supported in python

class overloading:
    def method1(self , a=None , b=None):
        if a!= None and b!= None:
            return a + b
        else:
            return a


