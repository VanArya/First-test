import mymodule as mym

mym.greeting("sen")
mym.zarb(17)
x = mym.P1["age"]
print(x)

import datetime

x = datetime.datetime.now()
print(x.year)

import math

f = math.sqrt(64)
print(int(f))

import re

x = "naser very GAV"
y = re.search("alil", x)
if y:
    print("HA")
else:
    print("NA")

import re

x = "ali very GAV and Sag"
y = re.findall("a", x)
print(y)

import re

x = "ali very GAV and Sag"
y = re.sub("a", "", x, 3)
print(y)

import camelcase

c = camelcase.CamelCase()
x = "ali az sag kamtar ast"
print(c.hump(x))