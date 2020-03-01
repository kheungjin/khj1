def main():
    문자열 = input("숫자로 된 문자열을 입력하세요 : ")
    array1 = 문자열.split(" ")
    print()
    print("입력 값", array1)
    array2 = []
    for n in array1:
        n = int(n)
        array2.append(n)
    print("정렬 전 : ", array2)

    array2.sort()
    print("정렬 후 : ", array2)
    print("최소값 : ", array2[0])
    print("최대값 : ", array2[len(array2)-1])

if __name__ == "__main__":
    main()    