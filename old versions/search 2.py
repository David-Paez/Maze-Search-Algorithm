from collections import defaultdict

class Maze:

	def createArray(self, p):
		mL = []
		f = open("Maze2.txt","r")
		for x in f:
			mL.append(x.rstrip('\n'))
		for x in mL:
			temp = []
			for i in x:
				temp.append(i)

			p.append(temp)


	def __str__(self):
		mazeMap = ''
		for i in self.plots:
			mazeMap += ''.join(i)
			mazeMap += "\n"
		return mazeMap
	#print(mazeLines)

	def __init__(self):
		self.plots = []
		self.createArray(self.plots)
		#print(self.plots)

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 

    def add_edge(self, u, v): 
        self.graph[u].append(v) 

def checkNorth(arr, line, point):
	try:
		if(arr[line-1][point] != "%"):
			#print("NCoords: " + str(line) + "," + str(point))
			v1 = (line * len(arr[0])) + point
			v2 = ((line-1) * len(arr[0])) + point
			#print(str(v1) + "," + str(v2))
			g.add_edge(v1,v2)
	except:
		return

def checkSouth(arr, line, point):
	try:
		if(arr[line+1][point] != "%"):
			#print("SCoords: " + str(line) + "," + str(point))
			v1 = (line * len(arr[0])) + point
			v2 = ((line+1) * len(arr[0])) + point
			#print(str(v1) + "," + str(v2))
			g.add_edge(v1,v2)
	except:
		return

def checkWest(arr, line, point):
	try:
		if(arr[line][point-1] != "%"):
			#print("WCoords: " + str(line) + "," + str(point))
			v1 = (line * len(arr[0])) + point
			v2 = (line * len(arr[0])) + point - 1
			#print(str(v1) + "," + str(v2))
			g.add_edge(v1,v2)
	except:
		return

def checkEast(arr, line, point):
	try:
		if(arr[line][point+1] != "%"):
			#print("ECoords: " + str(point) + "," + str(point))
			v1 = (line * len(arr[0])) + point
			v2 = (line * len(arr[0])) + point + 1
			#print(str(v1) + "," + str(v2))
			g.add_edge(v1,v2)
	except:
		return

def breadth_first_search(graph, initial):
	nodeCount = 0
	visited = [False] * (len(m.plots)) * (len(m.plots[0]))
	poppedNodes = []

	queue = []
	queue.append(initial)
	visited[initial] = True

	while queue:
		poppedNodes.append(queue[0])
		initial = queue.pop(0)
		nodeCount += 1
		#print (initial, end = " ")

		if(initial == goalState):
			print("We did it!")
			print(nodeCount)
			break

		for n in graph.graph[initial]:
			if visited[n] == False:
				queue.append(n)
				visited[n] = True

	poppedNodes.pop(0)
	poppedNodes.pop(len(poppedNodes)-1)
	return poppedNodes

def DFSUtil(graph, v, visited): 

	visited[v] = True
	print(v, end = ' ')

	# Recur for all the vertices  
	# adjacent to this vertex 
	for i in graph.graph[v]: 
	    if visited[i] == False: 
	        DFSUtil(graph, i, visited)

# The function to do DFS traversal. It uses 
# recursive DFSUtil() 
def depth_first_search(graph, v): 

    # Mark all the vertices as not visited 
    visited = [False] * (len(m.plots)) * (len(m.plots[0]))

    # Call the recursive helper function  
    # to print DFS traversal 
    DFSUtil(graph, v, visited)

m = Maze()
g = Graph()

initialState = 0
goalState = 0

for line in range(len(m.plots)):
	for point in range(len(m.plots[0])):
		if(m.plots[line][point] != "%"):
			checkNorth(m.plots, line, point)
			checkSouth(m.plots, line, point)
			checkEast(m.plots, line, point)
			checkWest(m.plots, line, point)
		if(m.plots[line][point] == "."):
			initialState = (line * len(m.plots[0])) + point
		if(m.plots[line][point] == "P"):
			goalState = (line * len(m.plots[0])) + point

#print("Initial: " + str(initialState))
#print("Goal: " + str(goalState))


bfsArr = breadth_first_search(g, initialState)
#bfsArr = depth_first_search(g, initialState)

bfsMaze = Maze()
count = 0


for i in bfsArr:
	line = i //len(bfsMaze.plots[0])
	point = i % len(bfsMaze.plots[0])
	bfsMaze.plots[line][point] = "_"
	#print("Coords: " + str(line) + "," + str(point))

print(bfsMaze)


'''
for v in g:
	for w in v.get_connections():
		print('{} -> {}'.format(v.key, w.key))

for v in g:
	print(v)
'''





