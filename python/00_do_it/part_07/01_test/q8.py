f = open("abc.txt", "r")
s = ""

while True:
    lines = f.readline()
    if not lines:
        break
    s = lines + s
f.close()

f = open("abc.txt", "w")
f.write(s)
f.close()