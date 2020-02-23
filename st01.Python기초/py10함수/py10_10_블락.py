def get_sum(x, y):
    sum=0
    for i in range(x, y+1, 1):
        sum = sum + i
    print(ascii)
    return sum


a = 3
b = 7
get_sum(a, b)

#전역변수 : a, b
#지역변수 : i, sum, x, y
#매개변수 : x, y