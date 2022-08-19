# 정규표현식이란?
# 복잡한 문자열을 처리할 때 사용하는 기법
# 모든 언어 공통

# 정규표현식이 필요한 이유
# ex_
# 주민등록번호의 뒷 자리를 *로 변경

# 정규표현식 X
data = """
choi 800905-1049118
park 700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

# 정규표현식 O
import re
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))