import sys
def kattunge():
    # d2 = {25:[24], 4:[3, 1, 2], 13:[9, 4, 11], 10:[20, 8, 7], 32:[10,21], 23:[13,19,32,22], 19:[12,5,14,17,30], 14:[6,15,16], 30:[18,31,29], 24:[23,26], 26:[27,28]}
    kitten = int(input())
    d = {}
    root, *children = map(int, input().split())
    d[root] = children

    inp = "temp"
    while inp != "-1":
        try:
            inp, *values = map(int, input().split())
        except ValueError:
            break
        d[inp] = values

    path = []    
    path.append(kitten)
    temp = kitten
    while not root in path:
        for key, value in d.items():
            for c in value:
                if c == temp:
                    temp = key
                    path.append(temp)
    
    string = " ".join(f"{node}" for node in path)
    print(string)
    

def main():
    kattunge()
main()
