#start = int(input("시작단수를 입력하세요: "))
#end = int(input("종료단수를 입력하세요: "))
#if start > end:
#    temp = start
#    start = end
#    end = temp
#for x in range(start,end+1,1):
#    for y in range(1,10,1):
#        str = "%2d * %d = %3d" % (x, y, x*y)
#        if y == 9:
#            print(str,end=".")
#        else:
#            print(str,end=", ")
#    print()
#===============================================================

while True:
    try:
        start = int(input("시작단수를 입력하세요: "))
        end = int(input("종료단수를 입력하세요: "))
    except Exception as identifier:
        break
    
    if start > end:
        temp = start
        start = end
        end = temp
    if start < 1:
        print("프로그램을 종료 합니다 !!!")
        break
    for x in range(start,end+1,1):
        for y in range(1,10,1):
            str = "%2d * %d = %3d" % (x, y, x*y)
            if y == 9:
                print(str,end=".")
            else:
                print(str,end=", ")
        print()
