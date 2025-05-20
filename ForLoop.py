# for loop: used only for finite iteration  :iteration  ek ek kr ke value ko uthata hai 
# syntex: for   i  in    collection:
# i = variable  , in= operater 

# l = [10,20,30,40]
# for i in l:
#     print(i+5)

# l = [10,20,30,40]
# l1 = []
# for i in l:
#     x = i +5
#     l1.append(x)
# print(l1)

# l = [10,20,30,40]
# l1 = []
# for i in l:
#     l1.append(i+5)
# print(l1)

# s = input("Enter any string")
# for i in s:
#     print(i)


# t = eval(input("Enter any tuple"))
# for i in t:
#     print(i)

# d = {'Name':'Priya' , 'age': 23 , 'quali':'Mca'}
# for i , j in d.items():
#     print(i , j)


# d = {'Name':'Priya' , 'age': 23 , 'quali':'Mca'}
# for k , v in d.items():
#     print(k ,'=',v)

# for k in d.keys():
#     print(k)
# for v in d.values():
#     print(v)

# n = int (input("enter any no:"))
# for i in range(1,n+1):
#     print(i)

# for i in range(2,n+1,2):
#     print(i)
# for i in range(1,n+1,2):
#     print(i)

# sum even number:
# for i in range(2, n+1, 2):
#     print(i)

# sum even natural number:
n = int (input("enter any number"))
sum = 0
for i in range(1,n+1):
        sum = sum+i
        print(sum)


