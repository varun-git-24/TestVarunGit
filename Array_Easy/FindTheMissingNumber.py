missing = [1,2,3,5]
#l = 5

def missingNum(data  , l):
    temp_sum1 = l * (l+1) // 2
    temp_sum2 = 0
    for ele in data:
        temp_sum2 = temp_sum2 + ele

    return temp_sum1 - temp_sum2

print('Missing Num is : ' , missingNum(missing,5))
