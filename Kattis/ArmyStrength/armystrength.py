import sys;import re

n = int(sys.stdin.readline())

for i in range(n):
    empty = sys.stdin.readline()
    ngm = sys.stdin.readline().strip().split(" ")
    ng = ngm[0]
    nm = ngm[1]

    ngMonsters = sys.stdin.readline().strip().split(" ")
    ngMonsters = list(map(int, ngMonsters))
    nmMonsters = sys.stdin.readline().strip().split(" ")
    nmMonsters = list(map(int, nmMonsters))
    ngMonsters.sort()
    nmMonsters.sort()

    warDone = False
    while(not warDone):    
        ngWeakest = ngMonsters[0]
        nmWeakest = nmMonsters[0]

        if(ngWeakest == nmWeakest):
            nmMonsters.remove(nmWeakest)
        elif(ngWeakest > nmWeakest):
            nmMonsters.remove(nmWeakest)
        else:
            ngMonsters.remove(ngWeakest)

        ngStr = sum(ngMonsters)
        nmStr = sum(nmMonsters)

        if(ngStr == 0 and nmStr == 0):
            print("uncertain")
            warDone = True
        elif(nmStr == 0):
            print("Godzilla")
            warDone = True
        elif(ngStr == 0):
            print("MechaGodzilla")
            warDone = True

    
