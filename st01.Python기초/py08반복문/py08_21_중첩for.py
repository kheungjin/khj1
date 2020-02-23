for y in range(0,10,1):
    for x in range(0,10,1):
        print("*", end="")
    print("")

#=================================================
for i in range(1,11,1):
    for j in range(1,i,1):
        print("*", end="")
    print()

#=================================================
for i in range(1,11,1):
    for j in range(1,i,1):
        print(" ",end="")
    for j in range(i,10,1):
        print("*", end="")
    print()