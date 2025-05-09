#  Even Number:
# 1) write a program to print even number.
n = int (input("Enter a number:"))
print("Even number", n , "are:") 
i = 2
while i <= 10:
    print(i , end=' ')
    i=i+2
   
#2) write a program to print even up to number.
n = int (input("Enter a number:"))
# print("Even number up to", n , "are:")
i = 2
while i <= n:
    print(i , end=' ')
    i=i+2    
print("Even number up to is:", n )

# 1)write a program to print n natural number.
n= int (input("Enter a natural number"))
print("First" , n , "natural numbers are:")
i = 1
while i <=n:
    print(i , end = ' ')
    i = i+1


# 2)  write a program to print factorial of any given number.
n = int (input("Enter a number"))
fact = 1 

if n < 0:
    print("Factorial is not define for negative numbers.")
else:
    i = 1
    while i <= n:
        fact =fact * i
        i = i+1
    print("Factorial of" , n , "is:" , fact)
            
# 3) write a program to print sum of n natural number.
n = int(input("Enter a sum natural number:"))
sum = 0 
i = 1
while i <= n:
    sum = sum + i
    i= i+1
print("sum of" , n , "natural numbers is :", sum)



# 4) write a program to print multiplication of n natural number.
n = int (input("Enter a numbers:"))
num = 1
i = 1
while i <= n:
    num = num * i
    if i<=(n-1):   
     print(i , end ='*')
    else:
        print(i,end='=')  
    i = i +1
print("Multiplication" , n , "natural number is:" , num)        
 

# 5)write a program to print n even number.
n = int (input("Enter a number:")) 
i = 2
print("Even number" , n , "are:")
while i <= n:
    print(i , end=' ')
    i=i+2


# 6) write a program to print even number up to n natural number.
n = int (input("Enter a natural number"))
i = 2
print("Enev numbers up to", n , "is:") 
while i <=n:
    print(i , end=' ')
    i = i+2


# 7)write a program to print sum of n even number.
n = int (input("Enter a number"))
sum = 0
i = 1

while i <=n:
    sum = sum+i
    i = i+1
print("Sum of even number" , n , "is:" , sum)  
 
 
# 8) write a program to print sum of even number upto n natural.
 

n = int (input("Enter a number"))
sum = 0
i = 2

while i <=10:
    sum = sum+i
    i = i+2
print("Sum of even number" , n , "is:" , sum)  


  
