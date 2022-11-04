import sys
import re
dec={
        ".- ":"A",
        "-... ":"B",
        "-.-. ":"C",
        "-.. ": "D",
        ". ":"E",
        "..-. ":"F",
        "--. ":"G",
        ".... ":"H",
        ".. ":"I",
        ".--- ":"J",
        "-.- ":"K",
        ".-.. ":"L",
        "-- ":"M",
        "-. ":"N",
        "--- ":"O",
        ".--. ":"P",
        "--.- ":"Q",
        ".-. ":"R",
        "... ":"S",
        "- ":"T",
        "..- ":"U",
        "...- ":"V",
        ".-- ":"W",
        "-..- ":"X",
        "-.-- ":"Y",
        "--.. ":"Z"
    }
s=".... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--"
s=s+" "

p=re.compile("[.-]+\s*")
m=p.findall(s)
for i in m:
    if i in list(dec.keys()):
        s=s.replace(i, dec.get(i), 1)
    elif i.replace("  ", " ") in list(dec.keys()):
        s=s.replace(i, str(dec.get(i.replace("  "," ")))+" ", 1)
print(s)
