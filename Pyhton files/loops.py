val = 0
while val <= 10:
    print(val)
    val += 1
    if val == 2:
        continue
    #print(".")
    if val == 15:
        break
else:
    print("val is no longer less than 11")

