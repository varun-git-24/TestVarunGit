my_array = [23,45,67,90,100,110]


def find_second_largest(arr):
    first_largest = 0
    second_largest = -1
    for i in arr:
        if i > first_largest:
            first_largest = i

    for j in arr:
        if j > second_largest and j != first_largest:
            second_largest = j

    return second_largest


print(find_second_largest(my_array))