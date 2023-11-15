import heapq

def prims(graph): #startv for startnode 
    startv = next(iter(graph)) #velge en "vilkårlig" node i grafen, i dette tilfelle første nøkkel i hashmappe
    queue = []
    parents = {}
    heapq.heappush(queue, (None, startv, 0))

    while queue:
        parent, current_node, cost = heapq.heappop(queue)

        if current_node not in parents:
            parents[current_node] = parent

            for neighbor, weight in graph[current_node].items():
                heapq.heappush(queue, (current_node, neighbor, weight))
    return parents


# -----------sjekke at det funke huehue:---------------

graph = {
    'A': {'B': 13, 'C': 6},
    'B': {'A': 13, 'C': 7, 'D': 1},
    'C': {'A': 6, 'B': 7, 'D': 14, 'E': 8, 'H': 20},
    'D': {'F': 3, 'B': 1, 'C': 14, 'E': 9},
    'F': {'D': 3, 'E': 2},
    'E': {'F': 2, 'D': 9, 'C': 8, 'J': 18},
    'J': {'E': 18, 'H': 17, 'G': 19, 'K': 16, 'L': 4},
    'L': {'J': 4, 'K': 12},
    'K': {'L': 12, 'J': 16, 'G': 10, 'I': 11},
    'I': {'K': 11, 'G': 5},
    'G': {'I': 5, 'K': 10, 'J': 19, 'H': 15},
    'H': {'J': 17, 'C': 20, 'G': 15},
    
}

result = prims(graph)
print(result)

