class intersection():
	def __init__(self,startNum):
		self.startNum=startNum
		self.roadList={}
	def addRoad(self,roadName,nextInter,length):
		self.roadList[roadName]={"nextInter":nextInter,"length":length}
	def getRoadInfo(self, roadName):
		try:
			return self.roadList[roadName]
		except:
			return None

class car():
	def __init__(self,startRoadName,roadDict,travelList):
		self.start=roadDict[startRoadName]['inter']
		self.travelList=travelList
		totalDist=0
		for i in travelList:
			totalDist+=roadDict[i]["length"]
		self.travelDist=totalDist
		print(self.travelDist)

def readFile(filePath):
	with open(filePath, "r") as f:
		return f.readlines()


def interpreter(totalTxt):
	global simSecs
	global interObjList
	global carObjList
	global roadDict
	interQuan=0
	roadQuan=0
	carQuan=0
	score=0
	interObjList={}
	carObjList=[]
	roadDict={}

	for idx, line in enumerate(totalTxt):
		if idx==0:
			strList=line.split()
			simSecs=int(strList[0])
			interQuan=int(strList[1])
			roadQuan=int(strList[2])
			carQuan=int(strList[3])
			score=int(strList[4])
		if idx>=1 and idx<=roadQuan:
			strList=line.split()
			startNum=int(strList[0])
			endNum=int(strList[1])
			try:
				if interObjList[startNum]:
					interObjList[startNum].addRoad(strList[2],int(strList[1]),int(strList[3]))
			except:
				obj=intersection(startNum)
				obj.addRoad(strList[2],int(strList[1]),int(strList[3]))
				interObjList[startNum]=obj
			roadDict[strList[2]]={"inter":int(strList[1]),"length":int(strList[3])}
		if idx>roadQuan:
			strList=line.split()
			obj=car(strList[1],roadDict,strList[:1:-1][::-1])



totalTxt=readFile('a.txt')
interpreter(totalTxt)

"""
global simSecs
global interObjList
global carObjList
global roadDict
"""