# Python의 반복문은 while과 for 두 개
# for 기본 구조
# for <variable> in <string> | <list> | <tuple> | <dictionary>
#     수행할 명령어

# list

_l = [1, 2, 3]
for i in _l:
    print(i)
print()

# tuple

_lt = [(1, 2), (3, 4), (5, 6)]
for _left, _right in _lt:
    print(_left, _right)
print()

# dictionary

_d = {
    '1' : 'one',
    '2' : 'two',
    '3' : 'three'
}

# key만 출력

for _key in _d.keys():
    print(_key)
print()

# value만 출력

for _value in _d.values():
    print(_value)
print()

# key와 value 모두 출력

for _k, _v in _d.items():
    print(_k, _v)
print()

# range
#         범위 시작, 끝, (간격)
for i in range(1, 11):
    print(i)
print()

# len() 활용

_l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(_l)):
    print(i + 1)
print()

## 응용 ##
# for문 한 줄로 만들기

result = []
for num in _l :
    if num % 2 == 0:
        result.append(num * 3)
print(result)
print()

result = [num * 3 for num in _l if num % 2 == 0]
print(result)
print()

# 이중 for문으로 구구단 만들기

_a = 10

for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end = " ")
    print(' ')
print()