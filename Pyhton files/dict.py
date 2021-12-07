testDic = {"first":"Hello World","key":{"one":"test","two":"test2"},"num":100,"num":200,"num":300,"boo":True}
#print(testDic)
testDic["first"] = "test value"
val = testDic["first"]
val = testDic["num"]
val = testDic["key"]["two"]
testDic["test"] = 10000
#testDic.pop("key")
#testDic.clear()

val = testDic.keys()
val = testDic.values()

test2 = {
    "first" : 100,
    "second" : "Values",
    "third" : True
}
print(test2)


#print(testDic)
print(val)
#print(testDic["test"])