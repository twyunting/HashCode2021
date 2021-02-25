def readFile(filePath):
	with open(filePath, "r") as f:
		return f.readlines()

def writeFile(resultList,fileName):
	with open(fileName, "w") as f:
		for i in resultList:
			listToStr = ' '.join([str(elem) for elem in i]) 
			f.write(listToStr)
			f.write("\n")
