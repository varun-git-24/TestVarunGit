one = [1,1,0,0,0,1,1,1,1,1,1,1,1,0,1,1,1,1]#out = 4
two = [1,0,1,1,1,1,1]#out = 3
three = [0]
f = [1,0,1,1]

def maxones(inp):
    temp_count = 0
    max_consecutive = 0
    for ele in inp:
        if ele == 1:
            temp_count = temp_count + 1
            max_consecutive = max(max_consecutive, temp_count)
        else:
            temp_count = 0




    return max_consecutive


print(maxones(one))