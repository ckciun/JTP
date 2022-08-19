# Python 자체적으로 포함하고 있는 함수

# all
# 모든 값이 참인가
print(all([1, 2, 3]))
print()
print(all([1, 2, 3, 0]))
print()

# any
# 값 중에 참이 포함되어 있는가

print(any([1, 2, 3, 0]))
print()
print(any([0, ""]))
print()

# chr
# ASCII 코드를 문자로 출력

print(chr(97))
print()
print(chr(48))
print()

# dir
# 사용 가능한 변수나 함수 탐색

print(dir([1, 2, 3]))
print()
print(dir({'1':'a'}))
print()

# divmod
# 몫과 나머지를 튜플 형태로 반환

print(divmod(7, 3))
print()

# enumerate
# 열거하다
# 리스트를 dictionary 처럼 index와 value로 나눔

for i, name in enumerate(['First', 'Second', 'Third']):
    print(i, name)
print()

# filter
# 참 값만 반환

# def positive(x):
#     return x > 0

# a = list(filter(positive, [1, -3, 2, 0, -5, 6]))
# print(a)

a = list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
print(a)
print()
