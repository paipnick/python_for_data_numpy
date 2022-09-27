import re

L = ["python practice", "workearly training"]
for element in L:
      z = re.match("(p\w+)\W(p\w+)", element)
      if z:
          print((z.groups()))
