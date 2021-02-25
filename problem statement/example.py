def readFile(filePath):
	with open(filePath, "r") as f:
		return f.readlines()


texts = readFile("b.txt") #read the txt file

for idx, lines in enumerate(texts):
	if idx >= 2:
		

