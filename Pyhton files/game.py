import random
computerScore = 0
playerScore = 0
arr = ["Rock","Paper","Scissors"]
inPlay = True
def gamePlay():
    global inPlay
    global computerScore
    global playerScore
    while inPlay:
        player = input("Rock Paper or Scissors ? ").capitalize()
        computer = random.choice(arr).capitalize()
        print(f"You Selected : {player} vs Computer Selected : {computer}")
        if player ==  computer :
            print("Tie Game")
        elif player == "Rock":
            if(computer == "Paper"):
                print("You Lose")
                computerScore+=1
            else:
                print("You win")
                playerScore += 1
        elif player == "Paper":
            if(computer == "Scissors"):
                print("You Lose")
                computerScore+=1
            else:
                print("You win")
                playerScore += 1
        elif player == "Scissors":
            if(computer == "Rock"):
                print("You Lose")
                computerScore+=1
            else:
                print("You win")
                playerScore += 1
        print(f"You ({playerScore}) vs Computer({computerScore})")
        inPlay = input("Play Again ? ")
    print("Game Over")
    print(f"Your Score ({playerScore}) vs Computer({computerScore})")
gamePlay()
