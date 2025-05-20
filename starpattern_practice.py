
# 1)
# n = int(input("enter any number"))
# for i in range(n,0,-1):
#     print('*' * i + ' ' * (n-i))
# for i in range(2,n+1):
#     print('*' * i + ' ' * (n-i))

# #2) 
# n = int(input("enter any number"))
# for i in range(n,0,-1):
#     print(' ' * (n-i) + '*' * i)
# for i in range(2,n+1):
#     print(' ' * (n-i) + '*' * i)


# # 3) damru triangle:
# n = int(input("enter any number"))
# for i in range(n,0,-1):
#     print(' ' * (n-i) + '* ' * i)
# for i in range(2,n+1):
#     print(' ' * (n-i) + '* ' * i)  

# #  5)

row = 5
n = int (input("enter any no"))
col = 5
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * col)      

n = int (input("enter any no"))
n = 5
for i in range(n):
    print(' ' * (n - i - 1) + '* ' * n)

# 4)
# n = int (input("enter any no"))
# # n = 5
# for i in range(1,n+1):
#     print('*' * i)
# for i in range(n-1,0,-1):
#     print(' ' * (n-i) + '*' *i)    
    
