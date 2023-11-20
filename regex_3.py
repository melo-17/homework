import re

text = input()
b = re.sub(r'((?:[01]\d|2[0-3])\:(?:[0-5]\d)(?:\:[0-5]\d)?)', "(TBD)", text)

print(b)