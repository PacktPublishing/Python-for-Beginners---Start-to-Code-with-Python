testList = ["Laurence","Hello","World",55,100,True]
for item in testList :
    print(item)
myStr = "Hello World"
for letter in myStr :
    if letter == "l":
        continue
    if letter == "x":
        break
    print(letter)
else:
    print("Word done!")

testDic = {
    "first" : "Laurence",
    "last" : "Svekis",
    "allowed" : "True"
}
for key in testDic:
    print(key + ":" + testDic[key])
for key in testDic:
    print(testDic[key])
for val in testDic.values():
    print(val)
for val in testDic.keys():
    print(val)
for key,val in testDic.items():
    print(key,val)

