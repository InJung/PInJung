# PinJung 
# Copyright HyungJu SUNG <sungkisa@naver.com>
# 0.1.1: code cleaning, applied color to the terminal using the termcolor

import sys
from termcolor import colored
pinjung_mode = "strict" #Default: strict
pinjung_version = "0.1.1"

def interpret(filename):
	ifile = open(filename, 'r')
	if pinjung_mode == "unstrict":
		
		with open(filename) as ifile:
			while True :
				c = ifile.read(1)
				if c=="ㅇ":
					print("안녕 세계")
				if c=="ㅈ":
					exit()
				if c=="ㄱ":
					print("a")
				if c=="ㄴ":
					print("b")
				if c=="ㄷ":
					print("c")
				if c=="ㄹ":
					print("d")
				if c=="ㅁ":
					print("e")
				if c=="ㅂ":
					print("f")
				if c=="ㅅ":
					print("g")
				if c=="ㅋ":
					print("h")
				if c=="ㅌ":
					print("i")
				if c=="ㅍ":
					print("j")
				if c=="ㅎ":
					print("k")
				if c=="0":
					print("l")
				if c=="1":
					print("m")
				if c=="2":
					print("n")
				if c=="3":
					print("o")
				if c=="4":
					print("p")
				if c=="5":
					print("q")
				if c=="6":
					print("r")
				if c=="7":
					print("s")
				if c=="8":
					print("t")
				if c=="9":
					print("u")
				if c=="ㅏ":
					print("v")
				if c=="ㅑ":
					print("w")
				if c=="ㅓ":
					print("x")
				if c=="ㅕ":
					print("y")
				if c=="ㅗ":
					print("z")
				if not c:
					exit()


	else :

		with open(filename) as ifile:
			while True:
				c = ifile.read(1)
				if c=="ㅇ":
					print("안녕 세계")
				if c=="ㅈ":
					exit()
				if not c:
					exit()




if len(sys.argv) == 1:          


  try:
        print (colored('Error! ','red') +"No File Supplied.\n"+colored('Version: ','green')+ pinjung_version+colored('\nMode: ','green')+pinjung_mode)
  except:
      print("Error! No File Supplied.\nWarning! Please Install termcolor to more colorful messages!\nVersion: "+pinjung_version +"\nMode: "+pinjung_mode)
  exit(1)



interpret(sys.argv[1])

