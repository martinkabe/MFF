from collections import deque, defaultdict

def read_data():
    queue = deque()

    inpt = list(map(int, input().split()))
    queue.extend(inpt)
    N = queue.popleft()
    while inpt:
        inpt = list(map(int, input().split()))
        queue.extend(inpt)
    
    list_tuples = []
    cntr = 0
    if len(queue) == (2*N):
        for _ in range(0, len(queue)//2):
            t = ()
            for j in range(2):
                t += (queue[j+cntr],)
            cntr += 2
            list_tuples.append(t)
            # list_tuples.append((t[1], t[0]))
        list_tuples.sort(key=lambda x:x[1])
        return list_tuples
    return None


def DFS(G, v, seen=None, path=None):
   if seen is None: seen = []
   if path is None: path = [v]

   seen.append(v)

   paths = []
   for t in G[v]:
       if t not in seen:
           t_path = path + [t]
           paths.append(tuple(t_path))
           paths.extend(DFS(G, t, seen[:], t_path))
   return paths



data = read_data()
if data is not None:
    G = defaultdict(list)
    for (s,t) in data:
        G[s].append(t)
        G[t].append(s)

    result = [p for ps in [DFS(G, n) for n in set(G)] for p in ps]

    print(result)

# 5  1 2  1 2  2 3  2 17  2 17