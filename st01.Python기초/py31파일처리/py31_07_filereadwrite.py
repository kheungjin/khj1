
#  proverbs.txt 파일에서 줄 단위로 읽어서 output.txt 에 쓰시오 
infile = open("./file/proverbs.txt", "r", encoding="UTF-8")
outfile = open("./file/output.txt", "w", encoding="UTF-8")

line = infile.read()
print(line)
outfile.write(line)

infile.close()
outfile.close()