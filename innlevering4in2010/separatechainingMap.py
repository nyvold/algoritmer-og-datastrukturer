#innlevering4

class separatechainingMap:
    load_factor_threshold = 0.75
    def __init__(self):
        self.arr = [None] * 100_000 #vurder å sette det lik load factor tak, altså 0.75
    
    # Innsetting: gitt en nøkkel k som hasher til i, og en verdi v
	# 1. La B ← A[i] 
	# 2. Hvis B er null, opprett en liste og sett inn (k, v) 
	# 3. Ellers settes (k, v) inn på slutten av B 
    #     • Hvis det finnes en node med nøkkel k på veien, erstattes verdien med v
    def __setitem__(self, k: int, v: int): #k er key og v er value
        if self.arr[k] is None:
            self.arr[k] = []
            self.arr[k].append((k, v))
        
    
    def remove():
        pass

    def contains():
        pass

    #__len__ liksom
    def size():
        pass
    # separate chaining
    def hashFunction_sc():
        pass
