

#########################
# readline() 파일에서 한 줄씩 읽기
print("readLine() 파일에서 한줄씩 읽기")
pfr = open("st01.Python기초/py31파일처리/file/phones.txt", "r", encoding="UTF-8")
s = pfr.readline()
print(s,end="")
s = pfr.readline()
print(s,end="")
s = pfr.readline()
print(s,end="")
pfr.close()
#########################
##

#########################
##
