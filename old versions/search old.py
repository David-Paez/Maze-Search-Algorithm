class Maze:
	mazeLines = []
	plots = []

	def createArray(mL, p):
		f = open("Maze2.txt","r")
		for x in f:
			mL.append(x.rstrip('\n'))
		for x in mL:
			temp = []
			for i in x:
				temp.append(i)

			p.append(temp)


	createArray(mazeLines, plots)

	def __str__(self):
		for i in self.plots:
			print(''.join(i))
	#print(mazeLines)
	#print(plots)

class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def __str__(self):
        return '{} neighbors: {}'.format(
            self.key,
            [x.key for x in self.neighbors]
        )

    def get_connections(self):
        return self.neighbors.keys()

    def get_weight(self, neighbor):
        return self.neighbors[neighbor]

class Graph(object):
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex.key] = vertex

    def get_vertex(self, key):
        try:
            return self.vertices[key]
        except KeyError:
            return None

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, from_key, to_key, weight=1):
        if from_key not in self.vertices:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.vertices:
            self.add_vertex(Vertex(to_key))
        self.vertices[from_key].add_neighbor(self.vertices[to_key], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

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
	visited = [False] * (len(graph.vertices))
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
			
		for v in graph:
			for w in v.get_connections():
				queue.append(w.key)
				visited[w.key] = True

	poppedNodes.pop(0)
	poppedNodes.pop(len(poppedNodes)-1)
	return poppedNodes

def DFSUtil(self, v, visited): 

    # Mark the current node as visited  
    # and print it 
    visited[v] = True
    print(v, end = ' ') 

    # Recur for all the vertices  
    # adjacent to this vertex 
    for i in self.graph[v]: 
        if visited[i] == False: 
            self.DFSUtil(i, visited) 

# The function to do DFS traversal. It uses 
# recursive DFSUtil() 
def DFS(self, v): 

    # Mark all the vertices as not visited 
    visited = [False] * (len(self.graph)) 

    # Call the recursive helper function  
    # to print DFS traversal 
    self.DFSUtil(v, visited)

m = Maze()
g = Graph()

initialState = 0
goalState = 0

for i in range(len(m.plots) * len(m.plots[0])):
	g.add_vertex(Vertex(i))

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

bfsMaze = Maze()
count = 0

for i in bfsArr:
	line = i //len(bfsMaze.plots[0])
	point = i % len(bfsMaze.plots[0])
	bfsMaze.plots[line][point] = "."
	#print("Coords: " + str(line) + "," + str(point))

print(bfsMaze)
'''
for v in g:
	for w in v.get_connections():
		print('{} -> {}'.format(v.key, w.key))

for v in g:
	print(v)
'''





