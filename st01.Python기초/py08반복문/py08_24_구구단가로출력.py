for x in range(2,10,1):
    for y in range(1,10,1):
        str = "%2d * %d = %3d" % (x, y, x*y)
        print(str,end=" ")
    print()