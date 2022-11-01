#컴파일 옵션
#DOTALL, S
import re
p=re.compile("a.b", re.DOTALL|re.IGNORECASE)
m=p.match("a\nb")
print(m.group())

#IGNORECASE, I |re.IGNORECASE
p = re.compile("[a-z]", re.I)
m=p.match("Python")
print(m)

#MULTLINE, M
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

#VERBOSE, X
carref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')

carref = re.compile(r"""
&[#]                    # Start of a numeric entity reference
(
    0[0-7]+             # Octal form
    |[0-9]+             # Decimal form
    |x[0-9a-fA-F]+      # Hexadecimal form
)
;""", re.VERBOSE)       # Trailing semicolon



#MULTLINE, M
p = re.compile("ttt$", re.MULTILINE)

data = """python one ttt
life is too short
python two ttt
you need python
python three ttt"""

print(p.findall(data))