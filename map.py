'''Map : Python me map() ek built-in function hai jo kisi function ko ek ya 
zyada iterables (jaise list, tuple) ke har element par apply karta hai.
#avoid same loop repettion
#write once call  multiple
#code resuablity

# type --- inbuilt , userdefined 
# inbuilt function = print(),type(),max(),min(),len()

# userdefined---declartion , calling 

# 1) DECLARTION
# syntex:
# def fun-name(parameters):
#     |used variable are decleared as aparameter,
#     |perform operation, return 
# fun_name(argumrnts)'''

# def hello():
    # return"  #" denge toh blank ayega ,return lekhenge toh none btayega, 
    # string likhenge toh string btayega print(hello()) 
    
# def hello():
#     print('hello')
# hello()    

# def hello():
#     print('hello')
# x = hello()
# print(x)

# def hello():
#     return 'hello'
# x = hello()
# print(x)

# Natural number
# def natural(n):
#     for i in range(1,n+1):
#         print(i)
# x = int(input("enter natural num:"))
# natural(x)     

#Even Number:
# def evenno(n):
#     for i in range(1,n+1):
#         if i % 2 ==0:
#             print(i)
# x = int(input("Enter even num:"))
# evenno(x)
 

# odd:
# def oddno(n):
#     for i in range(1,n+1):
#         if i % 2 !=0:
#             print(i)
# x = int(input("Enter even num:"))
# oddno(x)

# sum of natural number:
# def sumno(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum = sum+i
#     return sum
# n = int(input("enter sum of natural num"))
# totalsum = sumno(n)
# print(totalsum)    

#  sum of even number:
# def sumofeven(n):
#     sum = 0
#     for i in range(2,n+1,2):
#       sum = sum+i
#     return sum
# n = int(input("Enter even number"))
# totalsum = sumofeven(n)
# print(totalsum)    

# sum of odd no:
# def sumofodd(n):
#     sum = 0
#     for i in range(1,n+1,2):
#         sum = sum+i
#     return sum
# n = int(input("enter odd num:"))
# totalsum = sumofodd(n)
# print(totalsum)    

# factorial of any number:
# def factorial(n):
#     result = 1
#     for i in range(1,n+1):
#         result = result * i
#     return result
# print(factorial(5))

# factor of any number:
# def find_factor(n):
#     factors = []
#     for i in range(1,n+1):
#         if n%i==0:
#           factors.append(i)
#     return factors      
# n = int(input("enter any num"))
# print('factorof',n,"are",find_factor(n))

# ===== OR =====
# def factors(n):
#     for i in range(1,n+1):
#         if n%i==0:
#           print(i)
# n = int (input("enter any num"))
# print('factor of',n,"are",factors(n))

# FABONACI SERIES
# def fibonaci(n):
#     a,b=0,1
#     for i in range(n):
#        print(a)
#        a,b=b,a+b
# fibonaci(10)    
