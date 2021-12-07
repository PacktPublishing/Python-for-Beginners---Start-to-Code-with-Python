boo = False
a = 500
b = 1500
#print(a < b)
if boo: print("boo is True")
print("Hello") if boo else print("world")
print("Equal") if a==b else print("B bigger") if b > a else print("A must be bigger") 

if a < b:
    a = 1000
    print(a)
    print("True")
elif a > b:
    print("a is greater")
else:
    print("a and b must be the same equal")