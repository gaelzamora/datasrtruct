# Dado 2 arreglos retornar los 2 grandes de cada uno en lista
# [1,4,6,7,9]
# [4,5,10]


'''
def powerFunction(num, n):
    res = 1
    if n == 0: return 0
    for i in range(n): 
        res *= num
    return res

print(powerFunction(4,3))
'''


def twoArrayBig(list1, list2):
    return [[list1[-1], list1[-2]],[list2[-1], list2[-2]]]


list1 = [1,4,6,7,9]
list2 = [4,5,10]

print(twoArrayBig(list1, list2))