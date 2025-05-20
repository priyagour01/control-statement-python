# #1) continue: skip current iteration
# #2) break:(terminate any loop)
# #3) pass: (skip/pass ciurrent block)

# # 1)
# # n = int (input("enter any num"))
# # i = 1
# # while i<=n:
# #     if i==5:
# #         i=i+1
# #         continue
# #     else:
# #         print(i)
# #         i =i+1

# n = int (input("enter any num"))  #kisi bhi block ko  syntical currect krne ke liye hum pass ka use karte h:particular kisi block ko scape krne ke liye iska use kiya jata hai  
# i = 1
# while i<=n:
#     if i==5:
#         pass
#     else:
#         print(i)
#         i =i+1        

# n = int (input("enter any num"))
# i = 1
# while i<=n:
#     if i==5:
#         break
#     else:
#         print(i)
#         i =i+1


# while True:
#     print("1 Add \n2.subs \n3.div \n4.off")
#     n = int (input("Enter any options"))
#     x = (1,2,3,4)
#     if n in x:
#         if n == 1:
#             p = int (input("Enter 1st value"))
#             q = int (input("Enter 1st value"))
#             print(p+q)
#         elif n == 2:
#             p = int (input("Enter 2st value"))
#             q = int (input("Enter 2st value"))
#             print(p-q)
#         elif n == 3:
#             p = int (input("Enter 3st value"))
#             q = int (input("Enter 3st value"))    
#             print(p/q)
#         elif n == 4:
#             print("off")
#             break
#     else:
#         print("Please enter valid option")   




# Restaurant menu as a dictionary
menu = {
    1: ["Pizza", 250],
    2: ["Burger", 150],
    3: ["Pasta", 200],
    4: ["Coffee", 80]
}

# Store order
order = {}

while True:
    print("\n------ Welcome to My Restaurant ------")
    for key in menu:
        print(f"{key}. {menu[key][0]} - ₹{menu[key][1]}")
    print("5. Show Bill")
    print("6. Exit")
    
    try:
        choice = int(input("Enter your option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice in menu:
        item_name = menu[choice][0]
        item_price = menu[choice][1]
        try:
            qty = int(input(f"Enter quantity for {item_name}: "))
        except ValueError:
            print("Invalid quantity. Try again.")
            continue
        if item_name in order:
            order[item_name] += qty
        else:
            order[item_name] = qty
        print(f"{qty} {item_name}(s) added to your order.")

    elif choice == 5:
        print("\n------ Your Bill ------")
        total = 0
        for item, qty in order.items():
            price = next(val[1] for val in menu.values() if val[0] == item)
            item_total = price * qty
            total += item_total
            print(f"{item} x {qty} = ₹{item_total}")
        print(f"Total Amount: ₹{total}")
        print("------------------------")

    elif choice == 6:
        print("Thank you! Visit again.")
        break
    else:
        print("Invalid option. Please try again.")


