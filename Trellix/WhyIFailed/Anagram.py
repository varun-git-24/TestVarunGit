x = 'CAT'
y = 'MAT'

def anagram(s1,s2):
    if len(s1) != len(s2):
        return False

    l = []
    for item in s1:
        if item not in s2:
            l.append(item)

    return len(l)

ln = anagram(x,y)
if ln == 0:
    print('Anagram')
else:
    print('Not Anagram')