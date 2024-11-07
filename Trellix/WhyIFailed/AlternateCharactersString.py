x = 'Varun'
y = 'Anusha'

n = [1,2,3,4,5]
o = [10,11,12,13]
def alternate(in1 , in2):
    a = len(in1)
    b = len(in2)
    x = []

    def helper(length):
        for item in range(length):
            x.append(in1[item])
            x.append(in2[item])

    if a == b:
        #for item in range(a):
        helper(a)
            # x.append(in1[item])
            # x.append(in2[item])
    if a < b:
        helper(a)
        for item in range(a,b):
            x.append(in2[item])
    if a > b:
        helper(b)
        for item in range(b,a):
            x.append(in1[item])
    return x

print(alternate(n,o))





