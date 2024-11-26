my_array1 = [23, 45, 67, 90, 120, 110]
my_array2 = [0,1]


def rev(arr):
    mid = len(arr)//2
    n = len(arr)
    for i in range(0,mid):
        arr[i] , arr[n-i-1] = arr[n-i-1] , arr[i]

    return arr

print(rev(my_array1))


# def lasttwoswap(arr):
#     # temp = arr[len(arr)-1]
#     # arr[len(arr) - 1] = arr[len(arr)-2]
#     # arr[len(arr)-2] = temp
#
#     arr[len(arr) - 1] , arr[len(arr) - 2] = arr[len(arr) - 2] , arr[len(arr)-1]
#
#     return arr
#
# print(lasttwoswap(my_array1))


def sorted_array(input_array):
    i = 0
    for j in range(1, len(input_array)):
        if input_array[j] < input_array[i]:
            return False
        i = i +1
            #continue
        # else:
        #     return False
    return True

print(sorted_array(my_array2))

