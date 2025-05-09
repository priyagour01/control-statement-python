# if statement : 
n = int (input("Enter any no"))
if n % 2 == 0:
    print(f'given no {n} is even')
    # print("Even no")
else: 
    print(f'given no {n} is odd')  

   
n = int (input("Enter the no"))
if n % 2 == 0:
    print(f'given no {n} is even')
else:
    print(f'given no {n} is odd')    

# if-elif-else:
x,y,z =int(input("Enter 1st value")) , int(input("Enter 2st value")) , int(input("Enter 3st value"))
if (x>y and x>z):
    print(f'{x} is greater than {y} and {z}')
elif (y>x and y>z):
    print(f'{y} is greater than {x} and {z}')
else:
    print(f'{z} is greater than {x} and {y}')    



n = int (input("Enter the no"))
if (n % 400 == 0):
    print(f'leap year')
elif (n % 4 == 0):
    print(f'leap year')  
else:
    print(f'not leap year')    


n = int (input("Enter the no"))
if (n % 4 == 0 and n % 100 !=0):
    print(f'leap year')
else:
     print(f'not leap year')    

n = int (input("Enter the no"))
if (n % 100 !=0 and n % 400 ==0):
    print(f'leap year')
else:
    print(f'not leap year')  

n = int (input("Enter the no"))
if (n % 4 ==0 and n % 100 !=0 or n % 400 == 0):
    print(f'leap year')
else:
    print(f'not leap year')  

h =float (input("Enter Hindiindi no"))
e =float (input("Enter English no"))
m =float (input("Enter Math no"))
if (h>=0 and h<=100 and e>=0 and m>=0 and m<=100):
     avg = h+e+m/3    
if avg>60:
     print("First Division")
elif avg>=45 and avg<=59:
     print("Second Division")
elif avg>=35 and avg<=44:
     print("Third Division")   
else :
     print("fail")   


# integer and string // eval ek number lena h uska data type if else ke according lena h data type int aa rha h 

x = eval(input("enter your values"))
print(x)
print(type(x))

val = eval(input("Enter value"))
if type(val) == type(int()):
    print(f"Given Value {val} is integer.")

if type(val) == type(float()):
    print(f"Given Value {val} is float.")

if type(val) == type(complex()):
    print(f"Given Value {val} is complex.")

if type(val) == type(str()):
    print(f"Given Value {val} is string.")

if type(val) == type(list()):
    print(f"Given Value {val} is list.")

if type(val) == type(tuple()):
    print(f"Given Value {val} is tuple.")

if type(val) == type(set()):
    print(f'Given Value {val} is set.')

if type(val) == type(dict()):
    print(f'Given Value {val} is dictionary.')
else :
    print(f"Given program is not run!")    