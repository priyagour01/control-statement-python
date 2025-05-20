# filter: <ya = 
# syntex: filtr(function name , collection)

# even no
# l = [1,2,3,4,5,6,7,8,9,10]
# def even_no(n):
#     if n % 2 == 0:
#         return n
# x = filter(even_no ,l)
# print(x)
# print(list(x))

# odd
# l = [1,2,3,4,5,6,7,8,9,10]
# def even_no(n):
#     if n % 2 != 0:
#         return n
# x = filter(even_no ,l)
# print(x)
# print(list(x)) 


# l = [2,3,5,10,20,15,13,14,17]
# def greater5(n):
#     if n>=5:
#         return n
# x = filter(greater5,l)
# print(list(x))    

# l = [1,2,3,4,5,6,7,8,9,10]
# l1 = []
# for i in l:
#     if i>=5:
#         l1.append(i)
# print(l1)        


# reduce() method:
# syntex:1)
# import functools 
# functools.reduce(fun-name , collection)
# from functools import reduce
# reduce(fun.name , collection)

# from functools import reduce
# l = [8,4,6,5,7,2,9,1]
# # def max_no(x,y):
# def min_no(x,y):
#     # if x>y:
#     if x<y:
#         return x
#     else:
#         return y
# # x = reduce(max_no,l) 
# x = reduce(min_no,l) 
# print(x)   

# from functools import reduce
# l = [8,4,6,5,7,2,9,1]
# max_digit = l[0]


# from functools import reduce
# l = [8,4,6,5,7,2,9,1]
# def total_sum(x , y):
#     return x+y
# x = reduce(total_sum , l)
# print(x)

from functools import reduce
l = [1,2,3,4,5]
l1 = [6,7,8,9,10]
def total_sum(x,y):
    return x+y
def add1_sum(x):
    return x+1
x = reduce(total_sum,list(map(add1_sum,l)))
print(x)



