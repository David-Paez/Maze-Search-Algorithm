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
				if self.plots[c][r] != "%":
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

def backtrack(parent, initial, goal):
	path = [goal]
	while path[-1] != initial:
		path.append(parent[path[-1]])
	path.reverse()
	print("Solution cost: " + str(len(path)))
	return path

def breadth_first_search(maze):
	queue = [maze.initialPos]
	visited = [[0 for i in range(maze.numCols)] for j in range(maze.numRows)]
	visitedCount = 0
	#visited = ([0] * maze.numCols) * maze.numRows


	parent = {}

	visited[maze.initialPos[0]][maze.initialPos[1]] = 1

	while queue:
		curr = queue.pop(0)
		visitedCount += 1
		#print (initial, end = " ")

		if(curr == maze.goalPos):
			print("==== Breadth First Search ====")
			print("Nodes expanded: " + str(visitedCount))
			return(backtrack(parent, maze.initialPos, maze.goalPos))

		#print(maze.getAdjacent(curr[0], curr[1]))
		for n in maze.getAdjacent(curr[0], curr[1]):
			if n == None:
				continue
			elif visited[n[0]][n[1]] == False:
				if n not in queue:
					parent[n] = curr
				
				queue.append(n)

				visited[n[0]][n[1]] = True

	

def depth_first_search(maze):
	stack = [maze.initialPos]
	#visited = []
	visited = [[0 for i in range(maze.numCols)] for j in range(maze.numRows)]

	parent = {}
	visitedCount = 0

	visited[maze.initialPos[0]][maze.initialPos[1]] = 1


	while stack:
		curr = stack.pop()
		visitedCount += 1
		#print (initial, end = " ")

		if(curr == maze.goalPos):
			print("==== Depth First Search ====")
			print("Nodes expanded: " + str(visitedCount))
			return(backtrack(parent, maze.initialPos, maze.goalPos))

		#print(maze.getAdjacent(curr[0], curr[1]))
		for n in maze.getAdjacent(curr[0], curr[1]):
			if n == None:
				continue
			elif visited[n[0]][n[1]] == False:
				if n not in stack:
					parent[n] = curr
				
				stack.append(n)

				visited[n[0]][n[1]] = True
			
	print (visitedCount)
	

def displayNewMaze(maze, path):
	temp = maze
	for vertex in path:
		if temp.plots[vertex[1]][vertex[0]] != "P":
			temp.plots[vertex[1]][vertex[0]] = "."

	print(temp)

def main():
	m = Maze()
	print(str(m.initialPos) + " " + str(m.goalPos) + " " + str(m.numRows) + " " + str(m.numCols))
	print(m)
	#print(breadth_first_search(m))
	displayNewMaze(m, breadth_first_search(m))
	#print(depth_first_search(m))
	displayNewMaze(m, depth_first_search(m))

main()




