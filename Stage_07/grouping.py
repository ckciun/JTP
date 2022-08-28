## grouping ()
import re
p = re.compile('(ABC)+')
m = p.search('ABCABCABC')
print(m)
print(m.group())
