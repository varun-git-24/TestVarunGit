given_input = [2, 3, 6, 8, 13]
s = 19  # out Yes and [1,4]
y = 12  # out No and [1,4]

###Brute
# def two_sum(input_data, sum):
#     index = []
#     for i in range(len(input_data)):
#         for j in range(i+1, len(input_data)):
#             if input_data[i] == input_data[j]:
#                 continue
#             if input_data[i] + input_data[j] == sum:
#                 index.extend([i, j])
#                 return f'Yes and {index}'
#
#     if not index:
#         return [-1,-1]

##Optimized
def two_sum(input_data, sum):
    index = []
    d = {}
    for i in range(len(input_data)):
        x = sum - input_data[i]
        if x not in d:
            d[input_data[i]] = i
        else:
            return d[x], i
    return None




print(two_sum(given_input, s))


