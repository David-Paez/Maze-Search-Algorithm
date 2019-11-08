from queue import PriorityQueue
from copy import deepcopy
import argparse
import sys

class Maze:
	def createArray(self, p, filename):
		lines = []

		try:
			f = open(filename,"r")
		except:
			print("No file named {0}, try again.".format(filename))
			sys.exit()

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

	def __init__(self, filename):
		self.plots = []
		self.initialPos = (-1,-1)
		self.goalPos = (-1,-1)
		self.numRows = -1
		self.numCols = -1
		self.createArray(self.plots, filename)

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
	path = []
	path.clear()
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

def manhattan_distance(n1, n2):
	return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])

def greedy_best_first_search(maze):
	pq = PriorityQueue()
	#visited = []
	visited = [[0 for i in range(maze.numCols)] for j in range(maze.numRows)]

	parent = {}
	visitedCount = 0
	mdist = 0

	pq.put((1, maze.initialPos))
	visited[maze.initialPos[0]][maze.initialPos[1]] = 1


	while pq:
		curr = pq.get()
		curr = curr[1]
		visitedCount += 1
		#print (initial, end = " ")

		if(curr == maze.goalPos):
			print("==== Greedy Best First Search ====")
			print("Nodes expanded: " + str(visitedCount))
			return(backtrack(parent, maze.initialPos, maze.goalPos))

		#print(maze.getAdjacent(curr[0], curr[1]))
		for n in maze.getAdjacent(curr[0], curr[1]):
			if n == None:
				continue
			elif visited[n[0]][n[1]] == False:
				parent[n] = curr
				
				pq.put((manhattan_distance(n, maze.goalPos), n))

				visited[n[0]][n[1]] = True
			
	print (visitedCount)

def a_star_search(maze):
	pq = PriorityQueue()
	#visited = []
	visited = [[0 for i in range(maze.numCols)] for j in range(maze.numRows)]

	parent = {}
	visitedCount = 0
	mdist = 0

	pq.put((1, maze.initialPos))
	visited[maze.initialPos[0]][maze.initialPos[1]] = 1


	while pq:
		curr = pq.get()
		curr = curr[1]
		visitedCount += 1
		#print (initial, end = " ")

		if(curr == maze.goalPos):
			print("==== A* Search ====")
			print("Nodes expanded: " + str(visitedCount))
			return(backtrack(parent, maze.initialPos, maze.goalPos))

		#print(maze.getAdjacent(curr[0], curr[1]))
		for n in maze.getAdjacent(curr[0], curr[1]):
			if n == None:
				continue
			elif visited[n[0]][n[1]] == False:
				parent[n] = curr
				
				pq.put((manhattan_distance(n, maze.goalPos) + manhattan_distance(n, maze.initialPos), n))

				visited[n[0]][n[1]] = True
			
	print (visitedCount)
	

def displayNewMaze(maze, path):
	temp = deepcopy(maze)
	for vertex in path:
		if temp.plots[vertex[1]][vertex[0]] != "P":
			temp.plots[vertex[1]][vertex[0]] = "."

	print(temp)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--method", help="choose which searching algorithm to use on maze")
	parser.add_argument("maze", help="choose the maze text file you would like to search")
	args = parser.parse_args()

	m = Maze(args.maze)

	print(args)

	if args.method == "breadth":
		displayNewMaze(m, breadth_first_search(m))
	elif args.method == "depth":
		displayNewMaze(m, depth_first_search(m))
	elif args.method == "greedy": 
		displayNewMaze(m, greedy_best_first_search(m))
	elif args.method == "astar":
		displayNewMaze(m, a_star_search(m))
	else:
		print("No proper method chosen. Default: Breadth")
		displayNewMaze(m, breadth_first_search(m))



main()




