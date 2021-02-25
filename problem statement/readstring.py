def readFile(filePath):
	with open(filePath, "r") as f:
		return f.readlines()


texts = readFile("b.txt")


first = []
simulationSeconds = []
intersections = []
streets = []
cars = [] 
points = []

def firstLine(texts):
  first.append(texts[0])

  return first


print(firstLine(texts))