import random
n=int(input("Hello! How many dices do you want to roll ? "))
while True:
 for i in range(0,n):
  print("Dice" ,i+1, "=", random.randint(1,6))
 choice=input("Do you want to startover? Enter Y to startover ")
 if(choice=='Y' or choice=='yes' or choice=='y' or choice=='Yes' or choice=='YES'):
  continue;
 else: 
    print("Goodbye !")
    break;
    
