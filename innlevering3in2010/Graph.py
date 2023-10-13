from collections import defaultdict, deque
import csv
# import graphviz

class Graph:

    def __init__(self, filename_movies, filename_actors):
        self.movies = {}
        self.actors = {}
        self.v, self.e, self.w = self.buildgraph(f"filer/{filename_movies}.tsv", f"filer/{filename_actors}.tsv")

    def buildgraph(self, moviefilepath: str, actorfilepath: str) -> tuple:
        v = set() #vertices(noder)
        e = defaultdict(set) #edges
        w = dict() #weights

        with open(f"{moviefilepath}", "r") as file:
            tsvReadermovie = csv.reader(file, delimiter="\t")

            for row in tsvReadermovie:
                ttid, title, rating, _ = row
                self.movies[ttid] = {"title":title, "rating":rating}
                v.add(ttid)
        # file.close()
        
        with open(f"{actorfilepath}", "r") as file:
            tsvReaderactor = csv.reader(file, delimiter="\t")

            for row in tsvReaderactor:
                nmid, name, *ttids = row
                v.add(nmid)
                for ttid in ttids:
                    if not ttid in self.movies:
                        continue
                    self.actors[nmid] = {"name":name, "ttid":set([ttid.strip() for ttid in ttids])}
                    e[nmid].add(ttid)#koble actor til movie
                    e[ttid].add(nmid)#koble movie til actor
                    w[(nmid, ttid)] = float(self.movies[ttid]["rating"])
                    w[(ttid, nmid)] = float(self.movies[ttid]["rating"])
                    v.add(nmid)
        # file.close()

        return v, e, w 

    def bfs_find_shortestpath_from(self, actor) -> dict:
        _, E, _ = self.v, self.e, self.w
        visited = set()
        parents = {actor : None}
        queue = deque([actor])

        while queue:
            u = queue.popleft()
            for node in E[u]:
                if node not in parents:
                    parents[node] = u
                    queue.append(node)
        return parents
    
    def bfs_shortest_path_between(self, actor1: str, actor2: str) -> list:
        parents = self.bfs_find_shortestpath_from(actor1)
        v = actor2
        path = []

        if actor2 not in parents:
            return path

        while v:
            path.append(v)
            v = parents[v]

        return path[::-1]

    
    def dijkstra(self, actor1, actor2):
        _, e, w = self.v, self.e, self.w
        queue = [(0, actor1)]
        dist = defaultdict(lambda: float('inf'))
        dist[actor1] = 0
        parents = {}

        while queue:
            cost, u = heappop(queue)
            if cost != dist[u]:
                continue

            for node in e[u]:
                c = cost + w[(u, node)]
                if c < dist[node]:
                    parents[node] = u
                    dist[node] = c
                    heappush(queue, (c, node))
        
        path = [actor2]
        weight = 0
        current = actor2
        while current != actor1:
            current = parents[current]
            path.append(current)
        
        return reversed(path), dist[actor2]
    
