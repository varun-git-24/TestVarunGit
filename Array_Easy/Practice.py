

a = [1,2,1,3,7,6,5,10,9,8]

# def sorting(x , i , j):
#     j = 0
#     for i in range(1,len(x)):
#         if x[i] > x[j]:
#             j = j+1
#         elif x[i] < x[j]:
#             x[j], x[i] = x[i], x[j]
#             j = j + 1



for i in range(0,len(a)):
    s = 0
    for j in range(i,len(a)):
        s = s + a[j]
        print(i,j)
    print(s)
