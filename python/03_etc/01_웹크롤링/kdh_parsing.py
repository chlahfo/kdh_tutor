import re
compiler = re.compile("[\" ]https://.*?[\" ]")
f = open("parsing_data.txt", "r", encoding = 'UTF-8')
lines = f.readlines()
for line in lines:
    search = compiler.findall(line)
    for i in search:
        print(i)
f.close()