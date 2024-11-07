
def checkIsoMorphicString(inputString1,inputString2):
    s1_l =[]
    s2_l = []
    for ele in inputString1:
        s1_l.append(inputString1.index(ele))
    for ele in inputString2:
        s2_l.append(inputString2.index(ele))
    if s1_l==s2_l:
        print(f"{inputString1} and {inputString2} are ISOMORPHIC")
    else:
        print ( f"{inputString1} and {inputString2} are NOT ISOMORPHIC" )

checkIsoMorphicString("egg","hii")


l1 = [1,2]
l2 = [3,4]

l1.extend(l2)
print(l1)