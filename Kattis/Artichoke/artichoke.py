import sys
import math

n = sys.stdin.readline().strip().split(" ")
n = list(map(int, n))

p = n[0]
a = n[1]
b = n[2]
c = n[3]
d = n[4]
k = n[5]

res = []
for x in range(1, k+1):
    res.append(p*(math.sin(a*x+b)+math.cos(c*x+d)+2))

res.sort()
print(res[len(res)-1]-res[0])