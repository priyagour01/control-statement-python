# Lambda:only ek time use karne ke liye banaya jata hai
# # syntex: lambda parameter:expression

# x = lambda p,q : p+q
# print(x(4,5))

# x = lambda p,q : print(p+q)
# x (4,5)

# x = lambda p,q : p-q
# print(x(4,5))

# x = lambda p,q : p*q
# print(x(4,5))

# x = lambda p,q : p/q
# print(x(4,5))

# x = lambda p,q : p//q
# print(x(4,5))

# x = lambda p,q : p%q
# print(x(4,5))

# l = [1,2,3,4,5,6]
# def squar_no(n):
#     return n**2
# print(list(map(lambda n: n**2,l)))
# ==== or ===

# l = [1,2,3,4,5,6]
# x = lambda n: n**2   # expression
# print(x(1))
# x = map(lambda n: n**2 , l)
# print(list(x))

# l1 = [1,2,3,4,5,6]
# l2 = [7,8,9,10,11,12]
# l3 = [2,4,6,8,10]

# x = map(lambda p,q,r : l1,l2,l3)
# print(list(x))
# print(list(map(lambda p,q,r :p+q+r, l1,l2,l3)))

# even num:
# l1 = [1,2,3,4,5]
# lambda n : n%2 ==0
# x = filter(lambda n :n%2==0 ,l1)
# print(list(x))

# odd
# l1 = [1,2,3,4,5]
# lambda n : n%2 ==0
# x = filter(lambda n :n%2!=0 ,l1)
# print(list(x))

# sum of number :
# l1 = [1,2,3,4,5]
# from functools import reduce
# p = reduce(lambda x,y:x+y,l1)
# print(p)

# if else lambda:
# syntex : lambda variable : if-result if condition else---else result
# lambda x,y:[x if x>y else y]

# p = lambda x,y:[x if x>y else y]
# print(p(10,20))
# print(list (p(10,20)))

# higher order function
# from functools import reduce
# sum :
# l = [1,2,3,4,5,6,7]
# p = reduce(lambda x,y:x+y,l,10)
# print(p)

# max
# l = [1,2,3,4,5,6]
# p = reduce(lambda x,y:x if x>y else y,l)
# print(p)

# # min
# l = [1,2,3,4,5,6]
# p =reduce (lambda x,y:x if x<y else y,l)
# print(p)

# map , filter ,reduce three methods se

# from functools import reduce
# l = [8,4,6,2,9,1,7,5]
# def add5(n):
#     return(n+1)
# def greater5(n):
#     if n>=5:
#         return n
# x = filter(greater5,list(map(add5,l)))
# def total_sum(x,y):
#     return x+y
# x = reduce(total_sum,list(filter(greater5,l)))
# print(x)    


from functools import reduce
l = [8,4,6,2,9,1,7,5]
def add5(n)
