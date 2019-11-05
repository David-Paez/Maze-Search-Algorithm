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

		self.numRows = x + 1
		self.numCols = y + 1


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

	def getPosition(self, r,c):
		if c >= 0 and c < self.numCols:
			if r >= 0 and r < self.numRows:
				return (r,c)
		else:
			return None

	def getAdjacent(self,r,c):
		neighbors = []
		neighbors.append(self.getPosition(r-1,c)) # North
		neighbors.append(self.getPosition(r,c+1)) # East
		neighbors.append(self.getPosition(r+1,c)) # South
		neighbors.append(self.getPosition(r,c-1)) # West

		return neighbors

def breadth_first_search(maze):

	visited = [[0 for i in range(maze.numCols)] for j in range(maze.numRows)]
	visitedCount = 0
	#visited = ([0] * maze.numCols) * maze.numRows

	queue = []

	queue.append(maze.initialPos)
	visited[maze.initialPos[0]][maze.initialPos[1]] = 1

	while queue:
		curr = queue.pop(0)
		visitedCount += 1
		#print (initial, end = " ")

		if(curr == maze.goalPos):
			print("We did it!")
			print(visitedCount)
			return curr

		#print(maze.getAdjacent(curr[0], curr[1]))
		for n in maze.getAdjacent(curr[0], curr[1]):
			if n == None:
				continue
			elif visited[n[0]][n[1]] == False:
				queue.append(n)
				visited[n[0]][n[1]] = True

def depth_first_search(maze):
	visited = ([0] * numCols) * numRows


def main():
	m = Maze()
	print(str(m.initialPos) + " " + str(m.goalPos) + " " + str(m.numRows) + " " + str(m.numCols))
	print(m)
	print(breadth_first_search(m))

main()




