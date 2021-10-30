#stop program execution for sometime
import time
password = 2334
balance = 4500
print("welcome to jammu and kashmir Bank:. Please Insert your card")
time.sleep(5)
pin = int(input("Enter your pin"))
if pin == password:
    print("""
             1 == balance
             2 == withdraw 
             3 == deposit
             4 == change pin
             5 == exit
              """)
option = int(input("Please enter your choice"))
if option < 1 and option > 4:
    print("Enter a valid option ")
elif option == 1:
    print(f"Your current balance is{balance}")
elif option == 2:
  withdraw_amount = int(input("Please Enter Withdraw amount:"))
  balance = balance - withdraw_amount
  print(f"{withdraw_amount} is debited from your account")
  print(f"your updated balance is{balance}")
elif option == 3:
 deposit_amount = int(input("please enter depost amount:"))
 balance = balance + deposit_amount
 print(f"{deposit_amount} is credited to your account!")
 print(f"Updated balance is {balance}")
elif option == 4:
        print("      ")
else:
    print("Wrong pin,Please try again ")






      