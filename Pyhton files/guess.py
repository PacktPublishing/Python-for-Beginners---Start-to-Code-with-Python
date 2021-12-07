num = 10
limit = 6
cnt = 0
playGame = False
guess = 0
while guess != num :
    print("You have "+str(limit - cnt)+" left")
    guessFirst = input("Enter a Number : ")
    if(guessFirst.isnumeric()):
        guess = int(guessFirst)
        if guess == num : playGame = True
        if(guess > num):
            print("Wrong too high")
        elif(guess < num):
            print("wrong too low")
    cnt+=1
    if((limit-cnt) == 0 ):
        break
else:
    playGame = True

if(playGame):
    print("You Got it!")
else:
    print("You ran out of guesses it was:"+str(num))