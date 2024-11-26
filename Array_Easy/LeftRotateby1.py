my_array1 = [23, 45, 67, 90, 100, 110]

#my_a = [45 , 67 , 90 , 100 , 110 , 23]


def LeftRotate(input_array):
    n = len(input_array)
    temp = input_array[0]
    for j in range(1, len(input_array)):
        input_array[j-1] = input_array[j]

    input_array[n-1] = temp

    return input_array



print(LeftRotate(my_array1))