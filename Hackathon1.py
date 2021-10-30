# Q6 Maximum of three numbers
a = int(input("Enter First number:"))
b = int(input("Enter Second number:"))
c = int(input("Enter Third number:"))
if a > b and a > c:
    print(" A is maximum")
elif b > a and b > c:
    print("B is maximum")
else:
    print("C is maximum")
# Q7 A number divisible by 11 and 5
num1 = int(input("Enter a number:"))
if num1 % 5 ==0 and num1 % 11 == 0:
    print("divisible")
else:
    print("not Divisible")
#Q8 Number is even or odd
num2 = int(input("Enter a number:"))
if num2 % 2 == 0:
    print("Even")
else:
    print("Odd")
# 9 To find a year is a leap year or not
year = int(input("Enter year"))
if year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
#Q10 Whether the character is an alphabet or not
ch = input("Please enter a character:")
if (ch >='A' and ch >='Z'):
  print("ch is an U - ALPHABET")
elif ( ch >= 'a' and ch >='z'):
    print("ch is a L-Alphabet")
else:
    print("ch is not an alphabet")
#Q11 To check the given alphabet is a vowel or consonant
ch1 = input("Enter a alphabet:")
if(ch1 == 'A' or ch1 == 'a' or ch1 == 'E' or ch1 =='e' or ch1 =='I'or ch == 'i' or ch1 == 'O' or ch1 =='o' or ch1 =='U'or ch1 =='u'):
    print("This is vowel")
else:
    print("This is a consonant")
#Q12 To check the given caracter is an Alphabet,digit or a special case
ch2 = input("Enter any character:")
if(ch2 >= 'A' or ch2 >='Z' or ch2 >='a' or ch2 >='z'):
    print("This character is an ALPHABET")
elif (ch2 <=0 or ch2 >=9):
    print("DIGIT")
else:
    print("SPECIAL CHARACTER") 