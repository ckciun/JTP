## grouping ()
import re
# p = re.compile('(ABC)+')
# m = p.search('ABCABCABC')
# print(m)
# print(m.group())

# p = re.compile(r'(\w+)\s+\d+[-]\d+[-]\d+')
# m = p.search("park 010-1234-5678")
# print(m.group(1))

# p = re.compile(r'(\b\w+)\s+\1')
# print(p.search('Paris in the the spring').group())

# ## 이름 붙이기 ?P<name>

# p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
# print(p.search('Paris in the the spring').group())

# p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
# m = p.search("park 010-1234-5678")
# print(m.group("name"))

## 전방탐색: 긍정형 (?=)

# p = re.compile(".+:")
# m = p.search("http://google.com")
# print(m.group())

## 검색 조건에는 포함되지만 결과에선 제외시킨다.
## (?=[제외시킬 값])

p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())
