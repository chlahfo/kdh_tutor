import re
s="""
park 010-9999-9988
kim 010-9909-7789
lee 010-8789-7768
"""
p = re.compile(r"([\d]+[-])([\d]+[-])([\d]+)")
m = p.findall(s)
print(p.sub("\g<1>\g<2>####", s))