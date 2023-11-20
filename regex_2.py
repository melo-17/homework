import re

text = input()
print(len(re.findall("\w[\w-]*\w*", text)))
