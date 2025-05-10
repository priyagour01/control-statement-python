# wap to print 5 digits fabonaci series
n = int (input("enter a number"))
x,y,i = 0,1,1
while i<=n:
    z = x+y
    if i<n:
        print(z , end= ',')
    else:
        print(z)
    x,y = y,z
    i = i+1    
    

# wap to check given no is armstrong or not.
n = int(input("enter a num"))
x=y=n
digit = 0 
sum = 0
while n>0:
    digit = digit+1
    n = n//10
# print(digit)   # debagging: jitne number likhenge utne hi output aayega
# print(n)   

while x>0:
    last_digit = x%10
    sum = sum +last_digit ** digit
    x = x//10
print(sum)
print(x)    

if y==sum:
    print(f'given no {y} is armstrong')
else:
    print(f'given no {y} is not armstrong')    


# wap to check given no/given string is palindrom or not.
n = input("enter any number")
if n==n[::-1]:
    print(f'given no {n} is palindrom')
else:
    print(f'given no {n} is not palindrom')  


num = input("Enter a number: ")
if num == num[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")


num = int(input("Enter a number: "))
original = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if original == rev:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

n = int(input("enter any number"))
x = n
rev = 0
while n>0:
    last_digit = n % 10
    rev = rev *10+last_digit
    n = n // 10
if x == rev:
    print(f'given no {x} is palindrom')
else:
    print(f'given no {x} is not palindrom')            

