import random
ele = ["Rock","Paper","Scissors"]
print("Hello lets play Rock Paper Scissors !\nThe winner of each round gets 3 points and the loser 0. If its a tie, you and me get a point each\nEnter N any time to stop ")
i=0
uscore=0
cscore=0
while True:
    i=i+1
    print(i,"Round\n Enter your move: Rock, Paper or Scissors ? ",end="")
    comp_choice= random.choice(ele)
    move=input()
    if(move=='N'or move=='n'):
        print("We have played",i,"rounds\nYour score is",uscore)
        print("My score is",cscore)
        if(uscore>cscore):
            print("Congratulations! You win")
        elif(uscore<cscore):
            print("Tough luck buddy, I win")
        else:
            print("We are tied. We both are champions!")
        break;
    print("I played",comp_choice)
    if((move=='Rock' or move=='rock') and comp_choice=='Scissors'):
        print("Bravo ! You won this round")
        uscore=uscore+3
    elif((move=='Rock' or move=='rock') and comp_choice=='Paper'):
        print("Better luck next time, I win !!")
        cscore=cscore+3
    elif((move=='Rock' or move=='rock') and comp_choice=='Rock'):
        print("We are tied !!")
        uscore=uscore+1 
        cscore=cscore+1 
    elif((move=='Paper' or move=='paper') and comp_choice=='Rock'):
        print("Bravo ! you won this round")
        uscore=uscore+3
    elif((move=='Paper' or move=='paper') and comp_choice=='Scissors'):
        print("Better luck next time, I win !!")
        cscore=cscore+3
    elif((move=='Paper' or move=='paper') and comp_choice=='Paper'):
        print("We are tied !!")
        uscore=uscore+1 
        cscore=cscore+1
    elif((move=='Scissors' or move=='scissors') and comp_choice=='Paper'):
        print("Bravo ! you won this round")
        uscore=uscore+3
    elif((move=='Scissors' or move=='scissors') and comp_choice=='Rock'):
        print("Better luck next time, I win !!")
        cscore=cscore+3
    elif((move=='Scissors' or move=='scissors') and comp_choice=='Scissors'):
        print("We are tied !!")
        uscore=uscore+1 
        cscore=cscore+1