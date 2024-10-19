from collections import deque, defaultdict

def bfs(capacity, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)
    
    while queue:
        u = queue.popleft()
        
        for v in capacity[u]:
            if v not in visited and capacity[u][v] > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                if v == sink:
                    return True
    return False

def edmonds_karp(capacity, source, sink):
    parent = {}
    max_flow = 0
    
    while bfs(capacity, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
        
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = parent[v]
        
        max_flow += path_flow
    
    return max_flow

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    s = int(data[2])
    p = int(data[3])
    
    capacity = defaultdict(lambda: defaultdict(int))
    
    index = 4
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        c = int(data[index + 2])
        capacity[u][v] += c
        index += 3
    
    source = s
    sink = n
    
    max_voters = edmonds_karp(capacity, source, sink)
    print(min(max_voters, p))

if __name__ == "__main__":
    main()