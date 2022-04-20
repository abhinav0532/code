from collections import defaultdict

class Graph:

	def __init__(self):

		self.graph = defaultdict(list)

	def verticies(self, u, v):
		self.graph[u].append(v)

	def utilities(self, v, visited):

		visited.add(v)
		print(v, end=' ')

		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.utilities(neighbour, visited)

	def DeapthFirstSearch(self, v):

		visited = set()

		self.utilities(v, visited)

g = Graph()
g.verticies(0, 2)
g.verticies(0, 4)
g.verticies(2, 4)
g.verticies(4, 0)
g.verticies(4, 3)
g.verticies(5, 5)

print("Following is DeapthFirstSearch from (starting from vertex 2)")
g.DeapthFirstSearch(2)

