import random
min = 1
max = 6
computerScore = 0
playerScore = 0
inPlay = True

x = 20
while x < 10:
    test = random.randint(min,max)
    print(test)
    x+=1

def gamePlay():
    global inPlay
    global computerScore
    global playerScore
    while inPlay:
        player = random.randint(min,max)
        computer = random.randint(min,max)
        print(f"You Got {player} vs {computer}")
        if(player == computer):
            print("Tie Game")
        elif (player > computer):
            print("Player Wins")
            playerScore += 1
        elif (player < computer):
            print("Computer Wins")
            computerScore += 1
        inPlay = input("Roll Again ? ")
        if inPlay == "exit" :
            break
gamePlay()
print("Game Over")
print(f"Computer Score : {computerScore } vs Player Score : {playerScore }")