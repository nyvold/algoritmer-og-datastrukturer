#her kan tuples settes inn og fjernes, ikke lik oblig der bare en verdi skal settes inn og fjernes
class hashTableSC:
    def __init__(self):
        self.n = 0 #ant element
        self.N = 10 #størrelse på hashtable 
        self._hashtable = [None for _ in range(self.N)] #separate chaining hashtable

    def size(self):
        pass

    def insert(self, k, v): #k for key og v for value
        i = self.hash(k) #finner indeks vi skal sette key og value inn på ved på hashe key

        if self._hashtable[i] == None: #hvis indeks i er tom, settes den lik en tom liste eller "bucket" og vi legger til key og value til den listen
            self._hashtable[i] = []
        
        for j in range(len(self._hashtable[i])): 
            kj, vj = self._hashtable[i][j] #kj for keyJ og vj for valueJ
            if kj == k: #vi sjekker om vi allerede har samme key i bucketen, hvis vi har det erstatter vi den gamle verdien med den nye
                self._hashtable[i][j] = (k, v)
                return
        
        self.n += 1 #plusser på size
        self._hashtable[i].append((k, v)) #legger til key og value inn i riktig bucket
        

    def remove(self, k): #k for key
        i = self.hash(k)

        if self._hashtable[i] == None:
            return
        
        for j in range(len(self._hashtable[i])): 
            kj, vj = self._hashtable[i][j] #kj for keyJ og vj for valueJ
            if kj == k: #hvis vi finner en nøkkel som er lik k, sletter vi elementet som har den nøkkelen
                self._hashtable[i].pop(j)
                if len(self._hashtable[i]) == 0:#hvis bucketen på indeks i blir tom av å slette elementet settes element på indeks i lik None så ting blir riktig
                    self._hashtable[i] = None
                return #returnerer hvis vi fikk slettet et element fordi vi trenger ikke sjekke mer

    def contains(self, k): #k for key
        i = self.hash(k) #hasher k til i så vi kan slå opp på indeks i og sjekke det vi skal sjekke
        #i for indeks
        if self._hashtable[i] == None: #hvis indeks i er None så returerer vi false fordi vi fant ikke keyen vi leter etter
            return False
        
        for ck, _ in self._hashtable[i]: #ck for checkedkey, _ for value som vi ikke bruker, vi sjekker alle keys på indeks i og hvis en matcher med arguementet returnerer vi true
            if ck == k:
                return True
        return False #returerer false siden vi ikke fant en key som matches argumentet på indeks i

    def hash(self, k: int) -> int: #k for key
        return k % self.N

