age = input("How old are you? ")
boo = age.isnumeric()
if boo:
    print("Thank you I am checking if you can come in...")
    val = int(age)
    if(val >= 21):
        print("Great you are allowed in and can drink")
    elif(val >= 18):
        print("Come in but can't drink")
    else:
        print("You are not allow in.  Not old enough")
else:
    print("We need your age!")