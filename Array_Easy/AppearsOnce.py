one = [2,2,1] #op = 1
two = [4,1,2,1,2] # op = 4
three = [2,3,4,2,3,4,6]
#Brute Force
def appearsOnce(inp):
    count = 0
    d = {}
    for item in inp:
        count = inp.count(item)
        d[item] = count

    for val in d:
        if d[val] == 1:
            return f'Ele which appears once is : {val}'
        else:
            continue
#
#EfficientCode

# def appearsOnce(inp):
#     sample = []
#     for item in inp:
#         if item not in sample:
#             sample.append(item)
#         else:
#             sample.remove(item)
#
#     if len(sample) == 0:
#         return 'No ele'
#     else:
#         for ele in sample:
#             return ele
# #
#
# th = [1,1]
# print(appearsOnce(th))










##############PRactice
s = [1,9,1,0,2,3,0,4,5]
y = ['2','2']
# s.remove(3)
# print(s)

d = {'s':1 , 't':2 , 'u':3}
for i in d.items():
    print(i)


print('x'.join(y))


















# three1 = [2,3,4,2,3,4,6]
#
# def appears(inp):
#     count = 0
#     my_dict = {}
#     for item in inp:
#         count = inp.count(item)
#         my_dict[item] = count
#
#     print(my_dict)
#
#     for key in my_dict:
#         if my_dict[key] == 1:
#             return key
#
#         continue
#
# print(appears(three1))