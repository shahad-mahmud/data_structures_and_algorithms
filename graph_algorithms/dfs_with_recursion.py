graph = {}
visited = []  # keep track of visited nodes

def add_edge(a, b):
    if a in graph.keys():
        graph[a].append(b)
    else:
        graph[a] = [b]
    
    # if bidirectional add other also



def dfs(node):
    if node not in visited:
        print(node)
        visited.append(node)

        if node in graph.keys():
            for n in graph[node]:
                dfs(n)


add_edge(0,1)
add_edge(1,2)
add_edge(1,5)
add_edge(2,3)
add_edge(0,4)
add_edge(5,6)
add_edge(5,7)
add_edge(7,8)
add_edge(7,9)

print(graph)
dfs(0)