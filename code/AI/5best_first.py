graph= {
'Black':[('Red',4), ('Yellow',1), ('Blue',2)],
'Red':[('Pink',8), ('Orange',6)],
'Yellow':[('Orange',10), ('Green',15)],
'Blue':[('Green',9)],
'Pink':[],
'Orange':[],
'Green':[]
}
def bfs(start, target, graph, queue=[], visited=[]):
    if start not in visited:
        print(start)
        visited.append(start)
    queue=queue+[x for x in graph[start] if x[0][0] not in visited]
    queue.sort(key=lambda x:x[1])
    if queue[0][0]==target:
        print(queue[0][0])
    else:
        processing=queue[0]
        queue.remove(processing)
        bfs(processing[0], target, graph, queue, visited)
bfs('Black','Orange', graph)
