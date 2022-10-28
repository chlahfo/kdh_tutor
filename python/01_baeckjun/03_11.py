#for-11 - impor
import sys
while True:
    try:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        print(a+b)
    except:
        break 