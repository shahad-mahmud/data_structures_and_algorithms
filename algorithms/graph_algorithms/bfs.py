graph = {}
visited = []  # keep track of visited nodes

def add_edge(a, b):
    if a in graph.keys():
        graph[a].append(b)
    else:
        graph[a] = [b]
    
    # if bidirectional add other also



def bfs(start_node):
    queue = []

    queue.append(start_node)
    visited.append(start_node)

    while queue:
        front_node = queue.pop(0)

        print(front_node)

        for n in graph[front_node]:
            if n not in visited:
                visited.append(n)
                queue.append(n)


add_edge(0,1)
add_edge(0,2)
add_edge(1,2)
add_edge(2,1)
add_edge(3,2)
add_edge(2,3)

print(graph)
bfs(0)