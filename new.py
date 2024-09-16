import re
a="vishu#24@vk.com"
b=re.search("(\w+)#(\w+)@(\w+).(\w+)",a)
print(b.group())
print(b.group(1))
print(b.group(2))
print(b.group(3))
print(b.group(4))