graph = {
  'S' : ['A','B'],
  'A' : ['C', 'D'],
  'B' : ['G','H'],
  'C' : ['E','F'],
  'D' : [],
  'G' : ['I'],
  'H' : [],
  'E' : ['K'],
  'F' : [],
  'I' : [],
  'K' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue
visited1 = set()

def dfs(visited1, graph, node):
    if node not in visited1:
        print(node,end=" ")
        visited1.add(node)
        for neighbour in graph[node]:
            dfs(visited1, graph, neighbour)

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s,end=" ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("BFS Traversal: ",end=" ")
bfs(visited, graph, 'S')
print()

# visited.clear()
print("DFS Traversal: ",end=" ")
dfs(visited1, graph, 'S')
print()
