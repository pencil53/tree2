from collections import deque

#bfs from given source
def bfs(adj, s):

    #create a queue for BFS
    q = deque()

    #initially mark all the vertices as not visited
    #when we push a vertex into the 1, we mark it as
    #visited
    visited = [False] * len(adj);

    #mark the source node as visited and enqueue it
    visited[s] = True
    q.append(s)

    #iterate over the queue
    while q:

        #dequeue a vertex from queue and print it
        curr = q.popleft()
        print(curr, end=" ")

        #get all adjacent vertices of the dequeued
        #vertex. if an adjacent has not been visited,
        #mark it visited and enqueue it
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

#function to add an edge to the graph
def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

#example usage
if __name__ == "__main__":

    #number of vertices in the graph
    V = 5

    #adjacency list representation of the graph
    adj = [[] for _ in range(V)]

    #add edges to the graph
    add_edge(adj, 0, 1)
    add_edge(adj, 0, 2)
    add_edge(adj, 1, 3)
    add_edge(adj, 1, 4)
    add_edge(adj, 2, 4)

    #perform BFS traversal starting from vertex 