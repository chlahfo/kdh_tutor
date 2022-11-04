import re
import sys
s = sys.stdin.readline().rstrip()
p = re.compile("c=|c-|dz=|d-|lj|nj|s=|z=|\w")
m = p.findall(s)
print(len(m))