'''
David Paez
Mini Project: Maze Search

search.py is a Python script that has an agent traverse through a 
given Maze txt file where "%" are obstacles, "P" is the goal, and "." 
is the starting point. The agent can use four different algorithms to 
search through the Maze: Breadth, Depth, Greedy Best First, and A* Search. 
'''

# Modules from the Python Standard Library I imported
from queue import PriorityQueue # Priority Queue for A* and Greedy search
from copy import deepcopy # In order to deep copy the Maze object
import argparse # Parses the command line
import sys # Exits the program when an error occurs
'''
Maze is a class that reads the maze txt file, creates a 2D Array based on the
text file representation. It sets up the initial state, goal state, and keeps
track of what state an agent can transition to (through getAdjacent). 
'''
class Maze:

	#This function creates the 2D array representation of the maze txt file
	def createArray(self, p, filename):
		lines = [] # to store the lines of the file

		try:
			f = open(filename,"r") # open the file and read it
		except: # if file cannot be found.
			print("No file named {0}, try again.".format(filename))
			sys.exit()

		# reads each line and makes sure to remove the new line character
		for line in f: 
			lines.append(line.rstrip('\n'))

		c = -1 # column count
		r = -1 # row count
		for line in lines: # for each line in the lines array
			temp = [] # temporary array to store the characters to create a 2D array
			r += 1 # increase row count
			c = -1 # reset column count for every new row
			for char in line: # for each char in a line
				c += 1 # increase the row count
				if char == ".": 
					self.initialPos = (r,c) # Initial State
				elif char == "P":
					self.goalPos = (r,c) # Goal State
				temp.append(char)
			p.append(temp)

		self.numRows = r + 1 # Total number of rows
		self.numCols = c + 1 # Total number of columns


	# How to print out the Maze object
	def __str__(self):
		mazeMap = '' 
		for i in self.plots: # go through every row
			mazeMap += ''.join(i) # join the characters in each column
			mazeMap += "\n"
		return mazeMap

	# Initialization of the maze object and all it's variables.
	def __init__(self, filename):
		self.plots = []
		self.initialPos = (-1,-1)
		self.goalPos = (-1,-1)
		self.numRows = -1
		self.numCols = -1
		self.createArray(self.plots, filename)

	# Returns whether the coordinate is a valid position in the Maze, not an obstacle
	def getPosition(self, r,c):
		if c >= 0 and c < self.numCols:
			if r >= 0 and r < self.numRows:
				if self.plots[r][c] != "%":
					#print(c,r)
					return (r,c)
		else:
			return None

	# Gets the adjacent neighbors of the current plot or node, provides agent with states to transition to
	def getAdjacent(self,r,c):
		neighbors = [] # list of neighbors to return

		neighbors.append(self.getPosition(r-1,c)) # North, transitions agent North
		neighbors.append(self.getPosition(r,c+1)) # East, transitions agent East
		neighbors.append(self.getPosition(r+1,c)) # South, transitions agent South
		neighbors.append(self.getPosition(r,c-1)) # West, transitions agent West

		return neighbors # returns the list of neighbors

'''
Breadth-First search uses a queue data structure to keep track of the nodes
in the graph. It searches through the shallowest nodes in the graph first
from the initial then goes through the successors till it finds the goal state.
'''
def breadth_first_search(maze):
	# initializes the queue with the first element being the initial state
	queue = [maze.initialPos] 

	# creates a two dimensional array of all the visited nodes
	visited = [[0 for i in range(maze.numCols)] for j in range(maze.numRows)]
	visitedCount = 0 # amount of nodes visited

	parent = {} # dictionary to keep track of a node's parent

	# the first node is visited
	visited[maze.initialPos[0]][maze.initialPos[1]] = 1

	# while elements in the queue
	while queue:
		curr = queue.pop(0) # FIFO, first element gets popped.
		visitedCount += 1 # A node was visited

		if(curr == maze.goalPos): # if you make it to the goal
			print("==== Breadth First Search ====") 
			print("Nodes expanded: " + str(visitedCount)) # returns number of expanded nodes

			# BFS returns the path from intial to goal position
			return(backtrack(parent, maze.initialPos, maze.goalPos))

		# Adds the neighbor nodes (North, East, South, West) to queue
		for n in maze.getAdjacent(curr[0], curr[1]):
			if n == None: # If an obstacle is hit or out of bounds
				continue
			elif visited[n[0]][n[1]] == False: # If node has not been visited
				if n not in queue: # if node has yet to be added to queue, give it a parent
					parent[n] = curr 
				
				queue.append(n) # queue adds neighbor node

				visited[n[0]][n[1]] = True # sets node as visited
	
'''
Depth-First search uses a stack data structure to keep track of the nodes
in the graph. It searches through the deepest nodes in the graph first,
following one branch, from the initial then goes through the successors 
till it finds the goal state.
'''
def depth_first_search(maze):
	# initializes the stack with the first element being the initial state
	stack = [maze.initialPos]

	# creates a two dimensional array of all the visited nodes
	visited = [[0 for i in range(maze.numCols)] for j in range(maze.numRows)]
	visitedCount = 0 # amount of nodes visited

	parent = {} # dictionary to keep track of a node's parent

	# the first node is visited
	visited[maze.initialPos[0]][maze.initialPos[1]] = 1

	# while elements in stack
	while stack:
		curr = stack.pop() # LIFO, last element gets popped.
		visitedCount += 1 # A node was visited

		if(curr == maze.goalPos): # if you make it to the goal
			print("==== Depth First Search ====")
			print("Nodes expanded: " + str(visitedCount)) # returns number of expanded nodes

			# DFS returns the path from intial to goal position
			return(backtrack(parent, maze.initialPos, maze.goalPos))

		# Adds the neighbor nodes (North, East, South, West) to stack
		for n in maze.getAdjacent(curr[0], curr[1]):
			if n == None: # If an obstacle is hit or out of bounds
				continue
			elif visited[n[0]][n[1]] == False: # If node has not been visited
				if n not in stack: # if node has yet to be added to queue, give it a parent
					parent[n] = curr
				
				stack.append(n) # stack adds neighbor node

				visited[n[0]][n[1]] = True # sets node as visited
		

# function to determine the manhattan distance between two nodes
def manhattan_distance(n1, n2):
	return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])

'''
Greedy Best-First search uses a priority queue data structure to keep track of the nodes
in the graph. It searches through the nodes with the lowest h score (manhattan distance 
in this case) in the graph first from the initial then goes through the 
successors till it finds the goal state.
'''
def greedy_best_first_search(maze):
	# initializes the Priority Queue
	pq = PriorityQueue() 

	# creates a two dimensional array of all the visited nodes
	visited = [[0 for i in range(maze.numCols)] for j in range(maze.numRows)]
	visitedCount = 0 # amount of nodes visited

	parent = {} # dictionary to keep track of a node's parent

	# places the initial position as the first element
	pq.put((1, maze.initialPos))

	# the first node is visited
	visited[maze.initialPos[0]][maze.initialPos[1]] = 1

	# while the priority queue has elements
	while pq:
		curr = pq.get() # Get the most prioritized tuple (lowest h score)
		curr = curr[1] # Get the element from the tuple
		visitedCount += 1 # A node was visited

		if(curr == maze.goalPos): # if you make it to the goal
			print("==== Greedy Best First Search ====")
			print("Nodes expanded: " + str(visitedCount)) # num of nodes expanded

			# GBFS returns the path from intial to goal position
			return(backtrack(parent, maze.initialPos, maze.goalPos))

		# Adds the neighbor nodes (North, East, South, West) to Priority Queue
		for n in maze.getAdjacent(curr[0], curr[1]):
			if n == None: # If an obstacle is hit or out of bounds
				continue
			elif visited[n[0]][n[1]] == False: # If node has not been visited
				parent[n] = curr
				
				# Make the element's priority equal to its h score
				pq.put((manhattan_distance(n, maze.goalPos), n))

				visited[n[0]][n[1]] = True # sets node as visited

'''
A* search uses a priority queue data structure to keep track of the nodes
in the graph. It searches through the nodes using the formula f(n) = g(n)+h(n),
the sum of the h heuristic (manhattan distance) and the path cost. 
'''
def a_star_search(maze):
	# initializes the Priority Queue
	pq = PriorityQueue() 

	# creates a two dimensional array of all the visited nodes
	visited = [[0 for i in range(maze.numCols)] for j in range(maze.numRows)]
	visitedCount = 0 # amount of nodes visited

	parent = {} # dictionary to keep track of a node's parent

	# places the initial position as the first element
	pq.put((1, maze.initialPos))

	# the first node is visited
	visited[maze.initialPos[0]][maze.initialPos[1]] = 1

	# while the priority queue has elements
	while pq:
		curr = pq.get() # Get the most prioritized tuple (lowest h score)
		curr = curr[1] # Get the element from the tuple
		visitedCount += 1 # A node was visited

		if(curr == maze.goalPos): # if you make it to the goal
			print("==== A* Search ====")
			print("Nodes expanded: " + str(visitedCount)) # num of nodes expanded

			# A* search returns the path from intial to goal position
			return(backtrack(parent, maze.initialPos, maze.goalPos))

		# Adds the neighbor nodes (North, East, South, West) to Priority Queue
		for n in maze.getAdjacent(curr[0], curr[1]):
			if n == None: # If an obstacle is hit or out of bounds
				continue
			elif visited[n[0]][n[1]] == False: # if node not been visited
				parent[n] = curr
				
				# Calculate f(n) = g(n)+h(n) to determine priority
				pq.put((manhattan_distance(n, maze.goalPos) + path_cost(parent, maze.initialPos, n), n))
		

				visited[n[0]][n[1]] = True # set nodes as visited

'''
Backtrack is a function used to find the agent's path from the initial state
to the goal state
'''
def backtrack(parent, initial, goal):
	path = [] # initialize path
	path.clear() # clear the path
	path.append(goal) # goal is first element

	# gets the path
	while path[-1] != initial:
		path.append(parent[path[-1]])

	path.reverse() # reverse the path, so it is from initial to goal
	print("Solution cost: " + str(len(path)))
	return path # returns the path from initial to goal

'''
Path Cost is a function to help A* search determine the current node's
path cost.
'''
def path_cost(parent, initial, node):
	cpath = [] # initiliaze path
	cpath.clear() # clear path
	cpath.append(node) # node is first element

	# gets the path from node to initial
	while cpath[-1] != initial:
		cpath.append(parent[cpath[-1]])

	return len(cpath) # returns the path cost
	
'''
Searched Maze uses the path returned by a search algorithm and recreates
the maze, adding the returned path.
'''
def searchedMaze(maze, path):
	temp = deepcopy(maze) # deep copies the maze

	# iterate through each node in the path list
	for node in path:
		if temp.plots[node[0]][node[1]] != "P": # Not the goal state
			temp.plots[node[0]][node[1]] = "." # Add dots to path

	# Makes initial I so it is easier to see
	temp.plots[temp.initialPos[0]][temp.initialPos[1]] = "I"

	print(temp) # print the searched maze

# Deals with parsing the command line and choosing the search algorithms
def main():
	parser = argparse.ArgumentParser() # Argument parser to parse command line

	# Add the argument method so user can choose which searching algorithm to use
	parser.add_argument("--method", help="choose which searching algorithm to use on maze")
	
	# Add the argument maze which is where the user specifies the txt file
	parser.add_argument("maze", help="choose the maze text file you would like to search")
	args = parser.parse_args() # the arguments

	m = Maze(args.maze) # creates a Maze object m with the txt file name given

	# Checks which method the user selected and prints that maze with the selected search algorithm
	if args.method == "breadth":
		searchedMaze(m, breadth_first_search(m))
	elif args.method == "depth":
		searchedMaze(m, depth_first_search(m))
	elif args.method == "greedy": 
		searchedMaze(m, greedy_best_first_search(m))
	elif args.method == "astar":
		searchedMaze(m, a_star_search(m))
	else: # By default, breadth first.
		print("No proper method chosen. Default: Breadth")
		searchedMaze(m, breadth_first_search(m))


main() # Runs the main function




