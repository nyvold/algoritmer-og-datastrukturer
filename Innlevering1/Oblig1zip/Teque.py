# Teque
from collections import deque
import sys

class Teque:
    def __init__(self):#kontruktør
        self.front = deque()
        self.back = deque()

    def push_front(self, nyElem):#setter nytt element i front
        self.front.appendleft(nyElem)
        self.rett_opp()
    
    def push_back(self, nyElem):#setter nytt element bakerst
        self.back.append(nyElem)
        self.rett_opp()

    def push_middle(self, nyElem):#setter nytt element bakerst i front listen, som vil bli midten siden det er foran "back" og bak "front"
        self.front.append(nyElem)
        self.rett_opp()
    
    #hjelpemetode
    def rett_opp(self): #må balansere listen hvis det er høyre eller venstre "tungt", eller front eller back "tungt"
        if(len(self) == 1 and len(self.back) == 0):
            return
        if (len(self.front) - len(self.back)) <= -1:
            self.front.append(self.back.popleft())
        if (len(self.front) - len(self.back)) > 1:
            self.back.appendleft(self.front.pop())
    
    def __getitem__(self, index):#get() metode for Teque
        if index < len(self.front):
            return self.front[index]
        return self.back[index - len(self.front)]

    def __len__(self):#len() metode til tequeen
        return len(self.front) + len(self.back)

def main():
    inp = int(sys.stdin.readline())

    tq = Teque()

    output = []

    for i in range(inp):
        inpu = sys.stdin.readline()
        strengArr = inpu.split()
        intInp = int(strengArr[1])
        strengInp = strengArr[0]

        if strengInp == "push_back":
            tq.push_back(intInp)
        elif strengInp == "push_front":
            tq.push_front(intInp)
        elif strengInp == "push_middle":
            tq.push_middle(intInp)
        elif strengInp == "get":
            # print(tq[intInp])  #hvis output skal komme med engang get() blir kalt
            output.append(tq[intInp])
    
    print("\noutput:")
    for i in output:#gjør slik at alt output blir skrevet ut samtidig og ikke bare når get() blir kalt
        print(i)

    fil = open(f"teque_results_{inp}.csv", "w")
    for line in output:
        fil.write(f"{line}\n")
    fil.close()
    
main()