
class Binaryheap:
    
    def __init__(self):
        root = self.arr[0]
        arr = []

    def insert(self, v: int):
        self.arr[len(self.arr)-1] = v #legger nytt element sist i heapen
        i = len(self.arr)-1 #i peker på siste indeks i heapen
        while i > 0 and self.arr[i] < self.arr[self.parentOf(i)]:#while i er større enn 0 og mindre en foreldrenoden til i
            self.arr[i], self.arr[self.parentOf(i)] = self.arr[self.parentOf(i)], self.arr[i] #swapper element på indeks i og element som er foreldrenoden til i
            i = self.parentOf(i) #i endres til foreldrenoden av i, altså det som ble swappet
    
    def removeMin(self):
        removed = self.arr[0]#husker det slettede elementet
        self.arr[0] = self.arr.pop() #swapper root og siste element og sletter det som var root, altså minste element
        i = 0
        while self.rightOf(i) < len(self.arr)-1:#mens i har et høyrebarn, altså vi er ikke utfor arrayet og vi har garantert et venstrebarn
            j = self.arr[self.leftOf(i)] if self.arr[self.leftOf(i)] <= self.arr[self.rightOf(i)] else self.arr[self.rightOf(i)]
            #^^^ variabelen j blir hva som er det minst av venstre eller høyre barn
            if self.arr[j] > self.arr[i]:#hvis vi har nådd riktig plass for elementet så stopper vi
                break
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]#swapper element på indeks i og element på indeks j
            i = j #i pekes til j
        if self.leftOf(i) < len(self.arr) and self.arr[self.leftOf(i)] <= self.arr[i]:
            #^^hvis vi ikke har et høyrebarn lenger, men vi må fortsatt sjekke om barnet er mindre enn elementet
            self.arr[i], self.arr[self.leftOf(i)] = self.arr[self.leftOf(i)], self.arr[i]
        
        return removed#returerer det slettede elementet
        
        
    def removeMinselvimplementert(self) -> int:
        i = 0 #i starter på root, settes lik 0 fordi element på indeks 0 er root
        self.arr[0], self.arr[len(self.arr)-1] = self.arr[len(self.arr)-1], self.arr[0]# swapper root, altså minste elementet med det siste elementet i heapen
        while self.arr[i] > self.leftOf(i) or self.arr[i] > self.rightOf(i):#while element på indeks i er større enn venstre eller høyre barnenode
            if self.arr[i] > self.arr[self.leftOf(i)]:#hvis element på indeks i er større enn venstrebarn så swappes de og i pekes til venstrebarn
                self.arr[i], self.arr[self.leftOf(i)] = self.arr[self.leftOf(i)], self.arr[i]
                i = self.leftOf(i)
            elif self.arr[i] > self.arr[self.rightOf(i)]:#hvis element på indeks i er større enn høyrebarn så swappes de og i pekes på høyrebarn
                self.arr[i], self.arr[self.rightOf(i)] = self.arr[self.rightOf(i)], self.arr[i]
                i = self.rightOf(i)
        return self.arr.pop() #popper minste element og returnerer det


    def parentOf(i: int) -> int:
        return i-1//2
    
    def leftOf(i: int) -> int:
        return 2*i+1
    
    def rightOf(i: int) -> int:
        return 2*i+2
