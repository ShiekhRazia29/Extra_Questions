# Number divisible by 5 or not
raw_input = int(input("Enter a number"))
if raw_input % 5 ==0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")
#Greater number among two inputs by the user
num1 =int(input("Enter first number:"))
num2 =int(input("Enter second number:"))
if num1 > num2:
    print("Number first is greater",num1)
elif num1 < num2:
    print("Number second is greater",num2)
else:
    print("Equal")
#Minimum among three numbers
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a > b and c > b:
    print("b is minimun")
elif a < b and c > a:
    print("a is minimum")
else:
    print("c is minimum")
# To check number is zero,negative or positive
num3 = int(input("Enter a number:"))
if num3 > 0:
    print("positive")
elif num3 < 0:
    print("Negative")
else:
    print("Zero")
# to find 1000 is greater or smaller than 2000
num4 = 2000
num5 = 1000
if num5 > num4:
    print("GREATER")
else:
    print(" SMALLER")