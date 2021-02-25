def readFile(filePath):
	with open(filePath, "r") as f:
		return f.readlines()


texts = readFile("b.txt") #read the txt file
first = []

def firstLine(texts):
	global simulationSeconds
	global intersections
	global streets
	global cars
	global points
	strList = " ".join(first).split()
	simulationSeconds = int(strList[0])
	intersections = int(strList[1])
	streets = int(strList[2])
	cars = int(strList[3])
	points = int(strList[4])

texts = readFile("b.txt") #read the txt file
firstLine(texts)
print(cars)