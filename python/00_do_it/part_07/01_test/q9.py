import re
f = open("sample.txt", "r")
bal = 0

s = f.read()
f.close()

cp = re.compile("[\d]+")
nums= cp.findall(s)
nums = list(map(int, nums))
sums = sum(nums)
bal = sums / len(nums)

f = open("result.txt", "w")
f.write(str(bal))
f.close()