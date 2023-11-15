import heapq


def dijkstra(graph, startv):
    distances = {v: float('inf') for v in graph}#distance til alle noder settes lik evig til å starte med
    queue = [(float('inf'), v) for v in graph]#legger alle noder til prioritetskøen, verdiene blir endret på underveis

    distances[startv] = 0 #setter startnoden sin distance lik 0
    queue.remove((float('inf'), startv)) #fjerner startnoden fra køen og setter inn på nytt med riktig prioritet
    heapq.heappush(queue, (0, startv))

    while queue: #mens køen ikke er tom
        current_distance, current_v = heapq.heappop(queue)

        if current_distance > distances[current_v]:#hopper over hvis vi allerede har en kortere vei til current node
            continue
            
        for node, weight in graph[current_v].items():#for naboer,vekt til current node
            cost = distances[current_v] + weight #veiens vekt fra startnoden til noden vi itererer på
            if cost < distances[node]: #hvis nye veiens vekt er kortere enn den vi hadde så bytter vi på veiene
                distances[node] = cost
                heapq.heappush(queue, (cost, node))
    return distances #returnerer korteste distanse fra startnoden til alle andre noder



# -----------sjekke at det funke huehue:---------------

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
result = dijkstra(graph, start_node)
print(result)