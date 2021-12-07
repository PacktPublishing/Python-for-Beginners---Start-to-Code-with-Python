import time
def test():
    val = 0
    while val < 10:
        val+=1
        time.sleep(1)
        print(val)

def countdown(t):
    while t:
        mins = t // 60
        secs = t % 60 
        output = "Your Time Left is {:02d}:{:02d}".format(mins,secs)
        print(output)
        time.sleep(1)
        t -= 1
    print("Time is up!!")
    start()
def start():
    t = input("Enter the number of seconds : ")
    if t.isnumeric() :
        countdown(int(t))
    else:
        print("Was not a Number")
        start()
start()