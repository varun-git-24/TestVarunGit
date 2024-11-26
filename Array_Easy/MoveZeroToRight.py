#zero = [1, 0, 0, 8, 0, 10, 1, 0, 100, 0, 90000000, 10]


# zero = [1,1,0,0,1,1,0,0,0,1,1]
#
# def moveZerotoRight(test):
    #firstZero = 0
    # for i in range(len(test)):
    #     if test[i] == 0:
    #         firstZero = i
    #         break
    #
    # for j in range(firstZero+1, len(test)):
    #     if test[j] != test[firstZero]:
    #         test[firstZero], test[j] = test[j], test[firstZero]
    #         firstZero = firstZero + 1

# def moveZeroToLeft(test):
#     firstZero = 0
#     for i in range(len(test)-1,0,-1):
#         if test[i] == 0:
#             firstZero = i
#             break
#
#     for j in range(firstZero - 1, -1,-1):
#         if test[j] != test[firstZero]:
#             test[firstZero], test[j] = test[j], test[firstZero]
#             firstZero = firstZero -1
#
#     return test
#
#
# print(moveZerotoRight(zero))






















i = [0,0,0,0,0,1,0,1,1,0,1,0,0,1,0,1,0,0,0]

def brute_one(inp_list):
    list_others = []
    list_one = []
    for item in inp_list:
        if item == 1:
            list_one.append(item)
        else:
            list_others.append(item)

    #print(list_others.extend(list_one))

    list_others.extend(list_one)
    return list_others


print(brute_one(i))

# def moving_zero_to_right(data):
#     first = 0
#     for one in range(0,len(data)):
#         if data[one] == 1:
#             first = one
#             break
#
#     for swap in range(first+1, len(data)):
#         if data[swap] != data[first]:
#             data[swap] , data[first] = data[first] ,data[swap]
#             first = first + 1
#
#     return data
#
#
# print(moving_zero_to_right(i))


