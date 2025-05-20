# fabonaci :
# n =int (input("Enter a num"))
# x,y,i = 0,1,1
# while i<=n:
#     z = x+y
#     if i<n:
#         print(z , end = ',')
#     else:
#         print(z)
#     x,y = y,z
#     i = i+1
    
# n = int (input("Enter any number"))
# x,y,i = 0,1,1
# while i<=n:
#     z = x+y
#     if i<n:
#         print(z , end=',')
#     else:
#         print(z)
#     x,y = y,z
#     i = i+1    
    

# Armstrong :
# n = int (input("Enter any num:"))
# x=y=n
# digit = 0
# sum = 0
# while n>0:
#     digit = digit+1
#     n = n//10
# # print(digit)
# # print(n)
# while x>0:
#     last_digit = x %10
#     sum = sum +last_digit ** digit
#     x = x //10
# # print(sum)
# # print(x)
# if y == sum:
#     print(f'given no {y} is armstrong')        
# else:
#     print(f'given no {y} is not armstrong')    



# n = int (input("Enter any number"))
# x=y=n
# digit = 0
# sum = 0
# while n>0:
#     digit = digit+1
#     n = n//10
# # print(digit)
# # print(n)
# while x>0:
#     last_digit = x % 10
#     sum = sum +last_digit ** digit
#     x = x//10
# print(sum)
# print(x)
# if y == sum:
#     print(f'given no {y} is armstrong')
# else:
#     print(f'given no {y} is not armstrong')       


n = int (input("enter any number"))
x = n
rev = 0
while n>0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
if x == rev:
    print(f'given no {x} is palindrom')
else:
    print(f'given no {x} is palindrom')