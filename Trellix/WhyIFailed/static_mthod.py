# class StaticMethod:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @staticmethod
#     def add(a,b):
#         return a + b
#
#     def sub(self):
#         if self.a > self.b:
#             return self.a - self.b
#
# print(StaticMethod.add(3,4))
# obj = StaticMethod(7, 3)
# print(obj.sub())


# def generatePascalTriangle(N):
#     out = [ [] for i in range(N)]
#     for i in range(N):
#         for j in range(i+1):
#             if j<i:
#                 if j==0:
#                     out[i].append(1)
#                 else:
#                     out[i].append(out[i-1][j]+out[i-1][j-1])
#             elif i==j:
#                 out[i].append(1)
#
#     print("Generated Pascals Triangle: ",out)
# generatePascalTriangle(5)



def find_pairs_with_sum(inputList,sum):
    seen=set()
    for no in inputList:
        complement=sum-no
        if complement in seen:
            print(f"Pairs: {no},{complement}")
        seen.add(complement)

