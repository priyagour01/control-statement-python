# control statement : 
#  conditional statement : 1) if-statement
#  syntex:

# if (condition):

n = int (input("Enter any number"))
if n % 2 == 0:
    print(f' given no {n} is even')  # output: given no 4 is even

    print("Even no")   # output:Even number    


# if - else statement
# syntex:
# if (condition)
#      statement1
# else 
#     statement2 

n = int (input("Enter any number"))
if n % 2 == 0:
    print(f' given no {n} is even')  # output: given no 4 is even

    print("Even no")   # output:Even number    
else:
    print(f' given no {n} is odd')

# if - elif statement:
# syntex :
# if (condition):
# statement1
# elif (condition):
# statement2
# elif (condition):
# statement3
# elif (condition):
# statement4
# eles:
# statement5

x = (input("Enter the no"))
y = (input("Enter the no"))
z = (input("Enter the no"))
x,y,z = int(input("Enter 1st value")) , int(input("Enter 2st value")) , int(input("Enter 3st value"))
if (x>y and x>z):
    print(f'{x} is greater than {y} and {z}')
elif (y>x and y>z):
    print(f'{y} is greater than {x} and {z}')
else : 
    print(f'{z} is greater than {x} and {y}')   

        
#  Itreative statement: 
# 1) while :infinite itreation +finite itreation 
# 2) for : finite itreation (python collection) 
#  block of code ke repetation ke liya hum Itreative statement 

