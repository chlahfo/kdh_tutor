import sys
import re
s = sys.stdin.readline().rstrip()
flt = re.compile("\w+")
m = flt.findall(s)
print(len(m))
