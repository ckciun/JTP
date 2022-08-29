## 문자열 바꾸기 sub

import re
# p = re.compile('(blue|white|red)')
# print(p.sub('colour', 'blue socks and red shoes'))

## Greedy vs Non-Greedy

s = '<html><head><title>Title</title>'
print(re.match('<.*>', s).group())  #Greedy
print(re.match('<.*?>', s).group()) #Non-Greedy
