# pattern :1) ssquare:
# n = int (input("Enter a number:"))
# i = 1
# while i<=n:
#     print('*' * n)
#     i = i+1

# 2) triangle
# n = int (input("Enter a number:"))
# i = 1    
# while i <=n:
#     print('*' * i)   #  formula: '*' * i + ' '* (n-i)
#     i = i+1

# 3) Right-Aligned Triangle
# n = int (input("Enter a number:"))
# i = 1    
# while i <=n:
#     print(' ' * (n-i)+'*' * i)  
#     i = i+1    

# 4) Pyramid Pattern
# n = int (input("Enter a number:"))
# i = 1    
# while i <=n:
#     # print(' ' * (n-i)+' *' * i)  
#     print(' ' * (n-i)+'*-' * i)  
#     i = i+1   


# 5)  Right-Aligned Inverted Half Pyramid:
# n = int (input("Enter a number:"))
# i = 0    
# while i<n:
#     print(' '*i+'*' * (n-i))
#     i = i+1

# 5)
# n = int (input("Enter a number:"))
# i = 0    
# while i<n:
#     print(' '*i+' *' * (n-i))
#     i = i+1    

# 6) Left-Aligned Inverted Half Pyramid

# n = int (input("Enter a number:"))   
# while n>0:
#     print('*'* n)
#     n = n-1

# 7) Hourglass Pattern (Left-Aligned)
# n = int (input("Enter a number:"))
# i = 0    
# while i<n:
#     print('*' * (n-i) + ' ' * i)
#     i = i+1
#     # print(i)
# i = i-2
# while i>=0:
#     print('*' * (n-i) + ' ' * i)
#     i = i-1    

# # 8)
n = int (input("Enter a number:"))
i = 0    
while i<n:
    print(' ' *i+ ' *'* (n-i))
    i = i+1
    # print(i)
i = i-2
while i>=0:
    print(' ' *i+ ' *'* (n-i))
    i = i-1    


