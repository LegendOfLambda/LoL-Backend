import random
def createArr(num, dimensions):
	# creates a 2d arr
	array = []
	for i in range(dimensions): #0-19
		array.append([])
		for j in range(dimensions):
			array[i].append(num)
	return array
def createMap():
  dimensions = 20
  maxTunnels = 5
  maxLength = 8
  newMap = createArr(1,dimensions) #fills 2d arr with 1's. 1's will be walls 0's will be path
  currentRow = random.randint(0, dimensions-1) # random row 1-20
  currentColumn = random.randint(0, dimensions-1) # random col 1-20
  directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] #to go up, subtract 1 from its row. to go down, add 1 to its row. to go right, add 1 to its column. to go left, subtract 1 from its column
  lastDirection = []
  randomDirection = []
  while maxTunnels and dimensions and maxLength :
	while True:
	  randomDirection = directions[random.randint(0,len(directions)-1)]
	  if lastDirection == [] or randomDirection[0] != -lastDirection[0] and randomDirection[1] != -lastDirection[1] or randomDirection[0] != lastDirection[0] and randomDirection[1] != lastDirection[1]:
		break
	randomLength = random.randint(0,maxLength)
	tunnelLength = 0
	while tunnelLength < randomLength :
	  if currentRow == 0 and randomDirection[0] == -1 or currentColumn == 0 and randomDirection[1] == -1 or currentRow == dimensions -1 and randomDirection[0] == 1 or currentColumn == dimensions -1 and randomDirection[1] == 1 :
		break
	  else :
		newMap[currentRow][currentColumn] = 0
		currentRow += randomDirection[0]
		currentColumn += randomDirection[1]
		tunnelLength = tunnelLength+1
	if tunnelLength:
	  lastDirection = randomDirection
	  maxTunnels = maxTunnels-1
  return newMap

print(createMap())