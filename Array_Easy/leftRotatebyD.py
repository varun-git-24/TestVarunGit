my_array1 = [23, 45, 67, 90, 100, 110]
#d=2 , = [67,90,100,110,23,45]
#d=3 , = [90,100,110,23,45,67]
#my_a = [45 , 67 , 90 , 100 , 110 , 23]
#my_a =
#right_rotateby3 = [90,100,110,23,45,67]

#right_rotateby2 = [100,110,23,45,67,90]

def RightRotate(input_array, d):
    n = len(input_array)
    d = d % n
    temp1 = []
    temp2 = []
    # for i in range(d):
    #     temp1.append(input_array[i])
    #
    # print(temp1)
    # # for j in range(0, n-d):
    # #     temp2.append(input_array[d+j])
    #
    # for j in range(d, n):
    #     temp2.append(input_array[j])
    #
    # print(temp2)
    #
    # return temp2 + temp1

    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1


    reverse(input_array, 0, n-d-1)
    reverse(input_array, n-d, n - 1)
    reverse(input_array, 0, n-1)

    return input_array
my_a = [1,2,3,4,5,6]
print(RightRotate(my_a,4))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# config_status = 'operational'
# print("============================== \n" + config_status + "\n========================================")