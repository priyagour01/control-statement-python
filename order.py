# Restaurant menu asa dictionary

menu = {
    1: ["Pizza",150],
    2: ["Burger",100],
    3: ["Pasta",200],
    4: ["Coffee",80]
}

# Store order
order = {}

while True :
    print("\n ------ Welcome to my restaurant -----")
    for key in menu:
        print(f'{key}. {menu[key][0]} - rs{menu[key][1]}')
    print("5. Show Bill")
    print("6. Exit")

    try :
        n = int(input("Enter your option:"))
    except ValueError:
        print("Plese enter a valid number.") 
        continue 
if n in menu:
    item_menu = menu[n][0]
    item_price = menu[n][1]
    try:
        qty = int(input("enter quantity for {item_name}: "))
    except ValueError:
         print("Invalid quantity. Try again.")
        
