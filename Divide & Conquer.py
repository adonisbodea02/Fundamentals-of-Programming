"""
1. Divide
2. Conquer
3. Combine

Merge sort and Quick - how they work with this method
Merge - works a lot on Combine
Quick - works a lot on Divide

The sum of the numbers of even positions - chip and conquer
"""
def chipandconquer(List, i, f):

    l = len(List)

    s = 0

    if i <= l:
        s = f + List[i]

    if i > l:
        return 0

    return s + chipandconquer(List, i + 2, s) - f

def divide(List):
    if len(List) == 1:
        return List[0]
    m = 0
    if len(List)%2 == 0:
        m = len(List)//2
    else:
        m = len(List) // 2 + 1
    print(List[:m:2])
    print(List[m::2])
    return divide(List[:m:2]) + divide(List[m::2])

def rad(n, r, p, left, right):
    m = (left + right) / 2
    if abs(m**r - n) < p:
        return m
    if m **r < n:
        return rad(n, r, p, m, right)
    else:
        return rad(n, r, p, left, m)

List = [1, 5, -1, 6, 2, 7, 9, 11, 12]
#print(chipandconquer(List, 0, 0))
print(divide(List))
print(rad(2,10,0.01,1,2))


