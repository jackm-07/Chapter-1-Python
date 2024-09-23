#Author: Jack Maher
#Trying to make blackjack

import random
dealerCard1 = random.randint(1,11)
dealerCard2 = random.randint(1,11)
dealerCard3 = random.randint(1,11)
dealerCard4 = random.randint(1,11)
dealerRunningTotal = dealerCard1 + dealerCard2
playerCard1 = random.randint(1,11)
playerCard2 = random.randint(1,11)
playerCard3 = random.randint(1,11)
playerCard4 = random.randint(1,11)
playerRunningTotal = playerCard1+playerCard2

def bustChecker():
    if playerRunningTotal>21:
        print("You have gone bust")
    if dealerRunningTotal>21:
        print("The dealer has gone bust")

bustChecker()

if playerRunningTotal and dealerRunningTotal ==21:
    print("Tied at blackjack")
elif playerRunningTotal == 21:
    print("You won!")
elif dealerRunningTotal == 21:
    print("Dealer won")
print("You are at", playerRunningTotal,"and the Dealer's first card is",dealerCard1)
print("Type (1) to stand, type (2) to hit")
choice = int(input())
if choice == 1:
    if dealerRunningTotal>playerRunningTotal:
        print("The dealer won with a",dealerRunningTotal,"against your",playerRunningTotal)
    elif dealerRunningTotal==playerRunningTotal:
        print("You and the dealer tied!")
    else:
        if dealerRunningTotal<playerRunningTotal:
            dealerRunningTotal = dealerRunningTotal + dealerCard3
        if dealerRunningTotal>21:
            print("The dealer went bust")
        if dealerRunningTotal<playerRunningTotal:
            dealerRunningTotal = dealerRunningTotal + dealerCard4
        if 22>dealerRunningTotal<playerRunningTotal:
            print("You win")
        elif dealerRunningTotal>playerRunningTotal:
            print("You lost")
        else:
            print("ERROR ERROR ERROR")
if choice == 2:
    playerRunningTotal = playerRunningTotal + playerCard3
    if 21<playerRunningTotal:
        print("You went bust")
    else:
        if dealerRunningTotal and playerRunningTotal ==21:
            print("You tied at 21")
        if dealerRunningTotal<playerRunningTotal:
            dealerRunningTotal = dealerRunningTotal + dealerCard3
            if dealerRunningTotal>21:
                print("Dealer went bust")
            if dealerRunningTotal>playerRunningTotal:
                print("The dealer won")
            if dealerRunningTotal==playerRunningTotal:
                print("Ye both tied")
        if dealerRunningTotal>playerRunningTotal:
            dealerRunningTotal=dealerRunningTotal+dealerCard3
            bustChecker()
            if 22>dealerRunningTotal<playerRunningTotal:
                dealerRunningTotal=dealerRunningTotal+dealerCard4
                bustChecker()
                if 22>dealerRunningTotal<playerRunningTotal:
                    print("Player wins by default")
                
            
        
