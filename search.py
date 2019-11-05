from collections import defaultdict

class Maze:
	def createArray(self, p):
		lines = []
		f = open("Maze2.txt","r")
		for line in f:
			lines.append(line.rstrip('\n'))

		x = -1
		y = -1
		for line in lines:
			temp = []
			y += 1
			x = -1
			for char in line:
				x += 1
				if char == ".":
					self.initialPos = (x,y)
				elif char == "P":
					self.goalPos = (x,y)
				temp.append(char)
			p.append(temp)

		self.numRows = y + 1
		self.numCols = x + 1


	def __str__(self):
		mazeMap = ''
		for i in self.plots:
			mazeMap += ''.join(i)
			mazeMap += "\n"
		return mazeMap
	#print(mazeLines)

	def __init__(self):
		self.plots = []
		self.initialPos = (-1,-1)
		self.goalPos = (-1,-1)
		self.numRows = -1
		self.numCols = -1
		self.createArray(self.plots)
		#print(self.plots)

	def getPosition(r,c):
		if c >= 0 and c < numCols:
			if r >= 0 and r < numRows:
				return self.plots[r][c]
		else:
			return None

	def getAdjacent(r,c):
		neighbors = []
		neighbors.append(getPosition(r-1,c)) # North
		neighbors.append(getPosition(r,c+1)) # East
		neighbors.append(getPosition(r+1,c)) # South
		neighbors.append(getPosition(r,c-1)) # West

		return neighbors

def breadth_first_search(maze):

	visitedCount = 0
	visited = [False] * maze.numRows * maze.numCols
	poppedNodes = []

	queue = []
	stack = []

	queue.append(maze.initialPos)
	visited[maze.initialPos] = True

	while queue:
		poppedNodes.append(queue[0])
		curr = queue.pop(0)
		visitedCount += 1
		#print (initial, end = " ")

		if(curr == goalState):
			print("We did it!")
			print(visitedCount)
			break

		for n in maze.getAdjacent(curr):
			if visited[n] == False:
				queue.append(n)
				visited[n] = True

	poppedNodes.pop(0)
	poppedNodes.pop(len(poppedNodes)-1)
	return poppedNodes

def main():
	m = Maze()
	print(str(m.initialPos) + " " + str(m.goalPos) + " " + str(m.numRows) + " " + str(m.numCols))
	print(m)

main()




