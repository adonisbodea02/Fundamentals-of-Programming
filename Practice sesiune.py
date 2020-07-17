from texttable import Texttable

# def bigger(x, y):
#     print(locals())
#     return x > y
#
# x = 1065467
# y = 23
#
# class Mama:
#     def __init__(self):
#         self.PAR = "MAMA"
#
# print(2**8 is 2**8)
# print(2**9 is 2**9)
#
# print(id(x))
# print(id(Mama))
# print(id(bigger))
# print(bigger(x,y))
#
# class A:
#     def f(self, l,nr):
#         l.append(nr)
# class B:
#     def g(self, l, nr):
#         nr = nr-1
#         l = l + [-2]
# a = A()
# b = B()
# l = [1,2]
# c = -1
# a.f(l,6)
# b.g(l,c)
# print(l,c)
# print(2**64/31536000)
#
# # def mycmp(a, b):
# #     res = cmp(a[0], b[0])
# #     if res == 0:
# #         return cmp(a[1], b[1])
# #     return -res
#
# List = [[1,"Alex"], [6,"Colhon"], [6,"Ion"], [5,"Vanessa"]]
# #List.sort(cmp=mycmp(), key=lambda x: (x[0], x[1])
# #List.sort(key = lambda x: (-x[0], x[1]), reverse=True)
# #List.sort(key = lambda x:(x[0], -x[2]))
# print(List)
#
#
# # a = lambda x: [x+1]
# # b = a(1)
# # c = lambda x: x + b
# # d = c([1])
# # a = 1
# # b = 3
# # print (a, b, c(4), d[1])
#
# def isPrime(n):
#
#     if n == 2:
#         return True
#     if n == 3:
#         return True
#     if n == 1:
#         return False
#     if n == 4 :
#         return False
#
#     for i in range(2, n//2):
#         if n % i == 0:
#             return False
#     return True
#
# def prime_pos(lst):
#
#
#     if len(lst) == 1:
#         return 0
#
#     if isPrime(len(lst)-1):
#         return lst[-1] + prime_pos(lst[:len(lst)-1])
#
#
#     return prime_pos(lst[:len(lst)-1])
#
# def test_prime():
#     lst = [9,3,3,8,7,7,4,3]
#     print(prime_pos(lst))
#
# test_prime()
#
# boardtable = Texttable()
# boardtable.add_rows([[21 for x in range(2)] for y in range(4)], [])
# print(boardtable.draw())
#
# def f(a, b, c):
#     a = a + 1
#     b.append(3)
#     c = c + [3]
# a = 7
# b = [1, 2]
# c = [1, 2]
# f(a, b, c)
# print(a, b, c)
#
# a, b = 1, 2
# l = [a, b]
# a = 7
# l2 = [a]
# l.append(l2)
# l2[0] = 8
# print(a, l2, l)

def f():
    return 1
def g(x=1):
    return x + 1
def h(x=1, y=2):
    return x + y
l = [f, g, h]
for e in l:
    print(e())
h = lambda x = 1, y = 2: x * y
print(l[2](3), h(), h(3), h(x=3), h(y=3))
print(h([2, 3]))
print(h(*[2, 3]))


