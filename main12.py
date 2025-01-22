from collections import deque

#bfs from given source
def bfs(adj, s, visited):

    q = deque() #create a queue for BFS

   #mark the source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    #iterate over the queue
    while q:
        curr = q.popleft()
        print(curr, end=" ")

        #get all adjacent vertices of curr
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

#function to add an edge to the graph
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)


def bfs_disconnected(adj):
    visited = [False] * len(adj)
    
    for i in range(len(adj)):
        if not visited[i]:
            bfs(adj, i, visited)

#example usage
V = 6
adj = [[] for _ in range(V)]

#edges to the graph
add_edge(adj, 0, 1)
add_edge(adj, 0, 2)
add_edge(adj, 3, 4)
add_edge(adj, 4, 5)

#perform BFS traversal for the entire graph
bfs_disconnected(adj)