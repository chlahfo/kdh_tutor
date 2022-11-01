#후방탐색 (인터넷 내용 추가) (?<=)
import re
p = re.compile("(?<=\$)[0-9.]+")
m = p.findall("""
ABC01: $23.45
HGG42: $5.31
CFMX1: $899.00
XTC99: $69.96
Total items found: 4
""", re.M)
print(m)