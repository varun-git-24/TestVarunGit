
s = 'Varuna'

def reveresed(i):
    new = ''
    for j in range(len(i)-1,-1,-1):
        new = new + i[j]

    return new

print(reveresed(s))