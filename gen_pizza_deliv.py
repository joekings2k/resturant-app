from copyreg import pickle
pizzza = [1500, 2000 , 2500]
toppings = [200, 300, 300]
xchee = [100 , 100, 100]
name = input("enter your name")
print(f"wlecome {name} ") 
print("we have three sizes of pizza, Large,Medium, small ")
pizza = input("what size of pizza do you want")
pizza = pizza.upper()
if pizza == "SMALL" :
    price1 = pizzza[0]
    topps = input("Would you like pepperoni")
    topps=topps.lower()
    if topps == "yes" :
        sumtop = price1 + toppings[0]
        print(sumtop)
        extra = input("would you like extra cheese")
        extra = extra.lower()
        if extra == "yes":
            sumchee = sumtop + xchee[0]
            print(sumchee)
        else:
            print(f"The price of your pizza is {sumtop}")
    
    else:
        print(f"The prize of your pizza is {price1}")
elif pizza == "MEDIUM" :
    price2 = pizzza[1]
    topps = input("Would you like pepperoni")
    topps=topps.lower()
    if topps == "yes" :
        sumtop = price2 + toppings[1]
        print(sumtop)
        extra = input("would you like extra cheese")
        extra = extra.lower()
        if extra == "yes":
            sumchee = sumtop + xchee[1]
            print(sumchee)
        else:
            print(f"The price of your pizza is {sumtop}")    
    else:
        print(f"The prize of your pizza is {price2}")
elif pizza == "LARGE" :
    price3 = pizzza[2]
    topps = input("Would you like pepperoni")
    topps=topps.lower()
    if topps == "yes" :
        sumtop = price3 + toppings[2]
        print(sumtop)
        extra = input("would you like extra cheese")
        extra = extra.lower()
        if extra == "yes":
            sumchee = sumtop + xchee[2]
            print(sumchee)
        else:
            print(f"The price of your pizza is {sumtop}")    
    else:
        print(f"The prize of your pizza is {price3}")
else:
    print("That size is not available")



