#Q12 To check the given caracter is an Alphabet,digit or a special case
ch2 = input("Enter any character:")
if(ch2 >= 'A' or ch2 >='Z' or ch2 >='a' or ch2 >='z'):
    print("This character is an ALPHABET")
elif (ch2 <=0 or ch2 >=9):
    print("DIGIT")
else:
    print("SPECIAL CHARACTER") 