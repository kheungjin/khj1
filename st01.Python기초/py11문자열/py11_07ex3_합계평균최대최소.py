
temp3 = "74 874 9883 73 9 73646 774"

def main():
    array1 = temp3.strip().split(" ")
    #print(array1)  # ['74', '874', '9883', '73', '9', '73646', '774']

    array2 = []
    for n in array1:
        n = int(n)
        array2.append(n)

    #print(array2)  # [74, 874, 9883, 73, 9, 73646, 774]
    def avr(arrayx):
        result = sum(arrayx)/len(arrayx)
        return result


    print(sum(array2))
    print(avr(array2))
    print(max(array2))
    print(min(array2))

if __name__ == "__main__":
    main()