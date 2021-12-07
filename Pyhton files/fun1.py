def fun1(val):
    print(val*val)
    #print("Hello")

fun1(1)
fun1(5)
fun1(6)
fun1(7)

def fun2(first,last):
    print("Hi, " + first + " " + last)
    return first + " " + last

fun2("Laurence","Svekis")
fun2("Linda","Jones")
fun2("Mike","Smith")
myName = fun2("Laurence","Svekis")
print(myName)

def fun3(val1,val2):
    total = val1 + val2
    print(str(val1) + " + " + str(val2) + " = " + str(total))
    return total

num1 = fun3(6,7)
num2 = fun3(126,2317)
print(num1, num2)