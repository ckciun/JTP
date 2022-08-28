## |(OR)
import re
# p = re.compile('Crow|Servo')
# m = p.match('CrowHello')
# print(m)

# ## ^(Start)
# print(re.search('^Life', 'Life is too short'))
# print(re.search('^Life', 'My Life'))

# ## $(End)
# print(re.search('short$', 'Life is too short'))
# print(re.search('short$', 'Life is too short, you need python'))

## \b(Space)
p = re.compile(r'\bclass\b')
print(p.search('no class at all'))
print(p.search('the declassified algorithm'))
print(p.search('one subclass is'))
