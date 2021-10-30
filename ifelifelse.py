day = input("Enter a day:")
if day == "Sunday":
    print("Today is holiday")
elif day =="monday":
    print("We have science class today")
elif day == "tuesday":
    print("We have Mathematics class today")
elif day == "wednesday":
    print("Today is programming classes")
elif day == "thrusday":
    print("We have cultural activites today")
elif day == "friday":
    print("Today we have cooking classes")
else:
    print("Today is a games day...wow")
value = "delhi"
guess = input("sheher ka nam guess karo >")
if guess != value:
    print("Galt guess hain!")
else:
     print("Apka guess sahi hai ")
speed =int( input("Enter the speed of the car>"))
if speed <= 60:
    print("The speed is under limit")
elif speed <= 70:
    print("High speed you need to reduce")
else:
    print("You are booked for rushing")
day = input("Enter a day>")
meal = input("Enter either lunch,breakfast or dinner")
if day == "monday":
    if meal == "breakfast": #nested if
        print ("Poha")
    elif meal == "lunch":
        print("Rajma Chawal")
    else:
        print("Roti Sabzi")
elif day =="tuesday":
    if meal =="breakfast": # nested if 2
        print("Pori Sabzi")
    elif meal =="Lunch":
        print("Thupka")
    else:
        print("Chicken Chawal")
else:
    print("we can have dal roti sabzi on other days too!")
