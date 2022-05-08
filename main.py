import re
def disemvowel(string_):
    print(re.sub(r"[aAuUiIeEoO]","", string_))

print(disemvowel("ThE qUicK bRoWn fOx JuMpA ovEr ThE lAzY Dog"))
#link = https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python