## 문자 클래스 []
## [abc]
    ## 'a'는 정규식과 일치하는 'a'가 있으므로 매치
    ## 'before'는 정규식과 일치하는 'b'가 있으므로 매치
    ## 'dude'는 정규식과 일치하는 문자가 없으므로 매치X
    ## 하이픈을 사용하여 From - To로 표현 가능
    ## Ex) [a-c] = [abc], [0-5] = [012345]

## Dot(.)
## a.b
    ## 줄바꿈(\n)을 제외한 모든 문자와 매치
    ## 'aab'는 가운데 문자 'a'가 줄바꿈이 아니므로 매치
    ## 'a0b' 역시 가운데 문자가 줄바꿈이 아니므로 매치
    ## 'abc'는 'a'와 'b' 사이에 문자가 없으므로 매치X
    
## 반복(*)
## ca*t
    ## 'ct'는 'a'가 0번 반복되어 매치
    ## 'cat'는 'a'가 0번 이상(1번) 반복되어 매치
    ## 'caaat'는 'a'가 3번 반복되어 매치
    
## 반복(+)
## ca+t
    ## 'ct'의 경우 반복(*)과는 다르게 0번 반복이면 매치X
    ## 나머지는 같음

## 반복({m,n}, ?)
## ca{2}t
    ## 'cat'는 'a'가 1번만 반복되어 매치X
    ## 'caat'는 'a'가 2번 반복되어 매치
## ca{2, 5}t
    ## 2 이상 5 이하
    ## 'caaaaat'는 'a'가 5번 반복되어 매치
## ab?c
    ## ? == {0, 1}과 같은 표현
    ## 'abc'는 'b'가 1번 사용되어 매치
    ## 'ac'는 'b'가 0번 사용되어 매치

## Match

import re

# p = re.compile('[a-z]+')
# m1 = p.match('python')
# m2 = p.match('1234 python')
# print(m1)
# print(m2)
# print()

# ## Match Method
#     ## .group() == 매치된 문자열을 리턴한다.
#     ## .start() == 매치된 문자열의 시작 위치를 리턴한다.
#     ## .end() == 매치된 문자열의 끝 위치를 리턴한다.
#     ## .span() == 매치된 문자열의 (시작,끝)에 해당되는 튜플을 리턴한다.
    
# print(m1.group())
# print(m1.start())
# print(m1.end())
# print(m1.span())
# print()

# ## Search

# s1 = p.search('python')
# s2 = p.search('1234 python')
# print(s1)
# print(s2)
# print()

# ## FIndall

# f1 = p.findall('lift is too short')
# print(f1)

# ## Finditer

# f2 = p.finditer('lift is too short')
# for r in f2:
#     print(r)

## Compile Option

# p1 = re.compile('a.b')
# p1 = re.compile('[a-z]')
# p1 = re.compile("^python\s\w+")
#     ## ^ == ^뒤에 있는 문자가 시작문자.
#     ## \s == 공백.
#     ## \w == word
# p1 = re.compile(r'&[#](0[0-7])+|[0-9]+|X[0-9a-fA-F]+);')

#     ## DOTALL, S
#     ## \n이 포함되어 있어도 결과 출력

# p2 = re.compile('a.b', re.DOTALL)
#     ## OR p2 = re.compile('a.b', re.S)
# m1 = p1.match('a\nb')
# m2 = p2.match('a\nb')

# print(m1)
# print(m2)

#     ## IGNORECASE, I
#     ## 대소문자를 무시하고 출력

# p2 = re.compile('[a-z]', re.I)
# print(p1.match('python'))
# print(p1.match('Python'))
# print(p1.match('PYTHON'))
# print()
# print(p2.match('python'))
# print(p2.match('Python'))
# print(p2.match('PYTHON'))

#     ## MULTILINE, M
#     ## 동일한 조건이 존재한다면 첫 번째만 출력하지 않고 모두 출력.

# p2 = re.compile("^python\s\w+", re.M)

# data = """python one
# lift is too short
# python two
# you need python
# python three
# hello python world"""

# print(p1.findall(data))
# print(p2.findall(data))

#     ## VERBOSE, X
#     ## 정규표현식의 길이가 길 때, 나눠서 표현.
    
# p2 = re.compile(r"""
# &[#]                # Start of a numberic entiry reference
# (
#     0[0-7])+        # Octal from
#     |[0-9]+         # Decimal from
#     |X[0-9a-fA-F]+  # Hexadecimal from
# )
# ;                   # Trailing semicolon
# """, re.X)
