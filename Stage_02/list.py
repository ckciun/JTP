# 비슷한 유형의 변수가 많을 경우 list 활용

print('list를 사용하지 않으면 각각의 변수를 만들고 print해야 함')
a = '홍길동'
b = '철수'
c = '영희'

print(a)
print(b)
print(c)
print()

print('list를 사용하면 입출력이 비교적 간단해짐')
d = ['홍길동', '철수', '영희', ['바둑이', '나비']]

print(d)
print()
print('특정 값만 출력하고 싶을땐 indexing 사용')
print(d[0])
print()
print('list안에 list 사용 가능')
print(d[3])
print()
print('list안에 list의 특정 값 출력')
print(d[3][1])

# a = [ ] 빈 값
# b = [1, 2, 3] 숫자형
# c = ['a', 'b', 'c'] 문자형
# d = [1, 'a', 2, 'b'] 숫자형 + 문자형
# e = [1, 2, ['a', 'b']] list 안에 list
