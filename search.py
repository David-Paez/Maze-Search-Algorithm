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
        self.verticies = {}

    def add_vertex(self, vertex):
        self.verticies[vertex.key] = vertex

    def get_vertex(self, key):
        try:
            return self.verticies[key]
        except KeyError:
            return None

    def __contains__(self, key):
        return key in self.verticies

    def add_edge(self, from_key, to_key, weight=1):
        if from_key not in self.verticies:
            self.add_vertex(Vertex(from_key))
        if to_key not in self.verticies:
            self.add_vertex(Vertex(to_key))
        self.verticies[from_key].add_neighbor(self.verticies[to_key], weight)

    def get_vertices(self):
        return self.verticies.keys()

    def __iter__(self):
        return iter(self.verticies.values())

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


m = Maze()
g = Graph()

row = 0;

for i in range(len(Maze.plots) * len(Maze.plots[0])):
	g.add_vertex(Vertex(i))

for line in range(len(Maze.plots)):
	for point in range(len(Maze.plots[0])):
		if(Maze.plots[line][point] != "%"):
			checkNorth(Maze.plots, line, point)
			checkSouth(Maze.plots, line, point)
			checkEast(Maze.plots, line, point)
			checkWest(Maze.plots, line, point)

for v in g:
	for w in v.get_connections():
		print('{} -> {}'.format(v.key, w.key))






