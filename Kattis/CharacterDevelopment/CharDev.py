import sys
import math

def fact(n):
    if(n == 0):
        return 1
    else:
        return n*fact(n-1)

n = int(sys.stdin.readline())
result = 0

if(n > 1):
    for k in range(2, n+1):
        result += math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

print(int(result))
