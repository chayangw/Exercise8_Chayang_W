username = input("Input your username: ")
password = input("Input your password: ")
dogball = 250
dogfood = 350
dogbed = 1200

if username == "admin" and password == "1234":
    print("Welcome to Hungtoo The Dog Shop")
    print("Please select your items")
    print("1. Dog Ball", dogball, "THB")
    print("2. Dog Food", dogfood, "THB")
    print("3. Dog Bed", dogbed, "THB")
    userselected = int(input("Choose your items: "))
    if userselected == 1:
        print("You have selected Dog Ball", dogball, "THB")
        amt = int(input("Please enter your amount: "))
        print("Total Price is: ", dogball*amt, "THB")
        print("Thank You")
    elif userselected == 2:
        print("You have selected Dog Food", dogfood, "THB")
        amt2 = int(input("Please enter your amount: "))
        print("Total Price is: ", dogfood*amt2, "THB")
        print("Thank You")
    elif userselected == 3:
        print("You have selected Dog Bed", dogbed, "THB")
        amt3 = int(input("Please enter your amount: "))
        print("Total Price is: ", dogbed*amt3, "THB")
        print("Thank You")

else :
    print("Error!, Incorrect username or password")