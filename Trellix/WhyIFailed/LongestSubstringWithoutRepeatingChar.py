# x = 'ab'
#
# def longest_substring(input_string):
#     i = 0
#     count = 1
#     max_count = 0
#     for j in range(i+1,len(input_string)):
#         if input_string[j] != input_string[i]:
#             count = count +1
#             max_count = max(max_count,count)
#         else:
#             count = 1
#             i = j
#
#     return max_count
#
# print(longest_substring(x))

l = [0, 1, 2, 3, 4, 5, 6]
d = 3
# out = [3,4,5,6,0,1,2]
# [2,1,0]
# [6,5,4,3]
# [2,1,0,6,5,4,3]
# [3,4,5,6,0,1,2]

def right_rotate(input_list , no_of_places):
    def rev(i,s,e):
        for k in range(s, e): #k = 3,4,5,6
            if k >= e:
                break
            i[k], i[e-1] = i[e-1], i[k]  #3,6 and 4,5
            e = e-1
    rev(input_list,0,no_of_places)
    rev(input_list,no_of_places,len(input_list))
    rev(input_list,0,len(input_list))

    return input_list
#
print(right_rotate(l,d))





