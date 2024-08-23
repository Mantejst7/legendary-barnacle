def stock_1():
    a=4
    b=5
    c=5
    d=8
    print(f"""|_______________STOCK INVENTORY_______________|
|--- Name       Price     Stock     Brand    --|
| 1. Shirt     RS.1500     {a}       RL      --|
| 2. Pants     RS.950      {b}       NK      --|
| 3. Perfume   RS.1000     {c}       FG      --|
| 4. Watches   RS.2500     {d}       GSHK    --|
|______________________________________________|""")
    user=int(input("You can add a ITEMS in STOCK INVENTORY....... In which item do you want to add more stock enter the number :-  "))
    much=int(input("How much do you want to add in the stock :-  "))
    stk=a+much
    stk1=b+much
    stk2=c+much
    stk3=d+much
    if(user==1):
        print(f"""|_________________STOCK INVENTORY________________|
|--- Name       Price     Stock       Brand    --|
| 1. Shirt     RS.1500     {stk}       RL      --|
| 2. Pants     RS.950      {b}         NK      --|
| 3. Perfume   RS.1000     {c}         FG      --|
| 4. Watches   RS.2500     {d}         GSHK    --|
|________________________________________________|""")
    elif(user==2):
        print(f"""|_________________STOCK INVENTORY________________|
|--- Name       Price     Stock       Brand    --|
| 1. Shirt     RS.1500     {a}         RL      --|
| 2. Pants     RS.950      {stk1}       NK      --|
| 3. Perfume   RS.1000     {c}         FG      --|
| 4. Watches   RS.2500     {d}         GSHK    --|
|________________________________________________|""")
    elif(user==3):
        print(f"""|_________________STOCK INVENTORY________________|
|--- Name       Price     Stock       Brand    --|
| 1. Shirt     RS.1500     {a}         RL      --|
| 2. Pants     RS.950      {b}         NK      --|
| 3. Perfume   RS.1000     {stk2}       FG      --|
| 4. Watches   RS.2500     {d}         GSHK    --|
|________________________________________________|""")
    elif(user==4):
        print(f"""|________________STOCK INVENTORY________________|
|--- Name       Price     Stock       Brand    --|
| 1. Shirt     RS.1500     {a}         RL      --|
| 2. Pants     RS.950      {b}         NK      --|
| 3. Perfume   RS.1000     {c}         FG      --|
| 4. Watches   RS.2500     {stk3}       GSHK    --|
|________________________________________________|""")
    else:
        print("Try again")
def Stock_2():
    a=4
    b=5
    c=5
    d=8
    print(f"""|_______________AVAILABLE STOCK________________|
|--- Name       Price     Stock    Brand     --|
| 1. Shirt     RS.1500     {a}       RL      --|
| 2. Pants     RS.950      {b}       NK      --|
| 3. Perfume   RS.1000     {c}       FG      --|
| 4. Watches   RS.2500     {d}       GSHK    --|
|______________________________________________|""")
def choose():
    a=4 
    b=5
    c=5
    d=8
    user=int(input("What do you want to buy from the Available stock enter the number:  "))
    print()
    if(user==1):
        print(f"""|--- Name       Price     Stock    Brand     --|
| 1. Shirt     RS.1500     {a}       RL      --|""")
        print()
        much=int(input("Tell me how many do you want to buy :  "))
        print("..........BILL PAYMENT..........")
        price=1500
        GST=0.18
        amount=(price*much)*GST/100
        print(f"Total amount is......  {amount}")
        print()
    elif(user==2):
        print(f"""|--- Name       Price     Stock    Brand     --|
| 2. Pants     RS.950      {b}       NK      --|""")
        print()
        much=int(input("Tell me how many do you want to buy :  "))
        print("..........BILL PAYMENT..........")
        price=950
        GST=0.18
        amount=(price*much)*GST
        print(f"Total amount is......  {amount}")
        print()
    elif(user==3):
        print(f"""|--- Name       Price     Stock    Brand     --|
| 3. Perfume   RS.1000     {c}       FG      --|""")
        print()
        much=int(input("Tell me how many do you want to buy :  "))
        print("..........BILL PAYMENT..........")
        price=1000
        GST=0.18
        amount=(price*much)*GST*100/100
        print(f"Total amount is......  {amount}")
        print()
    elif(user==4):
        print(f"""|--- Name       Price     Stock    Brand     --|
| 4. Watches   RS.2500     {d}       GSHK    --|""")
        print()
        much=int(input("Tell me how many do you want to buy :  "))
        print("..........BILL PAYMENT..........")
        price=2500
        GST=0.18
        amount=(price*much)*GST*100/100
        print(f"Total amount is......  {amount}")
        print()
    stock=a-much
    stock1=b-much
    stock2=c-much
    stock3=d-much
    if(user==1):
        print(f"""|_______________AVAILABLE STOCK________________|
|--- Name       Price     Stock    Brand         --|
| 1. Shirt     RS.1500     {stock}   RL          --|
| 2. Pants     RS.950      {b}       NK          --|
| 3. Perfume   RS.1000     {c}       FG          --|
| 4. Watches   RS.2500     {d}       GSHK        --|
|__________________________________________________|""")
    elif(user==2):
        print(f"""|_______________AVAILABLE STOCK________________|
|--- Name       Price     Stock     Brand         --|
| 1. Shirt     RS.1500     {a}        RL          --|
| 2. Pants     RS.950      {stock1}   NK          --|
| 3. Perfume   RS.1000     {c}        FG          --|
| 4. Watches   RS.2500     {d}        GSHK        --|
|___________________________________________________|""")
    elif(user==3):
        print(f"""|_______________AVAILABLE STOCK________________|
|--- Name       Price     Stock     Brand         --|
| 1. Shirt     RS.1500     {a}        RL          --|
| 2. Pants     RS.950      {b}        NK          --|
| 3. Perfume   RS.1000     {stock2}   FG          --|
| 4. Watches   RS.2500     {d}        GSHK        --|
|___________________________________________________|""")
    elif(user==4):
        print(f"""|_______________AVAILABLE STOCK________________|
|--- Name       Price     Stock    Brand         --|
| 1. Shirt     RS.1500     {a}       RL          --|
| 2. Pants     RS.950      {b}       NK          --|
| 3. Perfume   RS.1000     {c}       FG          --|
| 4. Watches   RS.2500     {stock3}   GSHK        --|
|__________________________________________________|""")
    else:
     print("Try Again")

user=int(input("What Account you want to login Admin(press-1) or Employee(press-2) ? :-  "))
print(" ")
def Admin():
    print("|__________Login your account__________|")
    username=input("Enter your UserName:  ")
    print(" ")
    stock_1
    password=input("Enter your Password:  ")
    passwd=5602
    if(passwd==password):
        print("Your password is correct....")
    else:
        print("Wrong password input......")
def Emp():
    print("|__________Login your account__________|")
    name=input("Enter your Name:  ")
    print(" ")
    Ph=int(input("Enter your mobile number:  "))
    print(" ")
    age=int(input("Enter your age:  "))
    print(" ")
if(user==1):
    Admin()
    stock_1()
elif(user==2):
    Emp()
    Stock_2()
    choose()
else:
    print("Wrong input")