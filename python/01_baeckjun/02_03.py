#if -3
year = int(input())
if year % 4 == 0 and year % 100!= 0 or year % 400 == 0:print(1)
else:print(0)

#
year = int(input())
if year % 400 == 0:
    print(1)
elif year % 4 == 0:
    if year % 100!= 0:
        print(1)
    else:
        print(0)
else:
    print(0)
    