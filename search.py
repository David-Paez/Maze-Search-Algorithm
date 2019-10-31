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
	
	queue = []
	queue.append(initial)
	visited[initial] = True

	while queue:
		initial = queue.pop(0)
		nodeCount += 1
		#print (initial, end = " ")

		if(initial == goalState):
			print("We did it!")
			print(nodeCount)
			return

		for v in g:
			for w in v.get_connections():
				queue.append(w.key)
				visited[w.key] = True
		'''
		for i in graph.get_vertex(initial).get_connections():
			if visited[i] == False:
				queue.append(i)
				visited[i] = True
		'''

m = Maze()
g = Graph()

initialState = 0
goalState = 0

for i in range(len(Maze.plots) * len(Maze.plots[0])):
	g.add_vertex(Vertex(i))

for line in range(len(Maze.plots)):
	for point in range(len(Maze.plots[0])):
		if(Maze.plots[line][point] != "%"):
			checkNorth(Maze.plots, line, point)
			checkSouth(Maze.plots, line, point)
			checkEast(Maze.plots, line, point)
			checkWest(Maze.plots, line, point)
		if(Maze.plots[line][point] == "."):
			initialState = (line * len(Maze.plots[0])) + point
		if(Maze.plots[line][point] == "P"):
			goalState = (line * len(Maze.plots[0])) + point

#print("Initial: " + str(initialState))
#print("Goal: " + str(goalState))
breadth_first_search(g, initialState)
'''
for v in g:
	for w in v.get_connections():
		print('{} -> {}'.format(v.key, w.key))

for v in g:
	print(v)
'''





