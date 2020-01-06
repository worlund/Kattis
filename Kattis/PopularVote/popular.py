import sys

t = int(sys.stdin.readline())

for case in range(t):
	candidates = int(sys.stdin.readline())
	votes = [0]*candidates
	for c in range(candidates):
		votes[c] = int(sys.stdin.readline())

	even = 0
	highest = -1
	leader = 0
	for i in range(len(votes)):
		if votes[i] > highest:
			even = 0
			highest = votes[i]
			leader = i
		elif votes[i] == highest:
			even = 1

	if even == 1:
		print("no winner")
	elif votes[leader] > sum(votes)//2:
		print("majority winner ",leader+1)
	else:
		print("minority winner ", leader+1)