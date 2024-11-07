# def argsss(*hi, **kwargs):
#     for item in hi:
#         print(item)
#
#     for key, value in kwargs.items():
#         print('These are kwargs', {key: value})
#
#
# argsss(10, 'HI', even='10', odd='5')


#print(5^2)

a = 10
a = 11

# l = ['A','N','U','S','H','A']
# l[2] = 'R'
# print(l)
#
# d = {'a':1,'b':2,'c':3}
# d['a']=2
# print(d['a'])
#
# s = 'ANUSHA'
# s[2] = 'R'
# print(s)

#
# l = [1,2,3,4,1,1,2]
# def second_max(inp):
#     temp_dict = {}
#     first_max = 0
#     second_max = 0
#     for item in inp:
#         count = inp.count(item)
#         temp_dict[item] = count
#     print(temp_dict)
#
#     for val in temp_dict:
#         if temp_dict[val] > first_max:
#             first_max = temp_dict[val]
#     print(first_max)
#
#     for val in temp_dict:
#         if temp_dict[val] > second_max and temp_dict[val] != first_max:
#             second_max = temp_dict[val]
#             return f'Second max is {val} , repatig {second_max} no of times'
#
# print(second_max(l))























# def ispomorphic(s1 , s2):
#     list_1 = []
#     list_2 = []
#     for i in s1:
#         list_1.append(s1.count(i))
#     for j in s2:
#         list_2.append(s2.count(j))
#
#     return list_1 , list_2
#
# a = "title"
# b = "paper"
# print(ispomorphic(a,b))

# def palin(n):
#     org = n
#     temp = 0
#
#     while n > 0:
#         d = n % 10
#         temp = temp * 10 + d
#         n = n // 10
#
#     if org == temp:
#         return 'palindrome'
#     else:
#         return 'not palindrome'
#
# print(palin(12321))


#fibonacci
def fibo(n):
    start = [0,1]
    x = len(start)
    # print("=======",start[n-1] + start[n-2])

    while x < n:
        start.append(start[-1]+start[-2])
        x += 1

    return start[:n]

print(fibo(10))

def gen(n):
    a , b = 0 , 1
    for i in range(n):
        yield i
        a , b = b , a + b

px = gen(5)
print(next(px))

x = [1,2,3,4,4]
dict = {}
for ele in x:
    dict[ele] = dict.get(ele,0) + 1
print(dict)

print(dict.get(5,'NOe exist'))