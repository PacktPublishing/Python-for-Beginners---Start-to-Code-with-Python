val = input("What is your favorite number 1-9: ")
boo = val.isnumeric()
print(boo)
message = "Sorry not a number "
if(boo):
    num = int(val)
    print(type(num))
    message = "Great your number is " + val
print(message)