#Author: Jack Maher
#Date of start: 9:30 19-9-24
#Description: Games project
#Rock Paper Scissors: completed 10:25 19-09-24

#IDEAS: x and o's
def playingAgain(): #this is the function i use to play things again
    gameChoice = input("If you want to play this again type 1\n")
    if gameChoice =="1":
        ChoosingAGame()


def RPSLogicCheck(computerDecision,playerDecision): # this contains all the logic for the rock paper scissors
    if computerDecision==playerDecision: #this checks for draws, it also makes sure that i dont have to type more if statements that neccesary
        print("It was a draw")
        gameChoice = input("If you want to play again this again type 1\n") 
        if gameChoice =="1": #this is just the raw files for playingAgain():
            ChoosingAGame()
    else: #this contains all the if statements for the 6 scenarios that arise 
        if computerDecision==1: #rock
            if playerDecision==2: #paper
                print("You Win! Paper beats Rock")
                playingAgain()
            elif playerDecision==3: #scissors
                print("You lose... Rock beats Scissors")
                playingAgain()
        if computerDecision==2: #paper
            if playerDecision==1:#rock
                print("You lose... Paper beats Rock")
                playingAgain()
            elif playerDecision==3:#scissors
                print("You win! Scissors beats Paper")
                playingAgain()
        if computerDecision==3:#scissors
            if playerDecision==1:#paper
                print("You win! Rock beats Scissors")
                playingAgain()
            elif playerDecision==2:#rock
                print("You lose... Scissors beats Paper")
                playingAgain()
    
def ChoosingAGame(): #this is where the choosing of games occurs
    if gameChoice =="1": #rock paper scissors game
        import random
        computerDecision = random.randint(1,3) #we generate the computer response either 1 rock 2 paper 3 scissors
        playerDecision = int(input("Rock (1)\nPaper(2)\nScissors(3)\n:"))#we get our player response
        RPSLogicCheck(computerDecision,playerDecision)#and then they get sent to the logic checker
    # if players want to player again, they can do so inside the logic checker
    # using the playingAgain function

gameChoice = input("Rock Paper Scissors (1)\n:",) #the choices
ChoosingAGame() #after the user makes their decision its sent to our choosing a game function
       