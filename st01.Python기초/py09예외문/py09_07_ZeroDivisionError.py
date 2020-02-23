(x, y) = (2, 0)
try:
    z = x/y
except ZeroDivisionError as ex:
    print("0으로 나누는 예외", ex)
