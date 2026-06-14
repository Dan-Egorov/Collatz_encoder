import coder as cd
import decode as dc
moving = int(input("Moving: "))
n = float(input("Dever: "))

table = {5: "A", 21: "B", 84: "C", 10: "D",  40: " "}

codes = []
while True:
    numb = int(input("Numb: "))
    if numb == -1:
        break
    print(cd.coder(numb, moving, n)[0], "".join(map(str, cd.coder(numb, moving, n)[1])))
    codes.append(cd.coder(numb, moving, n))
input()

for i in codes:
    print(table[dc.decode(i[1], i[0], moving, n)], end="")