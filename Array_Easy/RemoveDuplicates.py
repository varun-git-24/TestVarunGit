my_array1 = [23, 45, 67, 90, 100, 100, 110, 110]
#ans = 6

def RemoveDuplicates(input_arr):
    i = 0
    for j in range(1, len(input_arr)):
        if input_arr[j] != input_arr[i]:
            input_arr[i+1] = input_arr[j]
            i += 1

    return i+1


print(f"lenght or original list == {len(my_array1)}")
print(f"Length of uniqure list == {RemoveDuplicates(my_array1)}")