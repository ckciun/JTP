# count

a = "hobby"

print(a)
print("b의 개수는?", end = ' ')
print(a.count('b'))
print()

# find
# 중복된 글자가 있을 경우, 가장 처음 발견한 글자의 위치만 출력
# 찾고자 하는 글자가 없을 경우 -1 출력
# index 함수도 글자의 위치를 탐색하는 함수,
# 찾고자 하는 글자가 없을 경우 에러 발생

print("h의 위치는?", end = ' ')
print(a.find('h'))
print()

# join

b = ",".join('abcd')
c = ",".join(['a', 'b', 'c'])

print(b)
print(c)
print()

# replace

d = "Life is too short"
print(d)
print(d.replace("Life", "Your legs"))
print()

# split
# 특정 문자열을 기준으로 텍스트 자르기
# 결과물은 list 형식으로 생성

e = "a b c d"
f = "a:b:c:d"

print(e)
print(e.split(" "))
print(f)
print(f.split(":"))
print()

