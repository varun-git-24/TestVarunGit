myarray = [-1,1,1]
summ = 1  # [1,2,3,6]
l = 8




# def longestSubarray(input_a, s):
#     length = 0
#     for i in range(0, len(input_a)):
#         sum = 0
#         for j in range(i, len(input_a)):
#             sum = sum + input_a[j]
#             if sum == s:
#                 length = max(length, j - i + 1)
#
#     return length
#
#
# print(longestSubarray(myarray, summ))


# x = [1,2,3,'HI',4]
# y = []
# for item in x:
#     if isinstance(item,str):
#         for i in item:
#             y.append(i)
#     else:
#         y.append(item)
# print(y)

import json
# d = {
#     "key1": {
#         "key2": {
#             "key3": [
#                 {
#                     "subkey1": {
#                         "s": ["Mukulare Varun",1,2,3]
#                     }
#                 },
# {
#                     "subkey1": {
#                         "s": ["Mukulare Sachi"]
#                     }
#                 },
# {
#                     "subkey1": {
#                         "s": ["Mukulare Sanj",1,1,1,1,1,1,1,0]
#                     }
#                 }
#
#             ]
#         }
#     }
# }
# # Pretty-print the JSON
# # formatted_json = json.dumps(d, indent=4)
# # print(formatted_json)
# k = []
# for i in range(0,len(d['key1']['key2']['key3'])):
#     for j in range(0,len(d['key1']['key2']['key3'][i]['subkey1']['s'])):
#         k.append(d['key1']['key2']['key3'][i]['subkey1']['s'][j])
#         #k.append(d['key1']['key2']['key3'][i]['subkey1']['s'][j]))
#
# print(k)

matrix = [[1,2,3] ,
          [4,5,6],
          [7,8,9]]
#0,2  1,1  2,0
sum = 0
# for i in range(0,len(matrix)):
#     for j in range(0,len(matrix[i])):
#         # if i == j:
#         #     sum= sum + matrix[i][j]
#
#         print(matrix[i][len(matrix[i])-1-i])


def subArraySum(arr, target):
    i = 0
    sum = 0
    res = []
    for j in range(i, len(arr)):
        sum = sum + arr[j]
        if sum == target:
            res = [i, j]
            return res

        if j == len(arr) - 1:
            i = i + 1
            sum = 0


print(subArraySum([1,2,3,4,5] , 9))