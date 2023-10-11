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

def main():

    testg = Graph("marvel_movies", "marvel_actors")
    # num_nodestest = len(testg.v)
    # num_edgestest = sum(len(adj_list) for adj_list in testg.e.values()) // 2

    g = Graph("movies", "actors")

    num_nodes = len(g.v)
    num_edges = sum(len(adj_list) for adj_list in g.e.values()) // 2

    print(f"nodes: {num_nodes}")
    print(f"edges: {num_edges}")

    print(g.bfs_shortest_path_between("nm2255973", "nm8076281"))

    

main()
