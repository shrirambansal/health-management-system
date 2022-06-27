def getdate() :
    import datetime
    return datetime.datetime.now()

print("\t***\tWelcome, Health Management System\t***\t")
print("\t***\tPlease, Enter client code\t***\t\n\t1. Harry\n\t2. Rohan\n\t3. Hammad")
name = int(input("Enter the client code : "))

# This code for harry
if name == 1 :
    print("\t***\n\t1. for exercise\n\t2. for food")
    choose = int(input("Enter the what client do in code : "))
    # This code for exercise
    if choose == 1 :
        date_01 = getdate()
        add_1 = input("Enter what do you want to add : ")
        f = open("harry_exe.txt", "a")
        f.write(f"\n[{date_01}]\t--\t{add_1}")
        print("Sucessfully, added....")
        pass
    # This code for food
    elif choose == 2 :
        date_01 = getdate()
        add_2 = input("Enter what do you want to add : ")
        f = open("harry_food.txt", "a")
        f.write(f"\n[{date_01}]\t--\t{add_2}")
        print("Sucessfully, added....")
        pass
    # This code for invalid input
    else :
        print("Please, enter valid input.")
        pass
    pass

# This code for rohan
elif name == 2 :
    print("\t***\n\t1. for exercise\n\t2. for food")
    choose = int(input("Enter the what client do in code : "))
    # This code for exercise
    if choose == 1 :
        date_01 = getdate()
        add_3 = input("Enter what do you want to add : ")
        f = open("rohan_exe.txt", "a")
        f.write(f"\n[{date_01}]\t--\t{add_3}")
        print("Sucessfully, added....")
        pass
    # This code for food
    elif choose == 2 :
        date_01 = getdate()
        add_4 = input("Enter what do you want to add : ")
        f = open("rohan_food.txt", "a")
        f.write(f"\n[{date_01}]\t--\t{add_4}")
        print("Sucessfully, added....")
        pass
    # This code for invalid input
    else :
        print("Please, enter valid input.")
        pass
    pass

# This code for hammad
elif name == 3 :
    print("\t***\n\t1. for exercise\n\t2. for food")
    choose = int(input("Enter the what client do in code : "))
    # This code for exercise
    if choose == 1 :
        date_01 = getdate()
        add_5 = input("Enter what do you want to add : ")
        f = open("hammad_exe.txt", "a")
        f.write(f"\n[{date_01}]\t--\t{add_5}")
        print("Sucessfully, added....")
        pass
    # This code for food
    elif choose == 2 :
        date_01 = getdate()
        add_6 = input("Enter what do you want to add : ")
        f = open("hammad_food.txt", "a")
        f.write(f"\n[{date_01}]\t--\t{add_6}")
        print("Sucessfully, added....")
        pass
     # This code for invalid input
    else :
        print("Please, enter valid input.")
        pass
    pass

# This code for invalid input
else :
    print("Please enter valid code. Thank you")
