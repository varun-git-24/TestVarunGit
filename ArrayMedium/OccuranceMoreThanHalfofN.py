input_array = [1, 2, 3, 1, 2, 2, 2]


# n = 7 and n/2 = 3.5 , answer = 2


def count_half_of_lenght(data):
    N = len(data) // 2
    my_dict = {}
    for item in data:
        my_dict[item] = my_dict.get(item, 0) + 1

    for key, values in my_dict.items():
        if values > N:
            return key


print(count_half_of_lenght(input_array
                           ))
