#GUI 모듈
# turtle
# tkinter <-- 리눅스 tk/tcl언어를 파이썬으로 포팅

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilenames

readfile = askopenfilename()
if readfile != None:
    infile = open(readfile, "r", encoding="UTF-8")

for line in infile.readlines():
    line = line.strip()
    print(line)

infile.close()