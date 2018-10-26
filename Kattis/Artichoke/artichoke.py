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

#print("p = ", p, " a = ", a, " b = ", b, " c = ", c, " d = ", d, " k = ", k)
topValue = 0
highestDecline = 0 
for x in range(1, k+1):
    priceX = (p*(math.sin(a*x+b)+math.cos(c*x+d)+2))
    #print("PriceX = ", priceX, " x = ", x)
    if x>1:
        if(priceX > topValue):
            #print("price greater replace ", priceX, " > ", topValue)
            topValue = priceX
        elif((topValue-priceX) > highestDecline):
            #print("Higher decline, ", topValue, " - ", priceX, " = ", topValue-priceX, " < ", highestDecline)
            highestDecline = topValue-priceX
    else:
        #print("FirstCase")
        topValue = priceX


print(highestDecline)