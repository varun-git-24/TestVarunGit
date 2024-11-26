my_array = [23,45,67,90,100]


def find_largest(arr):
    lar = 0
    for ele in arr:
        if ele > lar:
            lar = ele

    return lar


print(find_largest(my_array))