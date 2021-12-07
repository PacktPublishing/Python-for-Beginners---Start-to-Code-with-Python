a = "test"
b = 0
def fun1(val):
    global b
    b = b + 1
    #a = "hello"
    def fun2():
        global b
        nonlocal val
        b += 5
        val += 1000
        print(val)
    fun2()    
    print(a)

fun1(100)
print(b)