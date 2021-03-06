# PinJung 
# Copyright HyungJu SUNG <sungkisa@naver.com>
# 0.1.2: Fixed command"ㅊ". 

import sys
try :
	from termcolor import colored
except:
	pass
pinjung_mode = "unstrict" #Default: strict
pinjung_version = "0.1.1"

def interpret(filename):
	ifile = open(filename, 'r')
	output=""
	if pinjung_mode == "unstrict":	
		with open(filename) as ifile:
			while True :
				c = ifile.read(1)
				if c=="ㅇ":
					print("안녕 세계")
				if c=="ㅈ":
					print(output)
					exit()

				if c=="ㄱ":
					#print("a")
					output=output+"a"
				if c=="ㄴ":
					#print("b")
					output=output+"b"
				if c=="ㄷ":
					#print("c")
					output=output+"c"
				if c=="ㄹ":
					#print("d")
					output=output+"d"
				if c=="ㅁ":
					#print("e")
					output=output+"e"
				if c=="ㅂ":
					#print("f")
					output=output+"f"
				if c=="ㅅ":
					#print("g")
					output=output+"g"
				if c=="ㅋ":
					#print("h")
					output=output+"h"
				if c=="ㅌ":
					#print("i")
					output=output+"i"
				if c=="ㅍ":
					#print("j")
					output=output+"j"
				if c=="ㅎ":
					#print("k")
					output=output+"k"
				if c=="0":
					#print("l")
					output=output+"l"
				if c=="1":
					#print("m")
					output=output+"m"
				if c=="2":
					#print("n")
					output=output+"n"
				if c=="3":
					#print("o")
					output=output+"o"
				if c=="4":
					#print("p")
					output=output+"p"
				if c=="5":
					#print("q")
					output=output+"q"
				if c=="6":
					#print("r")
					output=output+"r"
				if c=="7":
					#print("s")
					output=output+"s"
				if c=="8":
					#print("t")
					output=output+"t"
				if c=="9":
					#print("u")
					output=output+"u"
				if c=="ㅏ":
					#print("v")
					output=output+"v"
				if c=="ㅑ":
					#print("w")
					output=output+"w"
				if c=="ㅓ":
					#print("x")
					output=output+"x"
				if c=="ㅕ":
					#print("y")
					output=output+"y"
				if c=="ㅗ":
					#print("z")
					output=output+"z"
				if not c:
					print(output)
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


