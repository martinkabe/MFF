# https://www.youtube.com/watch?v=ynZdirmZre4

graph = {
    'A': ['B','C','D'],
    'B': ['E'],
    'C': ['D','E'],
    'D': [],
    'E': []
}

visited = set()

def dfs(visited, graph, root):
    if root not in visited:
        print(root, end=" ")
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited, graph, neighbour)

dfs(visited, graph, 'A')