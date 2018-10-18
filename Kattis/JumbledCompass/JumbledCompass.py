import sys
import math

current = int(sys.stdin.readline())
correct = int(sys.stdin.readline())

clockwise = 0
counterClock = 0

if current < correct:
    clockwise = correct - current
    counterClock = -(current+(360-correct))
else:
    clockwise = (360-current)+correct
    counterClock = -(current-correct)

result = clockwise
if(-counterClock < clockwise):
    result = counterClock

if(result == -180):
    result = 180

print(result)