import re
li = []
ki = []
with open("mac.txt") as fo:
    zoo = fo.readlines()
    f1 = open("sorted.txt", "w+")
    for rec in zoo:
        li += rec.split()
    pattern = re.compile(r"\w\w[-]\w\w[-]\w\w[-]\w\w[-]\w\w[-]\w\w")
    for k in li:
        matches=pattern.finditer(k)
        for match in matches:
            ki.append(match.group(0))
    print("mac address present in text file is=")
    print(ki)
    for j in ki:
        f1.write(j+"\n")

