# 1)square pattern:
n = int (input("enter number"))
i =1 
while i<=n:
    print('*' * n)
    i = i+1

# 2)triangle:
n = int (input("enter num"))
i = 1
while i <=n:
    print('*' * i)
    i = i+1

# 3)Right-Aligned Triangle:
n = int (input("enter num"))
i =1
while i <=n:
    print(' ' * (n-i) + '*' * i)
    i = i+1


# 4) pyramid:
n = int(input("enter num"))
i = 1
while i<=n:
    print(' ' * (n-i) + '* ' * i)
    i = i+1

# 5)
n = int (input("enter num"))
i = 1
while i<=n:
    print(' ' * i +'* ' * (n-i))
    i = i+1

# 6)
n = int (input("enter num"))
while n>0:
    print('*' * n)
    n = n-1

# 7)
n = int (input("enter num"))
i = 0
while i<n:
    print('*' * (n-i) + ' ' * i)
    i = i+1
    # print(i)
i = i-2
while i>=0:
    print('*' * (n-i) + ' ' * i)
    i = i-1    


# 8) 
n =int (input("enter a number"))
i =0
while i<n:
    print(' ' * i + ' *' * (n-i))
    i = i+1

i = i-2
while i>=0:
    print(' ' * i + ' *' * (n-i))
    i = i-1 
