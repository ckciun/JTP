## 전방탐색: 긍정형 (?=)
import re

# p = re.compile(".+:")
# m = p.search("http://google.com")
# print(m.group())

## 검색 조건에는 포함되지만 결과에선 제외시킨다.
## (?=[제외시킬 값])

# p = re.compile(".+(?=:)")
# m = p.search("http://google.com")
# print(m.group())

## 전방탐색: 부정형 (?!)
## 동일한 조건을 탐색할 때, 특정 문자가 포함된 문장을 결과에서 제외시킨다.

p = re.compile(".*[.](?!bat$).*$", re.M)
l = p.findall("""
autoexec.exe
autoexec.bat
autoexec.jpg
""")
print(l)
