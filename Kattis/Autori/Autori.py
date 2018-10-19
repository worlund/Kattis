import sys;import re

print(re.sub(r'[a-z]*-?',"",sys.stdin.readline()).strip())

