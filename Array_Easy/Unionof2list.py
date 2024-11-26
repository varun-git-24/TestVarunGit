a1 = [1,2,3,4,5,8,9]
a2 = [2,3,4,4,5,6,2,6,10]
#out = [1,2,3,4,5,6]


def union(i1, i2):
    out = []
    for item in i1:
        if item not in i2:
            out.append(item)
    for item in i2:
        if item not in out:
            out.append(item)

    out.sort()
    return out


print(union(a1,a2))