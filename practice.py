# if else statement :

x = float(input("Enter a value"))
if x % 2 == 0 :
    print(f'even number')
else:
    print(f'odd number') 

 
#  if-else-elif:
x = float(input("Enter 1st value"))  
y = float(input("Enter 2st value"))  
z = float(input("Enter 3st value"))  

if (x>y and x>z):
    print(f'{x} is grater than {y} and {z}')
elif (y>x and y>z):
    print(f'{y} is greater than {x} and {z}')
else:
    print(f'{z} is greater than {x} and{y}')        


# leap_year in loop:
year = int(input("Enter no"))
if (year % 400 == 0):
    print(f'leap year')
elif (year % 4 == 0):
    print(f'leap year') 
else:
    print(f'not leap year')       


x = float(input("Enter a value"))
if (x % 4 ==0 and x % 100 != 0):
    print(f'leap year')
else:
    print(f'not leap year') 

n = int(input("Enter a value"))
if ( n %  100 !=0 and n % 400 ==0):
    print(f'leap year')
else:
    print(f'not leap year')           

n = int (input("Enter the value"))
if (n % 4 ==0 and n % 100 !=0 and n % 400 ==0):
    print(f'leap year')
else:
    print(f'not leap year')   



Hindi = float(input("Enter Hindi No."))
English = float(input("Enter English No."))
Math = float(input("Enter Math No."))

if(Hindi>=0 and Hindi<=100 and English>=0 and Math>=0 and Math<=100):
    Avg = Hindi+English+Math/3
if Avg>60:
    print(f'First Division')

elif Avg>=45 and Avg<=59:
    print(f'Second Division')

elif Avg>=35 and Avg<=44:
    print(f'Third Division')

else:
    print(f'Fail')               