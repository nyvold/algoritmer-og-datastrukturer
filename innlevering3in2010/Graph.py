from collections import defaultdict
import csv

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

def main():

    testg = Graph("marvel_movies", "marvel_actors")
    # num_nodestest = len(testg.v)
    # num_edgestest = sum(len(adj_list) for adj_list in testg.e.values()) // 2

    g = Graph("movies", "actors")

    num_nodes = len(g.v)
    num_edges = sum(len(adj_list) for adj_list in g.e.values()) // 2

    print(f"nodes: {num_nodes}")
    print(f"edges: {num_edges}")

    

main()