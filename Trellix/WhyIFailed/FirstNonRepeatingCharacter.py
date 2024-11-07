

name1 = 'Varun'
name2 = 'anusha'

# def non_repeating(s):
#     ref_dict={}
#     count = 0
#     for item in s:
#         count = s.count(item)
#         ref_dict[item] = count
#
#     print(ref_dict)
#     for c in s:
#         if ref_dict[c] == 1:
#             return c
#     return None
#
# print(non_repeating(name2))

d = {1:3,2:4}
print(d.values())



x = [1,2,1,3,4,1]
y = set()
for item in x:
    y.add(item)

print(y)

def checkIsoMorphicString(inputString1,inputString2):
    s1_l =[]
    s2_l=[]
    for ele in inputString1:
        s1_l.append(inputString1.index(ele))
    for ele in inputString2:
        s2_l.append(inputString2.index(ele))
    if s1_l==s2_l:
        print(f"{inputString1} and {inputString2} are ISOMORPHIC")
    else:
        print ( f"{inputString1} and {inputString2} are NOT ISOMORPHIC" )
checkIsoMorphicString("title","paper")


s1="ravi"
s2="teja"

s3=""
for i in range(len(s1)):
    s3[i]=s1[i]
    s3[i+1]=s2[i]
print(s3)