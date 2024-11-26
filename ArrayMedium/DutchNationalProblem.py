x = [1, 0, 1, 0, 2, 2, 0, 2, 0]


def dutch_national(a):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for item in a:
        if item == 0:
            count_0 += 1
        elif item == 1:
            count_1 += 1
        else:
            count_2 += 1

    print(count_0,count_1,count_2)

    for zero in range(count_0):
        a[zero] = 0
    for one in range(count_0,count_0+count_1):
        a[one] = 1
    for two in range(count_1+count_0 , len(a)):
        a[two] = 2

    return a

print(dutch_national(x))