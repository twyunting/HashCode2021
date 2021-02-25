def readFile(filePath):
	with open(filePath, "r") as f:
		return f.readlines()

def writeFile(resultList,fileName):
	with open(fileName, "w") as f:
		for i in resultList:
			listToStr = ' '.join([str(elem) for elem in i]) 
			f.write(listToStr)
			f.write("\n")

def txtToList(totalTxt):
	global pizzaList
	global totalPizza
	global duoTeamQuan
	global triTeamQuan
	global squTeamQuan
	pizzaList=[]
	for idx, line in enumerate(totalTxt):
		if idx==0:
			strList=line.split(" ")
			totalPizza=int(strList[0])
			duoTeamQuan=int(strList[1])
			triTeamQuan=int(strList[2])
			squTeamQuan=int(strList[3])
		else:
			strList=line.split(" ")
			pizzaList.append((idx-1,int(strList.pop(0)),strList))
def duoTeamDeliver(duoTeamQuan):
	#add two pizza
	for _ in range(duoTeamQuan):
		for idx,item in enumerate(pizzaList):
			if idx+1<len(pizzaList)-1:
				if len(set(pizzaList[idx][2]+pizzaList[idx+1][2]))==pizzaList[idx][1]+pizzaList[idx+1][1]:
					pizzaList.pop(idx)
					pizzaList.pop(idx+1)
					resultList.append([2,pizzaList[idx][0],pizzaList[idx+1][0]])

global resultList
resultList=[]

filePath="c_many_ingredients.in"#"b_little_bit_of_everything.in"
totalTxt=readFile(filePath)
txtToList(totalTxt)
pizzaList=sorted(pizzaList,key=lambda x:len(x[2]),reverse=True)

totalList=[]
for i in pizzaList:
	totalList+=i[2]
print(len(set(totalList)))


duoTeamDeliver(duoTeamQuan)
print(pizzaList)
writeFile(resultList,'no')