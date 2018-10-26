import sys
import math

current = int(sys.stdin.readline())
seedlings = sys.stdin.readline().strip().split(" ")
seedlings = list(map(int, seedlings))
seedlings.sort(reverse=True)

days = 0
prev = 0
time = 0

for i in range(len(seedlings)):
    days += 1
    #print("days = ", days, " seed[i] = ", seedlings[i], " time = ", time)
    if(days+seedlings[i] > time):
        #print("inif")
        time += abs(seedlings[i]+days-time)
        prev = seedlings[i]
    ##print(seedlings[i], " ", time)

time += 1
##print("final days = ", days, " final time = ", time)
print(time)